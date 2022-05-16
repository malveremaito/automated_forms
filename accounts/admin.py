from django.contrib import admin
from accounts.models import Department, Role
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class RoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'roles')
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'roles', ]
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'department')
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'department', ]
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Department, DepartmentAdmin)


admin.site.register(Role, RoleAdmin)


class AccountInLine(admin.StackedInline):
    model = Department
    can_delete = False


class Roles(admin.StackedInline):
    model = Role
    can_delete = False


class CustomizedUserAdmin (UserAdmin):
    inlines = (AccountInLine, Roles, )


admin.site.unregister(User)


admin.site.register(User, CustomizedUserAdmin)

