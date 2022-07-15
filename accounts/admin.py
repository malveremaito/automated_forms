from django.contrib import admin
from accounts.models import Department, Role, Unit
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ExportActionMixin

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


class UnitAdmin(admin.ModelAdmin):
    list_display = ('user', 'unit')
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'unit', ]
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Role, RoleAdmin)


class Departments(admin.StackedInline):
    model = Department
    can_delete = False

class Units(admin.StackedInline):
    model = Unit
    can_delete = False


class Roles(admin.StackedInline):
    model = Role
    can_delete = False


class CustomizedUserAdmin (ExportActionMixin,UserAdmin):
    inlines = (Departments, Roles,Units, )


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)



