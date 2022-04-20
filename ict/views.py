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
    data = RequisitionForm(user=request.user, department=request.user.department, date=request.POST['date'], service_requested=request.POST['service_requested'], other_service=request.POST['other_service'],reason_for_request=request.POST['reason_for_request'])
    data.save()
    return redirect('/')




@login_required
def userdashboard(request):
    requisitionforms = RequisitionForm.objects.all()
    totalrequests = RequisitionForm.objects.all().count()
    
    
    return render(request,"ict_user_dashboard/userdashboard.html",{'requisitionforms':requisitionforms,'totalrequests':totalrequests})

@login_required
def managerdashboard(request):
    return render(request,"manager/approval.html")

