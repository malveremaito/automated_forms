from pyexpat import model
from tabnanny import verbose
from django.contrib import admin
from accounts.models import Department, Role
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountInLine(admin.StackedInline):
    model = Department
    can_delete = False
    
class Roles(admin.StackedInline):
    model = Role
    can_delete = False


class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInLine,Roles )



admin.site.unregister(User) 
admin.site.register(User,CustomizedUserAdmin)    
admin.site.register(Department)   
admin.site.register(Role)  
