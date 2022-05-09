from django.shortcuts import render

# Create your views here.

#from re import TEMPLATE
from django.contrib import messages
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from accounts.models import Department, Role
from .models import ICTRequisitionForm 
# Create your views here.




#view / fill/ requisitionform   
@login_required   
def form(request):
    return render(request,"form_index.html")

#add / requisitionform
@login_required   
def insertrequisitionform(request):
    
    if request.method =="POST":
            user=request.user
            department=request.user.department
            start_date=request.POST.get('start_date')
            if not start_date:
                messages.warning(request, 'Field Must Not Be empty!')
                return redirect('ict-requisition-form')
            end_date=request.POST.get('end_date')    
            start_time=request.POST.get('start_time')
            if not start_time:
                messages.warning(request, 'Field Must Not Be empty!')
                return redirect('ict-requisition-form') 
            end_time=request.POST.get('end_time')
            
            service_requested=request.POST.get('service_requested')
            if not service_requested:
                messages.warning(request, 'Field Must Not Be empty!')
                return redirect('ict-requisition-form')  
            other_service=request.POST.get('other_service')
            reason_for_request=request.POST.get('reason_for_request')
            if not reason_for_request:
                messages.warning(request, 'Field Must Not Be empty!')
                return redirect('ict-requisition-form')  
            
            data = ICTRequisitionForm(user=user,department=department,start_date=start_date,end_date=end_date,start_time=start_time,end_time=end_time,service_requested=service_requested,other_service=other_service,reason_for_request=reason_for_request)
            data.save()
        
            messages.success(request, 'Form Submitted Successfully ')
            return redirect("dashboard")  

#ICT Manager Approval
@login_required 
def ict_manager_approval(request, id):
    if request.user.role.roles == "ICT_Manager":    
        data = ICTRequisitionForm.objects.get(id=id)
        
        if request.method == 'POST':
            t = ICTRequisitionForm.objects.get(id=id)
            t.manager_ict_decision = request.POST.get('manager_ict_decision')
            t.manager_ict_comments = request.POST.get('manager_ict_comments')
            t.save() 
            messages.success(request, 'Updated Successfully')
            return redirect("approvals")  

        else:

            return render(request, 'manager_ict/more_and_approval.html', {"data": data})
    else:
        return render(request,"unathorized.html")

#Director DSS Approval        
@login_required  
def dss_director_approval(request, id):
    if request.user.role.roles == "DSS_Director":        
        data = ICTRequisitionForm.objects.get(id=id)
        
        if request.method == 'POST':
            t = ICTRequisitionForm.objects.get(id=id)
            if t.department =='DSS':
                t.resp_dir_decision = request.POST.get('dss_dir_decision')
                t.dss_dir_decision = request.POST.get('dss_dir_decision')
                t.resp_dir_comments = request.POST.get('dss_director_comments')
                t.dss_director_comments = request.POST.get('dss_director_comments')
                t.save()
            else:  
                t.dss_director_comments = request.POST.get('dss_director_comments')
                t.dss_dir_decision = request.POST.get('dss_dir_decision')
                t.save()
            messages.success(request, 'Updated Successfully')
            return redirect("approvals")  

        else:

            return render(request, 'director_dss/more_and_approval.html', {"data": data})
    else:
        return render(request,"unathorized.html")


#Director FRD Approval 
@login_required 
def fmd_director_approval(request, id):
    if request.user.role.roles == "FMD_Director":

        data = ICTRequisitionForm.objects.get(id=id)
        
        if request.method == 'POST':
            t = ICTRequisitionForm.objects.get(id=id)
            t.resp_dir_comments = request.POST.get('resp_dir_comments')
            t.resp_dir_decision = request.POST.get('resp_dir_decision')
            t.save() 
            messages.success(request, 'Updated Successfully')
            return redirect("approvals")  

        else:

            return render(request, 'director_fmd/more_and_approval.html', {"data": data})
    else:
        return render(request,"unathorized.html")

@login_required 
def frd_director_approval(request, id):
    if request.user.role.roles == "FRD_Director":    
        data = ICTRequisitionForm.objects.get(id=id)
        
        if request.method == 'POST':
            t = ICTRequisitionForm.objects.get(id=id)
            t.resp_dir_comments = request.POST.get('resp_dir_comments')
            t.resp_dir_decision = request.POST.get('resp_dir_decision')
            t.save() 
            messages.success(request, 'Updated Successfully')
            return redirect("approvals")  

        else:

            return render(request, 'director_frd/more_and_approval.html', {"data": data})
    else:
        return render(request,"unathorized.html")
        

