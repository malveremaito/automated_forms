from django.contrib import admin
from import_export.admin import ExportActionMixin

from afterhours.models import AfterHoursForm

# Register your models here.

class AfterhoursAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('user', 'department', 'service_requested', 'other_service', 'reason_for_request', 'created_at', )
    # actions = [ict_requisition_form_csv]
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'department', 'service_requested', 'other_service', 'reason_for_request', ]
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    


admin.site.register(AfterHoursForm, AfterhoursAdmin)