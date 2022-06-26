import csv
from urllib import response
from django.contrib import admin
import decimal, csv
from django.http import HttpResponse
from ict_requisition.models import ICTRequisitionForm

# Register your models here.
# admin.site.register(ICTRequisitionForm)  
 


# def ict_requisition_form_csv(modeladmin, request, queryset):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="books.csv"'
#     writer = csv.writer(response)
#     writer.writerow(['User', 'Department', 'SERVICE REQUESTED', 'OTHER SERVICE', 'REASONS'])
#     ICTRequisitionForm = queryset.values_list('user', 'department', 'service_requested', 'other_service', 'reason_for_request')
#     for ICTRequisitionForms in ICTRequisitionForm:
#         writer.writerow(ICTRequisitionForm)
#     return response
# ict_requisition_form_csv.short_description = 'Export to csv'



class ICTRequisitionFormAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'service_requested', 'other_service', 'reason_for_request', 'created_at', )
    # actions = [ict_requisition_form_csv]
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'department', 'service_requested', 'other_service', 'reason_for_request', ]
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    


admin.site.register(ICTRequisitionForm, ICTRequisitionFormAdmin)


    
