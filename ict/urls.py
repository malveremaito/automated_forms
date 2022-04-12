from django.urls import path
from . import views

urlpatterns = [
    path('forms', views.ict_homepage, name='forms'),
    path('requisition-form', views.ictrequisitionform, name='ict-requisition-form'),
    path('', views.userdashboard, name='ict-home'),
    path('managerdashboard', views.managerdashboard, name='manager-dashboard')
]