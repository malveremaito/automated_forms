from django.contrib import admin
from ict_requisition.models import ICTRequisitionForm

# Register your models here.
# admin.site.register(ICTRequisitionForm)  
 


class ICTRequisitionFormAdmin(admin.ModelAdmin):
    list_display = ('user','department','service_requested','other_service','reason_for_request','created_at')
    search_fields = ['user__username','user__first_name','user__last_name','department','service_requested','other_service','reason_for_request',]
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(ICTRequisitionForm, ICTRequisitionFormAdmin)