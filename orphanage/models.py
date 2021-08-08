from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models import OneToOneField
from django.db.models.deletion import CASCADE, PROTECT, ProtectedError


class CountryModel(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'البلاد'
        verbose_name_plural = 'البلاد'



class CityModel(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = 'المحافظات'
        verbose_name_plural =  'المحافظات'



class OrphanageModel(models.Model):
    from sponser.models import UserModel
    OrphanageID = models.AutoField(primary_key=True)
    UserID      = models.ForeignKey(UserModel, on_delete=PROTECT, default=0)
    CEO         = models.CharField(max_length=1000, blank=True)
    Description = models.CharField(max_length=1000, blank=True)
    PermissionNo = models.CharField(max_length=250)
    CommercialNo = models.CharField(max_length=250)
    StartDate    = models.DateField()
    Website = models.CharField(max_length=500)
    CityID = models.ForeignKey(CityModel, on_delete=PROTECT, default=0)
    Notes = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'دار الايتام '
        verbose_name_plural = 'دار الايتام '


class AdoptionTypeModel(models.Model):
    AdoptionTypeID = models.AutoField(primary_key=True)
    AdoptionTypeName = models.CharField(max_length=250)

    def __str__(self):
        return self.AdoptionTypeName

    class Meta:
        verbose_name = 'انواع التبني'
        verbose_name_plural  = 'انواع التبني'


class ChildrensModel(models.Model):
    ChildID = models.AutoField(primary_key=True)
    RealName = models.CharField(max_length=250, blank=True)
    NationalID = models.CharField(max_length=12, blank=True)
    HisDream = models.CharField(max_length=250, blank=True)
    BirthDate = models.DateField(null=True)
    OrphanageID = models.ForeignKey(OrphanageModel, on_delete=models.CASCADE,null=True)
    CostPrice = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    AdoptionTypeID = models.ForeignKey(AdoptionTypeModel, on_delete=models.CASCADE,null=True)
    CaseHistory = models.CharField(max_length=500, blank=True)
    HealthStatus = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.RealName

    class Meta:
        verbose_name = 'الاطفال'
        verbose_name_plural = 'الاطفال'


class ChildImageModel(models.Model):
    ChildImageID = models.AutoField(primary_key=True)
    ChildID      = models.ForeignKey(ChildrensModel, on_delete=PROTECT, default=0,related_name = "child_id")
    ChildImage   = models.ImageField(null=True, blank=True,upload_to='upload/')

  #  def __str__(self):
     #   return '%s' % (self.ChildID.RealName)

    class Meta:
        verbose_name = 'صور الاطفال'
        verbose_name_plural ='صور الاطفال'



