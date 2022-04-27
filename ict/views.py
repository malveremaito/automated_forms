#from re import TEMPLATE
from django.contrib import messages
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import RequisitionForm
# Create your views here.


@login_required
def ict_homepage(request):
    return render(request,"home/forms.html")

@login_required
def viewrequisitionform(request):

    return render(request,"ict_requisition_form/ict-requisition-form.html")

@login_required   
def insertrequisitionform(request):
    
    if request.method =="POST":
            
            
            user=request.user
            department=request.user.department
            date=request.POST.get('date')
            if not date:
                messages.warning(request, 'Field Must Not Be empty!')
                return redirect("view-requisition-form")  
            start_time=request.POST.get('start_time')
            if not start_time:
                messages.warning(request, 'Field Must Not Be empty!')
                return redirect("view-requisition-form") 
            end_time=request.POST.get('end_time')
            
            service_requested=request.POST.get('service_requested')
            if not service_requested:
                messages.warning(request, 'Field Must Not Be empty!')
                return redirect("view-requisition-form")  
            other_service=request.POST.get('other_service')
            reason_for_request=request.POST.get('reason_for_request')
            if not reason_for_request:
                messages.warning(request, 'Field Must Not Be empty!')
                return redirect("view-requisition-form")  
            
            data = RequisitionForm(user=user,department=department,date=date,start_time=start_time,end_time=end_time,service_requested=service_requested,other_service=other_service,reason_for_request=reason_for_request)
            data.save()
        
            messages.success(request, 'Form Submitted Successfully ')
            return redirect("ict-home")  
    
@login_required
def viewmorequisitionform(request, id):
       
    data = RequisitionForm.objects.get(id=id)
    data
    return render(request, 'ict_requisition_form/view.html', {"data": data})

@login_required
def userdashboard(request):
    requisitionforms = RequisitionForm.objects.all()
    totalrequests = RequisitionForm.objects.all().count()   
    return render(request,"home/userdashboard.html",{'requisitionforms':requisitionforms,'totalrequests':totalrequests})

@login_required
def managerdashboard(request):
    requisitionforms = RequisitionForm.objects.all()
    totalrequests = RequisitionForm.objects.all().count()   
    return render(request,"manager/approval.html",{'requisitionforms':requisitionforms,'totalrequests':totalrequests})

@login_required
def viewmorequisitionformmanager(request, id):
       
    data = RequisitionForm.objects.get(id=id)
    data
    return render(request, 'manager/view.html', {"data": data})