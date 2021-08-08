from django.shortcuts import render
from orphanage.models import OrphanageModel,ChildrensModel,ChildImageModel,CountryModel,CityModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from .models import UserModel, UserTypeModel,UserStatusModel
from admin_kafala.models import Requests,RequestStatus,RequestType
from django.http import HttpResponse
from sponser.forms import MakeRequestForm
from django.core.exceptions import FieldDoesNotExist
from django.forms.models import model_to_dict


def view_index(request):
    orphange       = OrphanageModel.objects.all()[:6]
    childs         = ChildImageModel.objects.all()[:6]
    context = {"orphange": orphange,"childs" : childs}
    return render(request, 'sponser/index.html',context)


def view_about(request):
    return render(request, 'sponser/about.html')


def view_contact_us(request):
    return render(request, 'sponser/contact_us.html')

def view_all_child(request):
    inside_child = ChildrensModel.objects.filter(AdoptionTypeID=2)
    childs_in = []
    for ch in inside_child:
        images = ChildImageModel.objects.all().filter(ChildID=ch.ChildID).first()
        dict = {"id": ch.ChildID, "name": ch.RealName, "image": images.ChildImage} 

        childs_in.append(dict)

    out_child = ChildrensModel.objects.filter(AdoptionTypeID=1)
    childs_out = []
    for ch in out_child:
        images = ChildImageModel.objects.all().filter(ChildID=ch.ChildID).first()
        if images:
            Ci= images.ChildID_id
        else: 
            Ci= 'No images set'

        


        dict = {"id": ch.ChildID, "name": ch.RealName, "image": Ci}
        print(Ci)
        
        childs_out.append(dict)

    context = {"childs_out": childs_out, "childs_in": childs_in}
    return render(request, 'sponser/all_child.html',context)

def view_child(request):
    return render(request, 'orphanage/child.html')



##### profile
def update_profile(request):
    page_name = "orphanage/add_new_child_form.html"
    sponsor = UserModel.objects.get(UserID=request.session['sponser_id'])
    form = RegisterForm(instance=sponsor)
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=sponsor)
        try:
            if form.is_valid():
                form.save()
                form = RegisterForm(request.POST, instance=sponsor)
                context = {'form': form}
                messages.success(request, 'تمت عملية التعديل بنجاح')
                return render(request,page_name, context)
            else:
                form = RegisterForm(instance=sponsor)
                context = {'form': form}
                messages.success(request, 'من فضلك املا الحقول الفارغة')
                return render(request,page_name, context)
        except AssertionError as error:
            print(error)
    context = {'form': form}
    return render(request, page_name, context)




def view_team_work(request):
    return render(request, 'sponser/team_work.html')



def view_sponser_child(request):
    requests = Requests.objects.filter(UserID=request.session['sponser_id'])
    childs_in = []
    for ch in requests:
        images = ChildImageModel.objects.all().select_related("ChildID").filter(ChildID=ch.ChildID.ChildID).first()
        dict = {"id":ch.ChildID.ChildID,
                "RealName": ch.ChildID.RealName,
                "image": images.ChildImage.url,
                "BirthDate":ch.ChildID.BirthDate,
                "NationalID":ch.ChildID.NationalID}
        childs_in.append(dict)
    context = {"childs": childs_in}
    return render(request, 'sponser/view_sponser_child.html', context)



