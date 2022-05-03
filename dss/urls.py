from django.urls import path
from . import views

urlpatterns = [
#Users
    path('forms', views.forms, name='forms'),
    path('dashboard', views.userdashboard, name='dashboard'),
    path('approvals', views.approvals, name='approvals'),
    
    path('more/<int:id>', views.more, name='more'),


#Forms
<<<<<<< HEAD
<<<<<<< HEAD
    path('ictrequisitionform', views.requisitionform, name='requisitionform'),
=======
    path('ict-requisition-form', views.ict_requisition_form, name='requisitionform'),
>>>>>>> 5637812568ecbe33409cc8a0b14f52f3fc0d20d4
=======
    path('ict-requisition-form', views.ict_requisition_form, name='requisitionform'),
>>>>>>> 5637812568ecbe33409cc8a0b14f52f3fc0d20d4
    
#Dir & Managers Approvals

    path('requisitionform_more_and_approval/<int:id>', views.requisitionform_more_and_approval, name='requisitionform_more_and_approval'),
    path('insert-requisition-form', views.insertrequisitionform, name='insert-requisition-form'),
    path('ictmanager-more-requisition-form-manager/<int:id>', views.requisitionform_ict_manger_approval, name='ict.manager.approval.requisitionform'),
    
]