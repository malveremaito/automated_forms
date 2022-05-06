from django.urls import path
from . import views

urlpatterns = [
#Users
    path('forms', views.forms, name='forms'),
    path('dashboard', views.userdashboard, name='dashboard'),
    path('approvals', views.approvals, name='approvals'),
    
    path('more/<int:id>', views.more, name='more'),


#Forms


    path('ictrequisitionform', views.ict_requisition_form, name='requisitionform'),



#Dir & Managers Approvals

#ICT Manager Approval#
#####################################################################################################
    path('ict-manager-approval/<int:id>', views.ict_manager_approval, name='ict-manager-approval'),
#####################################################################################################  

#DSS Director Approval#
#####################################################################################################
    path('dss-director-approval/<int:id>', views.dss_director_approval, name='dss-director-approval'),
#####################################################################################################

#FMD Director Approval#
#####################################################################################################
    path('fmd-director-approval/<int:id>', views.fmd_director_approval, name='fmd-director-approval'),
#####################################################################################################

#FRD Director Approval#
#####################################################################################################
    path('frd-director-approval/<int:id>', views.frd_director_approval, name='frd-director-approval'),
#####################################################################################################

#GOV Approval#
#####################################################################################################
    path('gov-approval/<int:id>', views.gov_approval, name='gov-approval'),
#####################################################################################################

#ERD Director Approval#
#####################################################################################################
    path('erd-director-approval/<int:id>', views.erd_director_approval, name='erd-director-approval'),
#####################################################################################################
    
    path('insert-requisition-form', views.insertrequisitionform, name='insert-requisition-form'),
    path('ictmanager-more-requisition-form-manager/<int:id>', views.requisitionform_ict_manger_approval, name='ict.manager.approval.requisitionform'),
    
]