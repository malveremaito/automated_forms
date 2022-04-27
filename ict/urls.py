from django.urls import path
from . import views

urlpatterns = [
    path('forms', views.ict_homepage, name='forms'),
    path('view-requisition-form', views.viewrequisitionform, name='view-requisition-form'),
    path('', views.userdashboard, name='ict-home'),
    path('managerdashboard', views.managerdashboard, name='manager-dashboard'),
    path('insert-requisition-form', views.insertrequisitionform, name='insert-requisition-form'),
    path('view-more-requisition-form/<int:id>', views.viewmorequisitionform, name='view.more.requisitionform'),
    path('view-more-requisition-form-manager/<int:id>', views.viewmorequisitionformmanager, name='manager.view.more.requisitionform'),
    
]