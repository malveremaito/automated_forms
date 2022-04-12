#from re import TEMPLATE
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def home(request):
    return render(request,"home/index.html")


# def index(request):
#     return HttpResponse("Hello World")