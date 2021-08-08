from django.contrib import admin
from .models import UserStatusModel,UserTypeModel,UserModel

admin.site.register(UserModel)
admin.site.register(UserStatusModel)
admin.site.register(UserTypeModel)



