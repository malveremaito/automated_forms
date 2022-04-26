from django.urls import path
from . import views

urlpatterns = [
    path('forms', views.ict_homepage, name='forms'),
    path('view-requisition-form', views.viewrequisitionform, name='view-requisition-form'),
    path('', views.userdashboard, name='ict-home'),
    path('managerdashboard', views.managerdashboard, name='manager-dashboard'),
    path('insert-requisition-form', views.insertrequisitionform, name='insert-requisition-form'),
    path('viewregform/<int:id>', views.ictrequisitionformmodalview, name='reqform.view'),
    
]