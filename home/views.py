#from re import TEMPLATE
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ict_requisition.models import ICTRequisitionForm
# Create your views here.

@login_required
def home(request):
    totalrequests = ICTRequisitionForm.objects.all().count()  
    return render(request,"home/index.html",{'totalrequests':totalrequests})
