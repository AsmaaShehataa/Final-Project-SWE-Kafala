from django import forms
from .models import ChildrensModel, ChildImageModel, AdoptionTypeModel, OrphanageModel, CityModel
from sponser.models import UserModel, UserTypeModel
from django.db import transaction
from django.contrib.auth.models import User

class DayInput(forms.DateInput):
    input_type = 'date'


class ChildForm(forms.ModelForm):
    class Meta:
        model = ChildrensModel
        fields = (
            "RealName", "NationalID", "HisDream", "BirthDate", "CostPrice", "AdoptionTypeID", "CaseHistory",
            "HealthStatus")
        labels = {
            "RealName": "الاسم الكامل للطفل",
            "NationalID": " الرقم القومي",
            "HisDream": "حلم الطفل ",
            "BirthDate": "تاريخ ميلاد الطفل ",
            "CostPrice": "تكلفة كفالة الطفل",
            "AdoptionTypeID": " نوع التبني",
            "CaseHistory": "الحالة الصحية",
            "HealthStatus": "وصف الحالة الصحية ",
        }
        widgets = {
            'RealName': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'NationalID': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'HisDream': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'BirthDate': DayInput(attrs={'class': 'form-control input-field'}),
            'CostPrice': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'AdoptionTypeID': forms.Select(attrs={'class': 'form-control input-field'}),
            'CaseHistory': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'HealthStatus': forms.Textarea(attrs={'class': 'form-control input-field'}),
        }


class UploadChildImageForm(forms.ModelForm):
    class Meta:
        model = ChildImageModel
        fields = ("ChildImage", "ChildID")
        labels = {
            "ChildImage": "رفع صور للطفل",
            "ChildID": "اسم الطفل"
        }
        widgets = {
            'ChildID': forms.Select(attrs={'class': 'form-control input-field'}),
        }

        def __init__(self, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)
            self.fields['ChildImage'].widget.attrs['class'] = 'form-control input-field'


class AdvancedChildSearch(forms.Form):
    Name = forms.CharField(max_length=100, label='اسم الطفل')
    Name.widget.attrs.update({'class': 'form-control input-md'})
    Adoption = forms.ModelChoiceField(queryset=AdoptionTypeModel.objects.all(), label='نوع التبني')
    Adoption.widget.attrs.update({'class': 'form-control input-md'})
    CivilID = forms.CharField(max_length=100,label='الرقم القومي')
    CivilID.widget.attrs.update({'class': 'form-control'})



class LoginForm(forms.Form):
    username = forms.CharField(label= 'اسم الدخول',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='كلمة المرور ',
                      widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ("Name" ,"UserName" ,"Password" ,"UserBirthday","UserNationalID","UserArea","UserStreet"
        ,"UserCityID" ,"UserProfile")
        labels = {
            "Name": "اسم الدار بالكامل",
            "UserName": "كلمة الدخول",
            "Password": "كلمة المرور",
            "label": "المحافظة",
            "UserBirthday": "تاريخ الانشاء ",
            "UserNationalID": "الرقم القومي",
            "UserArea": "المنطقة",
            "UserStreet": "عنوان الشارع",
            "UserProfile": "صورة البروفيل",
            "UserCityID": "المحافظة",
            "UserProfile": "رفع صورة",

        }
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'UserName': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control input-field'},),
            'UserBirthday': DayInput(attrs={'class': 'form-control input-field'}),
            'UserCityID': forms.Select(attrs={'class': 'form-control input-field'}),
            'UserNationalID': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'UserArea': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'UserStreet': forms.TextInput(attrs={'class': 'form-control input-field'}),
        }

        def __init__(self, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)
            self.fields['UserProfile'].widget.attrs['class'] = 'form-control input-field'


class ProfileOrphanageForm(forms.ModelForm):
    class Meta:
        model = OrphanageModel
        fields = ("CEO" ,"Description" ,"PermissionNo" ,"CommercialNo","StartDate","Website","CityID","Notes")
        labels = {
            "CEO": "اسم المدير  ",
            "Description": "الوصف",
            "PermissionNo" : "رقم الإذن",
            "CommercialNo" : "رقم تجاري",
            "StartDate"    : "تاريخ الانشاء ",
            "Website": "الموقع الالكتروني",
            "CityID": "المحافظة",
            "Notes": " ملاحظات",
        }
        widgets = {
            'CEO': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'Description': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'PermissionNo': forms.TextInput(attrs={'class': 'form-control input-field'},),
            'CommercialNo': forms.TextInput(attrs={'class': 'form-control input-field'}, ),
            'StartDate': DayInput(attrs={'class': 'form-control input-field'}),
            'Website': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'Notes': forms.TextInput(attrs={'class': 'form-control input-field'}),
        }

        def __init__(self, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)
            self.fields['UserProfile'].widget.attrs['class'] = 'form-control input-field'




