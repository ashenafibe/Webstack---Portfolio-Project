from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,AdminHOD,ClientUser,OperationUser,FinanceUser,ManagerUser
# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)
admin.site.register(AdminHOD)
admin.site.register(ClientUser)
admin.site.register(OperationUser)
admin.site.register(FinanceUser)
admin.site.register(ManagerUser)


