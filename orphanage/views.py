from django.shortcuts import render, redirect
from .serializers import CountrySerializer, CitySerializer, OrphanageSerializer
from .models import CountryModel, CityModel, OrphanageModel, ChildrensModel, AdoptionTypeModel, ChildImageModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import ChildForm, UploadChildImageForm, AdvancedChildSearch, RegisterForm, LoginForm,ProfileOrphanageForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from sponser.models import UserModel, UserTypeModel, UserStatusModel
from django.views.generic import CreateView
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import FieldDoesNotExist


def view_index(request):
    return render(request, 'orphanage/index.html')


# View all Orphange
def view_all_orphange(request):
    orphanges = OrphanageModel.objects.all()
    print(orphanges)
    context = {"orphanges": orphanges}
    return render(request, 'orphanage/view_all_orphange.html', context)


# Orphanage Detials
def orphange_detials(request, pk):
    orphange = OrphanageModel.objects.get(OrphanageID=pk)
    inside_child = ChildrensModel.objects.filter(OrphanageID=orphange, AdoptionTypeID=2)
    childs_in = []
    for ch in inside_child:
        images = ChildImageModel.objects.all().select_related("ChildID").filter(ChildID=ch.ChildID).first()
        dict = {"id": ch.ChildID, "name": ch.RealName, "image": images.ChildImage.url}
        childs_in.append(dict)

    out_child = ChildrensModel.objects.filter(OrphanageID=orphange, AdoptionTypeID=1)

    childs_out = []
    for ch in out_child:
        images = ChildImageModel.objects.all().select_related("ChildID").filter(ChildID=ch.ChildID).first()
        dict = {"id": ch.ChildID, "name": ch.RealName, "image": images.ChildImage.url}
        childs_out.append(dict)

    context = {"orphange": orphange, "childs_out": childs_out, "childs_in": childs_in}
    return render(request, 'orphanage/orphange_details.html', context)


def detials_child(request, pk):
    child = ChildrensModel.objects.get(ChildID=pk)
    image = ChildImageModel.objects.filter(ChildID=pk)
    context = {'child': child, "image": image}
    return render(request, 'sponser/child_detail.html', context)


def view_index(request):
    return render(request, 'orphanage/index.html')


def view_dashboard(request):
    return render(request, 'orphanage/dashboard.html')


def view_child(request):
    childs = ChildrensModel.objects.filter(OrphanageID=request.session['orphanage'])
    count = ChildrensModel.objects.count()
    context = {'childs': childs, "count": count}
    return render(request, 'orphanage/child.html', context)


def view_child_detials(request, pk):
    child = ChildrensModel.objects.get(ChildID=pk)
    context = {'child': child}
    return render(request, 'orphanage/child_detail.html', context)


def add_new_child_form(request):
    form = ChildForm()
    if request.method == 'POST':
        form = ChildForm(request.POST)
        context = {'form': form}
        try:
            if request.method == 'POST':

                child1             = ChildrensModel.objects.create()
                child1.OrphanageID =  OrphanageModel.objects.get(OrphanageID=request.session['orphanage'])
                child1.RealName    = request.POST['RealName']
                child1.NationalID  = request.POST['NationalID']
                child1.HisDream    = request.POST['HisDream']
                child1.BirthDate   = request.POST['BirthDate']
                child1.CostPrice      = request.POST['CostPrice']
                child1.AdoptionTypeID =  AdoptionTypeModel.objects.get(AdoptionTypeID=request.POST['AdoptionTypeID'])
                child1.CaseHistory =  request.POST['CaseHistory']
                child1.HealthStatus = request.POST['HealthStatus']
                child1.save()

                messages.success(request, 'تمت عملية الحفظ بنجاح')
                return render(request, 'orphanage/add_new_child_form.html', context)
            else:
                form = ChildForm()
                context = {'form': form}
                messages.success(request, 'من فضلك املا الحقول الفارغة')
                return render(request, 'orphanage/add_new_child_form.html', context)
        except AssertionError as error:
            print(error)
    context = {'form': form}
    return render(request, 'orphanage/add_new_child_form.html', context)


def upload_image_child(request):
    uploadForm = UploadChildImageForm()
    if request.POST:
        uploadForm = UploadChildImageForm(request.POST, request.FILES)
        if uploadForm.is_valid():
            uploadForm.save()
            uploadForm = UploadChildImageForm()
            context = {'form': uploadForm}
            messages.success(request, 'تمت عملية الحفظ بنجاح')
            return render(request, 'orphanage/upload_image_child.html', context)
        else:
            form = ChildForm()
            context = {'form': form}
            messages.success(request, 'من فضلك املا الحقول الفارغة')
            return render(request, 'orphanage/upload_image_child.html', context)

    context = {'form': uploadForm}
    return render(request, 'orphanage/upload_image_child.html', context)


def update_child(request, pk):
    child = ChildrensModel.objects.get(ID=pk)
    form = ChildForm(instance=child)

    if request.method == 'POST':
        form = ChildForm(request.POST, instance=child)
        try:
            if form.is_valid():
                form.save()
                form = ChildForm(instance=child)
                context = {'form': form}
                messages.success(request, 'تمت عملية التعديل بنجاح')
                return render(request, 'orphanage/update_child.html', context)
            else:
                form = ChildForm(instance=child)
                context = {'form': form}
                messages.success(request, 'من فضلك املا الحقول الفارغة')
                return render(request, 'orphanage/update_child.html', context)
        except AssertionError as error:
            print(error)
    context = {'form': form}
    return render(request, 'orphanage/update_child.html', context)


