from django.contrib import admin
from .models import Payments,RequestType,Requests,RequestStatus


admin.site.register(RequestType)
admin.site.register(Payments)
admin.site.register(Requests)
admin.site.register(RequestStatus)