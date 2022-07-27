from django.contrib import admin
from import_export.admin import ExportActionMixin

from afterhours.models import AfterHoursForm

# Register your models here.

class AfterhoursAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ( )
    # actions = [ict_requisition_form_csv]
    search_fields = [ ]
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    


admin.site.register(AfterHoursForm, AfterhoursAdmin)