def sponser_login(request):
    field1 = None
    try:
        field1 = request.session['sponser_user']
    except KeyError:
            page_name = 'sponser/sponser_login.html'
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
                    user.UserCityID = CityModel.objects.get(ID=1)
                    user.UserStatusID = UserStatusModel.objects.get(UserStatusID=2)
                    user.UserTypeID = UserTypeModel.objects.get(UserTypeID=2)
                    user.UserProfile = request.POST['UserProfile']
                    user.save()
                    messages.success(request,
                                     'شكرا للاشتراك معانا في موقع كفالة يمكنك الدخول بعد ٢٤ ساعة بعد التاكد من بياناتك ')
                    return render(request, page_name, context)
                else:
                    messages.success(request, 'يوجد مشكلة في التسجيل برجاء حاول مرة اخري')
                    return render(request, page_name, context)

            elif "Login_Form" in request.POST:
                try:
                    if request.method == 'POST':
                        users = UserModel.objects.get(UserName=request.POST['username'], Password=request.POST['password'],
                                                      UserTypeID=2)
                        user = users
                        if user.UserStatusID == UserStatusModel.objects.get(UserStatusID=1):
                            sponser_dashboard = 'sponser/sponser_dashboard.html'
                            request.session['sponser_user'] = user.UserName
                            request.session['sponser_pass'] = user.Password
                            request.session['sponser_id'] = user.UserID
                            return render(request, sponser_dashboard, context)

                        elif user.UserStatusID == UserStatusModel.objects.get(UserStatusID=2):
                            messages.success(request, 'لم يتم تفعيل حسابك الشخصي')
                            return render(request, page_name, context)

                        else:
                            messages.success(request, 'من فضلك يوجد مشكلة اتصل بالادمن')
                            return render(request, page_name, context)

                    else:
                        messages.success(request, 'عفوا كلمة الدخول و كلمة المرور غير صحيحة')
                        return render(request, page_name, context)

                except Exception as e:
                    messages.success(request, e)
                    return render(request, page_name, context)
            else:
                context = {'form': form, "LoginForm": loginForm}
                return render(request, page_name, context)
    context = {'form': form, "LoginForm": loginForm}
    return render(request, page_name, context)

    if field1:
        return view_sponser_child(request)

# make_request
def make_request(request):
    field1 = None
    try:
        field1 = request.session['sponser_user']
    except FieldDoesNotExist:
        page_name = 'sponser/sponser_login.html'
        form = RegisterForm()
        loginForm = LoginForm()
        context = {'form': form, "LoginForm": loginForm}
        return render(request, page_name, context)

    if field1:
        page_name = "orphanage/make_request.html"
        makeRequestForm = MakeRequestForm()
        context = {"form": makeRequestForm}

        try:
            if request.method == 'POST':
                request1                 = Requests.objects.create()
                request1.RequestTypeID   = RequestType.objects.get(RequestTypeID=1)
                request1.UserID          = UserModel.objects.get(UserID=request.session['sponser_id'])
                request1.RequestDate     = request.POST['RequestDate']
                request1.ChildID         = ChildrensModel.objects.get(ChildID=request.GET['child_id'])
                request1.OrphanageID     = OrphanageModel.objects.get(OrphanageID=request.GET['orphnage'])
                request1.RequestStatusID = RequestStatus.objects.get(RequestStatusID=1)
                request1.save()
                messages.success(request,'تمت عملية رفع الملفات بنجاح سوف يتم مراجعة طلبك و الرد عليك في القريب العاجل')
                return render(request, page_name, context)
            else:
                makeRequestForm = MakeRequestForm()
                context = {"form": makeRequestForm}
                messages.success(request, 'يوجد مشكلة في التسجيل برجاء حاول مرة اخري')
                return render(request, page_name, context)
        except Exception as e:
            makeRequestForm = MakeRequestForm()
            context = {"form": makeRequestForm}
            messages.success(request,e)
            return render(request, page_name, context)
    else:
        makeRequestForm = MakeRequestForm()
        context = {"form": makeRequestForm}
        messages.success(request, 'يوجد مشكلة في التسجيل برجاء حاول مرة اخري')
        return render(request, page_name, context)


def view_all_request(request):
    requests = Requests.objects.filter(UserID=request.session['sponser_id'])
    context = {"requests": requests}
    return render(request, 'sponser/view_all_request.html', context)



def sponser_child_details(request, pk):
    image_arr = []
    child  = ChildrensModel.objects.get(ChildID=pk)
    for img in ChildImageModel.objects.filter(ChildID=child.ChildID):
        dict = {"image": img.ChildImage.url}
        image_arr.append(dict)
    context = {'child': child,'images':image_arr}
    return render(request, 'sponser/child_detail_sponser.html', context)


def detials_requests(request,pk):
    array_request = Requests.objects.get(RequestID=pk)
    context = {"array_request": array_request}
    return render(request, 'sponser/view_detials_requests.html', context)


def logout(request):
    del request.session['sponser_user']
    del request.session['sponser_pass']
    del request.session['sponser_id']
    page_name = 'sponser/sponser_login.html'
    messages.success(request, 'شكرا لك لقد خرجت من الموقع')
    return render(request,page_name)

