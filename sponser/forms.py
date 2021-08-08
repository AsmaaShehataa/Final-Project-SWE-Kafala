from django import forms
from .models import UserModel, UserTypeModel
from django.db import transaction
from django.contrib.auth.models import User
from admin_kafala.models import Requests,RequestType,RequestStatus

class DayInput(forms.DateInput):
    input_type = 'date'


class LoginForm(forms.Form):
    username = forms.CharField(label= 'اسم الدخول',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='كلمة المرور ',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ("Name" ,"UserName" ,"Password" ,"UserBirthday","UserNationalID","UserArea","UserStreet"
                  ,"UserCountryID","UserProfile")
        labels = {
            "Name": "اسم الكفيل بالكامل",
            "UserName": "كلمة الدخول",
            "Password": "كلمة المرور",
            "label": "المحافظة",
            "UserBirthday": "تاريخ ميلاد ",
            "UserNationalID": "الرقم القومي او رقم الجواز",
            "UserArea": "المنطقة",
            "UserStreet": "عنوان الشارع",
            "UserProfile": "صورة البروفيل",
            "UserCountryID": "البلد",
            "UserProfile": "رفع صورة",

        }
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'UserName': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control input-field'},),
            'UserBirthday': DayInput(attrs={'class': 'form-control input-field'}),
            'UserCountryID': forms.Select(attrs={'class': 'form-control input-field'}),
            'UserNationalID': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'UserArea': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'UserStreet': forms.TextInput(attrs={'class': 'form-control input-field'}),
        }

        def __init__(self, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)
            self.fields['UserProfile'].widget.attrs['class'] = 'form-control input-field'






class UpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ("Name" ,"UserName" ,"Password" ,"UserBirthday","UserNationalID","UserArea","UserStreet"
                  ,"UserCountryID","UserProfile")
        labels = {
            "Name": "اسم الكفيل بالكامل",
            "UserName": "كلمة الدخول",
            "Password": "كلمة المرور",
            "label": "المحافظة",
            "UserBirthday": "تاريخ ميلاد ",
            "UserNationalID": "الرقم القومي او رقم الجواز",
            "UserArea": "المنطقة",
            "UserStreet": "عنوان الشارع",
            "UserProfile": "صورة البروفيل",
            "UserCountryID": "البلد",
            "UserProfile": "رفع صورة",

        }
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'UserName': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control input-field'},),
            'UserBirthday': DayInput(attrs={'class': 'form-control input-field'}),
            'UserCountryID': forms.Select(attrs={'class': 'form-control input-field'}),
            'UserNationalID': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'UserArea': forms.TextInput(attrs={'class': 'form-control input-field'}),
            'UserStreet': forms.TextInput(attrs={'class': 'form-control input-field'}),
        }

        def __init__(self, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)
            self.fields['UserProfile'].widget.attrs['class'] = 'form-control input-field'

class MakeRequestForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ("RequestDate", "RequestFileUpload")
        labels = {
            "RequestDate": "تاريخ ميلاد ",
            "RequestFileUpload": "رفع مرفق للثبات",
        }
        widgets = {
            'RequestDate': DayInput(attrs={'class': 'form-control input-field'})
        }

        def __init__(self, *args, **kwargs):
            super(MyForm, self).__init__(*args, **kwargs)
            self.fields['RequestFileUpload'].widget.attrs['class'] = 'form-control input-field'





