#from re import TEMPLATE

from django.shortcuts import redirect, render 
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.contrib import messages     

# from django.contrib.auth.models import User, auth
# Create your views here.



def login_user(request):
    if request.method =="POST":
        username = request.POST['username']
        password =request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
           login(request,user)
           return redirect ('home')
        else:
            messages.success(request, 'Invalid Credentials!')
            return redirect("login")
    else:
        return render(request,'registration/login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out! "))
    return redirect ('login')


def change_password(request):
    return render(request,'change_password.html')

        

    


# def index(request):
#     return HttpResponse("Hello World")
