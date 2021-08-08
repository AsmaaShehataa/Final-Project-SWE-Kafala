from django.db import models
from django.db.models.deletion  import CASCADE, PROTECT, ProtectedError
from datetime import date

class RequestStatus(models.Model):
    RequestStatusID = models.AutoField(primary_key=True)
    RequestStatusName = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.RequestStatusName

    class Meta:
        verbose_name = 'حالات الطلب'
        verbose_name_plural =  'حالات الطلب'




class RequestType(models.Model):
    RequestTypeID = models.AutoField(primary_key=True)
    RequestTypeName = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.RequestTypeName

    class Meta:
        verbose_name = 'انواع الطلب'
        verbose_name_plural =  'انواع الطلب'

# Create your models here.
class Requests(models.Model):
    from sponser.models import UserModel
    from orphanage.models import OrphanageModel,ChildrensModel
    RequestID         = models.AutoField(primary_key=True)
    RequestTypeID     = models.ForeignKey(RequestType, on_delete=PROTECT,null=True)
    RequestFileUpload = models.FileField(null=True, blank=True,upload_to='upload/')
    UserID            = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    ChildID           = models.ForeignKey(ChildrensModel, on_delete=models.CASCADE, null=True)
    OrphanageID       = models.ForeignKey(OrphanageModel, on_delete=models.CASCADE, null=True)
    RequestStatusID   = models.ForeignKey(RequestStatus, on_delete=models.CASCADE, null=True)
    RequestDate       = models.DateField(default=date.today,blank=False)

    def __str__(self):
        return'New Request Number: {}'.format(self.RequestID)


    class Meta:
        verbose_name = 'الطلبات'
        verbose_name_plural = 'الطلبات'


class Payments(models.Model):
    from sponser.models import UserModel
    PaymenID = models.AutoField(primary_key=True)
    PayAmount = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=False)
    RequestID = models.ForeignKey(Requests, on_delete=PROTECT, default=0)
    UserID = models.ForeignKey(UserModel, on_delete=PROTECT, default=0)
    PayDate = models.DateField(auto_now_add=True, blank=True)


    class Meta:
        verbose_name = 'الدفع الالكتروني'
        verbose_name_plural = 'الدفع الالكتروني'

