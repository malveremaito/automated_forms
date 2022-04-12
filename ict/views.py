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
def ictrequisitionform(request):
    if request.method =="POST":
        
            data = RequisitionForm()
            data.user=request.user;
            data.department=request.user.department;
            data.date=request.POST.get('date')
            data.service_requested=request.POST.get('service_requested')
            data.other_service=request.POST.get('other_service')
            data.reason_for_request=request.POST.get('reason_for_request')
            
        
            data.save()
        
            messages.success(request, 'Form Submitted Successfully ')
            return redirect("ict-home")  
    else:
        return render(request,"ict_requisition_form/ict-requisition-form.html")

@login_required
def userdashboard(request):
    requisitionforms = RequisitionForm.objects.all()
    totalrequests = RequisitionForm.objects.all().count()
    
    
    return render(request,"ict_user_dashboard/userdashboard.html",{'requisitionforms':requisitionforms,'totalrequests':totalrequests})

@login_required
def managerdashboard(request):
    return render(request,"manager/approval.html")

