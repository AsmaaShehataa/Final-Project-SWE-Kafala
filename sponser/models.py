from django.db import models
from django.db.models.deletion import CASCADE, PROTECT, ProtectedError
from datetime import date

# Create your models here.
class UserTypeModel(models.Model):
    UserTypeID = models.AutoField(primary_key=True)
    UserTypeName = models.CharField(max_length=250)
    def __str__(self):
        return self.UserTypeName

    class Meta:
        verbose_name = 'انواع المستخدمين'
        verbose_name_plural = 'انواع المستخدمين'


class UserStatusModel(models.Model):
    UserStatusID = models.AutoField(primary_key=True)
    UserStatusName = models.CharField(max_length=250)

    def __str__(self):
        return self.UserStatusName

    class Meta:
        verbose_name = 'حالات المستخدمين'
        verbose_name_plural = 'حالات المستخدمين'

class UserModel(models.Model):
    from orphanage.models import CityModel,CountryModel
    UserID         = models.AutoField(primary_key=True)
    Name           = models.CharField(max_length=200,blank=False)
    UserName       = models.CharField(max_length=200,blank=False)
    Password       = models.CharField(max_length=200,blank=False)
    UserBirthday   = models.DateField(default=date.today,blank=False)
    UserNationalID = models.CharField(max_length=200,blank=False)
    UserArea       = models.CharField(max_length=200)
    UserStreet     = models.CharField(max_length=200)
    UserCountryID  = models.ForeignKey(CountryModel, on_delete=PROTECT,null=True)
    UserCityID     = models.ForeignKey(CityModel, on_delete=PROTECT,null=True)
    UserStatusID   = models.ForeignKey(UserStatusModel, on_delete=PROTECT,null=True)
    UserTypeID     = models.ForeignKey(UserTypeModel, on_delete=PROTECT,null=True)
    UserProfile    = models.ImageField(null=True, blank=True,upload_to='upload/')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'كل المستخدمين'
        verbose_name_plural = 'كل المستخدمين'


class UserPhoneModel(models.Model):
    UserPhoneID = models.AutoField(primary_key=True)
    UserPhone = models.CharField(max_length=30)
    UserID = models.ForeignKey(UserModel, on_delete=PROTECT)