@login_required 
def gov_approval(request, id):
    if request.user.role.roles == "GOV":    
        data = ICTRequisitionForm.objects.get(id=id)
        
        if request.method == 'POST':
            t = ICTRequisitionForm.objects.get(id=id)
            t.resp_dir_comments = request.POST.get('resp_dir_comments')
            t.resp_dir_decision = request.POST.get('resp_dir_decision')
            t.save() 
            messages.success(request, 'Updated Successfully')
            return redirect("approvals")  

        else:

            return render(request, 'gov/more_and_approval.html', {"data": data})
    else:
        return render(request,"unathorized.html")


@login_required 
def erd_director_approval(request, id):
    if request.user.role.roles == "ERD_Director":   
        data = ICTRequisitionForm.objects.get(id=id)
        
        if request.method == 'POST':
            t = ICTRequisitionForm.objects.get(id=id)
            t.resp_dir_decision = request.POST.get('resp_dir_decision')
            t.resp_dir_comments = request.POST.get('resp_dir_comments')
            t.save() 
            messages.success(request, 'Updated Successfully')
            return redirect("approvals")  

        else:

            return render(request, 'director_erd/more_and_approval.html', {"data": data})

    else:
        return render(request,"unathorized.html")


#view more details
@login_required   
def more(request, id):
   
    data = ICTRequisitionForm.objects.get(id=id)
    return render(request, 'dashboard_more.html', {"data": data})

#user dashboard
@login_required
def userdashboard(request):
    requisitionforms = ICTRequisitionForm.objects.filter(user_id = request.user.id)
    totalrequests = ICTRequisitionForm.objects.filter(user_id = request.user.id).count()  
    return render(request,"dashboard.html",{'requisitionforms':requisitionforms,'totalrequests':totalrequests})


# @login_required
# def requisitionform_ict_manger_approval(request, id):
       
#     data = ICTRequisitionForm.objects.get(id=id)
#     return render(request, 'manager_ict/approval.html', {"data": data})

#Manager
@login_required
def approvals(request):

    if request.user.role.roles == "ICT_Manager":
        requisitionforms = ICTRequisitionForm.objects.filter(resp_dir_decision="Approved",dss_dir_decision="Approved") 
        totalrequests = ICTRequisitionForm.objects.filter(resp_dir_decision="Approved",dss_dir_decision="Approved").count()   
        return render(request,"manager_ict/dashboard.html",{'requisitionforms':requisitionforms,'totalrequests':totalrequests})

    if request.user.role.roles == "DSS_Director":

        requisitionforms = ICTRequisitionForm.objects.filter(department='DSS')
        otherdepartment = ICTRequisitionForm.objects.filter(~Q(department= 'DSS'),resp_dir_decision="Approved")   
        return render(request,"director_dss/dashboard.html",{'requisitionforms':requisitionforms,'otherdepartment':otherdepartment})    
    
    if request.user.role.roles == "FMD_Director":
        requisitionforms = ICTRequisitionForm.objects.filter(department='FMD')
        totalrequests = ICTRequisitionForm.objects.filter(department='FMD').count()   
        return render(request,"director_fmd/dashboard.html",{'requisitionforms':requisitionforms,'totalrequests':totalrequests})
    
    if request.user.role.roles == "GOV":
        requisitionforms = ICTRequisitionForm.objects.filter(department='GOV')
        totalrequests = ICTRequisitionForm.objects.filter(department='GOV').count()   
        return render(request,"gov/dashboard.html",{'requisitionforms':requisitionforms,'totalrequests':totalrequests})
    
    if request.user.role.roles == "ERD_Director":
        requisitionforms = ICTRequisitionForm.objects.filter(department='ERD')
        totalrequests = ICTRequisitionForm.objects.filter(department='ERD').count()   
        return render(request,"director_erd/dashboard.html",{'requisitionforms':requisitionforms,'totalrequests':totalrequests})
    
    if request.user.role.roles == "FRD_Director":
        # depart = Department.object.filter(department='FRD')
        requisitionforms = ICTRequisitionForm.objects.filter(department='FRD')
        totalrequests = ICTRequisitionForm.objects.filter(department='FRD').count()   
        return render(request,"director_frd/dashboard.html",{'requisitionforms':requisitionforms,'totalrequests':totalrequests})
    
    else:
        return render(request,"unathorized.html")
        
