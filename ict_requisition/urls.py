from django.urls import path
from . import views

urlpatterns = [
#dashboard view
    path('dashboard', views.userdashboard, name='dashboard'),
    path('authorization', views.authorization, name='authorization'),
    path('approved', views.approved, name='approved'),
    
    path('more-user-pdf/<int:id>', views.more_user_pdf, name='more-user-pdf'),
    path('more/<int:id>', views.more, name='more'),


#Form
    path('form', views.form, name='ict-requisition-form'),
    path('insert-requisition-form', views.insertrequisitionform, name='insert-requisition-form'),
    
    # path('ictmanager-more-requisition-form-manager/<int:id>', views.requisitionform_ict_manger_approval, name='ict.manager.approval.requisitionform'),

#Dir & Managers Approvals

#ICT Manager Approval#
#####################################################################################################
    path('ict-manager-approval/<int:id>', views.ict_manager_approval, name='ict-manager-approval'),

    #PDF View
#####################################################################################################  
    path('more-authorization-pdf/<int:id>', views.more_authorization_pdf, name='more-authorization-pdf'),
    path('more-approved-pdf/<int:id>', views.more_approved_pdf, name='more-approved-pdf'),

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


    
]