def search_child(request):
    form = AdvancedChildSearch()
    context = {'form': form}
    q = ""
    results = []
    query = Q()
    if 'q' in request.GET:
         form =  AdvancedChildSearch(request.POST)
         if form.is_valid():
             # q = form.cleaned_data['q']
             # if q is not None:
             #    quer &= Q(title__contains=q)
             #    result = ChildrensModel.objects.filter(query)
             #    context = {'form': form,'result':result}
                return render(request, 'orphanage/search_child.html', context)

    return render(request, 'orphanage/search_child.html', context)


def register_orphange(request):
    field1 = None
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))

    try:
        field1 = request.session['orphanage'] # If found will jump to line 248
    except KeyError:
        #If he didn't find the orphanage key inside the session array, will get into the exception 
        #will check the post request (login form or the register form )

        form = RegisterForm()
        loginForm = LoginForm()
        context = {'form': form, "LoginForm": loginForm}
        if "Register_Form" in request.POST:
            if request.method == 'POST':
                user = UserModel.objects.create()
                user.Name = request.POST['Name']
                user.UserName = request.POST['UserName']
                user.Password = request.POST['Password']
                user.UserBirthday = request.POST['UserBirthday']
                user.UserNationalID = request.POST['UserNationalID']
                user.UserArea = request.POST['UserArea']
                user.UserStreet = request.POST['UserStreet']
                user.UserCountryID = CountryModel.objects.get(ID=1)
                user.UserCityID = CityModel.objects.get(ID=request.POST['UserCityID'])
                user.UserStatusID = UserStatusModel.objects.get(UserStatusID=2)
                user.UserTypeID = UserTypeModel.objects.get(UserTypeID=1)
                user.UserProfile = request.POST['UserProfile']
                user.save()
                messages.success(request,
                                 'شكرا للاشتراك معانا في موقع كفالة يمكنك الدخول بعد ٢٤ ساعة بعد التاكد من بياناتك ')
                return render(request, 'orphanage/login_orphange.html', context)
            else:
                messages.success(request, 'يوجد مشكلة في التسجيل برجاء حاول مرة اخري')
                return render(request, 'orphanage/login_orphange.html', context)

        elif "Login_Form" in request.POST:
            try:
                if request.method == 'POST':
                    #Filter all the users(user model -all database users) that match the username & password sent by the form (login form)
                
                    users = UserModel.objects.filter(UserName=request.POST['username'], 
                                                     Password=request.POST['password'], UserTypeID=1)
                    user = users
                    orphanage = OrphanageModel.objects.filter(UserID=user[0].UserID)

                    if user[0].UserStatusID == UserStatusModel.objects.get(UserStatusID=1):
                        request.session['username'] = user[0].UserName
                        request.session['password'] = user[0].Password
                        request.session['orphanage'] = orphanage[0].OrphanageID
                        request.session['user_id'] = user[0].UserID
                        return view_child(request)

                    elif user[0].UserStatusID == UserStatusModel.objects.get(UserStatusID=2):
                        messages.success(request, 'لم يتم تفعيل حسابك الشخصي')
                        return render(request, 'orphanage/login_orphange.html', context)

                    else:
                        messages.success(request, 'من فضلك يوجد مشكلة اتصل بالادمن')
                        return render(request, 'orphanage/login_orphange.html', context)

                else:
                    messages.success(request, 'عفوا كلمة الدخول و كلمة المرور غير صحيحة')
                    return render(request, 'orphanage/login_orphange.html', context)
            except:
                messages.success(request, 'عفوا كلمة الدخول و كلمة المرور غير صحيحة')
                return render(request, 'orphanage/login_orphange.html', context)
        else:
            context = {'form': form, "LoginForm": loginForm}
            return render(request, 'orphanage/login_orphange.html', context)

    if field1:
        return view_child(request)


# update_profile
def update_profile_orphange(request):
    page_name = "orphanage/update_profile.html"
    orphanage = UserModel.objects.get(UserID=request.session['user_id'])
    form    = RegisterForm(instance=orphanage)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=orphanage)
        try:
            if form.is_valid():
                form.save()
                form = RegisterForm(request.POST, instance=orphanage)
                context = {'form': form}
                messages.success(request, 'تمت عملية التعديل بنجاح')
                return render(request,page_name, context)
            else:
                form = RegisterForm(instance=orphanage)
                context = {'form': form}
                messages.success(request, 'من فضلك املا الحقول الفارغة')
                return render(request,page_name, context)
        except AssertionError as error:
            print(error)
    context = {'form': form}
    return render(request, page_name, context)



def more_info_orphange(request):
    page_name = "orphanage/more_info.html"
    orphanage = OrphanageModel.objects.get(OrphanageID=request.session['orphanage'])
    form = ProfileOrphanageForm(instance=orphanage)
    if request.method == 'POST':
        form = ProfileOrphanageForm(request.POST, instance=orphanage)
        try:
            if form.is_valid():
                form.save()
                form = ProfileOrphanageForm(request.POST, instance=orphanage)
                context = {'form': form}
                messages.success(request, 'تمت عملية التعديل بنجاح')
                return render(request, page_name, context)
            else:
                form = ProfileOrphanageForm(instance=orphanage)
                context = {'form': form}
                messages.success(request, 'من فضلك املا الحقول الفارغة')
                return render(request, page_name, context)
        except AssertionError as error:
            print(error)
    context = {'form': form}
    return render(request, page_name, context)

