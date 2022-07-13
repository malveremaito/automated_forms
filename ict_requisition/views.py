import django
from django.shortcuts import render

# Create your views here.

#from re import TEMPLATE
from django.contrib import messages
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from accounts.models import Department, Role, Unit
from .models import ICTRequisitionForm 
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
django.utils.timezone.now
# Create your views here.


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


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

            
            #Automated Email Send to the user submiting form
            subject = 'ICT Requisition'
            template = render_to_string('email_template.html',{'firstname':request.user.first_name,'lastname':request.user.last_name})
            email_from = settings.DEFAULT_FROM_EMAIL
            recipient = [request.user.email]

            send_mail( subject, template, email_from, recipient,fail_silently=False)
            
          
            # data1 = Role.objects.filter(roles='DSS_Director')
            # dss_dir_email = data1.user.email

            #Automated Email Send to DSS Director for staff requesting in DSS department
            
            if request.user.department.department=='DSS':
                subject1 = 'ICT Requisition'
                template1 = render_to_string('director_dss/email_template.html',{'firstname':request.user.first_name,'lastname':request.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list1 =[]
                for role in Role.objects.filter(roles='DSS_Director'):
                    recipient_list1.append(role.user.email)

                send_mail( subject1, template1, email_from, recipient_list1,fail_silently=False)    
            #Automated Email Send to GOV for staff requesting in GOV department
            if request.user.department.department=='GOV':
                subject2 = 'ICT Requisition'
                template2 = render_to_string('gov/email_template_pending.html',{'firstname':request.user.first_name,'lastname':request.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list2 =[]
                for role in Role.objects.filter(roles='GOV'):
                    recipient_list2.append(role.user.email)

                send_mail( subject2, template2, email_from, recipient_list2,fail_silently=False)      
            #Automated Email Send to FRD for staff requesting in FRD department
            if request.user.department.department=='FRD':
                subject3 = 'ICT Requisition'
                template3 = render_to_string('director_frd/email_template_pending.html',{'firstname':request.user.first_name,'lastname':request.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list3 =[]
                for role in Role.objects.filter(roles='FRD_Director'):
                    recipient_list3.append(role.user.email)

                send_mail( subject3, template3, email_from, recipient_list3,fail_silently=False)       
            #Automated Email Send to ERD Director for staff requesting in ERD department
            if request.user.department.department=='ERD':
                subject4 = 'ICT Requisition'
                template4 = render_to_string('director_erd/email_template_pending.html',{'firstname':request.user.first_name,'lastname':request.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list4 =[]
                for role in Role.objects.filter(roles='ERD_Director'):
                    recipient_list4.append(role.user.email)

                send_mail( subject4, template4, email_from, recipient_list4,fail_silently=False)

            #Automated Email Send to FMD Director for staff requesting in FMD department
            if request.user.department.department=='FMD':
                subject5 = 'ICT Requisition'
                template5 = render_to_string('director_fmd/email_template_pending.html',{'firstname':request.user.first_name,'lastname':request.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list5 =[]
                for role in Role.objects.filter(roles='FMD_Director'):
                    recipient_list5.append(role.user.email)

                send_mail( subject5, template5, email_from, recipient_list5,fail_silently=False)
            
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
            t.manager_ict_tasks_to_ICT_staffs = request.POST.get('manager_ict_tasks_to_ICT_staffs')
            t.save() 

            #if Approved notify the requestor
            if t.manager_ict_decision=='Approved':
                subject = 'ICT Requisition'
                template = render_to_string('manager_ict/email_template_approved.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list =[t.user.email]
                send_mail( subject, template, email_from, recipient_list,fail_silently=False)
            
                #if Approved notify the DSS Director
                subject1 = 'ICT Requisition'
                template1 = render_to_string('manager_ict/email_template_approved_dss.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list1 =[]
                for role in Role.objects.filter(roles='DSS_Director'):
                    recipient_list1.append(role.user.email)
                send_mail( subject1, template1, email_from, recipient_list1,fail_silently=False)

                #Notify ICT Team about the requisition when it has been approved

                # subject6 = 'ICT Requisition'
                # template6 = render_to_string('manager_ict/email_template_approved_ict.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list6 =[]
                # for unit in Unit.objects.filter(unit='ICT_Unit'):
                #     recipient_list6.append(unit.user.email)

                # send_mail( subject6, template6, email_from, recipient_list6,fail_silently=False)

                #Notify GOV Director about the status of the ICT requisition form a staff in his department has request.
                if t.department=='GOV':
                    subject2 = 'ICT Requisition'
                    template2 = render_to_string('manager_ict/email_template_approved_gov.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list2 =[]
                    for role in Role.objects.filter(roles='GOV'):
                        recipient_list2.append(role.user.email)
                    send_mail( subject2, template2, email_from, recipient_list2,fail_silently=False)
                              
                #Notify FRD Director about the status of the ICT requisition form a staff in his department has request.
                if t.department=='FRD':
                    subject3 = 'ICT Requisition'
                    template3 = render_to_string('manager_ict/email_template_approved_frd.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list3 =[]
                    for role in Role.objects.filter(roles='FRD_Director'):
                        recipient_list3.append(role.user.email)
                    send_mail( subject3, template3, email_from, recipient_list3,fail_silently=False)
                #Notify FMD Director about the status of the ICT requisition form a staff in his department has request.
                if t.department=='FMD':
                    subject4 = 'ICT Requisition'
                    template4 = render_to_string('manager_ict/email_template_approved_fmd.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list4 =[]
                    for role in Role.objects.filter(roles='FMD_Director'):
                        recipient_list4.append(role.user.email)
                    send_mail( subject4, template4, email_from, recipient_list4,fail_silently=False)
                #Notify ERD Director about the status of the ICT requisition form a staff in his department has request.
                if t.department=='ERD':
                    subject5 = 'ICT Requisition'
                    template5 = render_to_string('manager_ict/email_template_approved_erd.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list5 =[]
                    for role in Role.objects.filter(roles='ERD_Director'):
                        recipient_list5.append(role.user.email)
                    send_mail( subject5, template5, email_from, recipient_list5,fail_silently=False)
                

            if t.manager_ict_decision=='Disapproved':
                subject = 'ICT Requisition'
                template = render_to_string('manager_ict/email_template_disapproved.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list =[t.user.email]
                send_mail( subject, template, email_from, recipient_list,fail_silently=False)

                subject1 = 'ICT Requisition'
                template1 = render_to_string('manager_ict/email_template_disapproved_dss.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list1 =[]
                for role in Role.objects.filter(roles='DSS_Director'):
                    recipient_list1.append(role.user.email)
                send_mail( subject1, template1, email_from, recipient_list1,fail_silently=False)

                if t.department=='GOV':
                    subject2 = 'ICT Requisition'
                    template2 = render_to_string('manager_ict/email_template_disapproved_gov.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list2 =[]
                    for role in Role.objects.filter(roles='GOV'):
                        recipient_list2.append(role.user.email)
                    send_mail( subject2, template2, email_from, recipient_list2,fail_silently=False)
                
                #Notify FRD Director about the status of the ICT requisition form a staff in his department has request.
                if t.department=='FRD':
                    subject3 = 'ICT Requisition'
                    template3 = render_to_string('manager_ict/email_template_disapproved_frd.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list3 =[]
                    for role in Role.objects.filter(roles='FRD_Director'):
                        recipient_list3.append(role.user.email)
                    send_mail( subject3, template3, email_from, recipient_list3,fail_silently=False)
                
                if t.department=='FMD':
                    subject4 = 'ICT Requisition'
                    template4 = render_to_string('manager_ict/email_template_disapproved_fmd.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list4 =[]
                    for role in Role.objects.filter(roles='FMD_Director'):
                        recipient_list4.append(role.user.email)
                    send_mail( subject4, template4, email_from, recipient_list4,fail_silently=False)

                if t.department=='ERD':
                    subject5 = 'ICT Requisition'
                    template5 = render_to_string('manager_ict/email_template_disapproved_erd.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list5 =[]
                    for role in Role.objects.filter(roles='ERD_Director'):
                        recipient_list5.append(role.user.email)
                    send_mail( subject5, template5, email_from, recipient_list5,fail_silently=False)
                    
                    
            messages.success(request, 'Updated Successfully')
            return redirect("authorization")     

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
            
            if t.dss_dir_decision=='Approved':
                subject = 'ICT Requisition'
                template = render_to_string('director_dss/email_template_approved.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list =[t.user.email]
                send_mail( subject, template, email_from, recipient_list,fail_silently=False)

            #Email sent to notify ict manager about that dss director has approved a requisition form and pending ict manager approval

                subject1 = 'ICT Requisition'
                template1 = render_to_string('manager_ict/email_template_pending.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list1 =[]
                for role in Role.objects.filter(roles='ICT_Manager'):
                    recipient_list1.append(role.user.email)

                send_mail( subject1, template1, email_from, recipient_list1,fail_silently=False)

                #Notify Governor / DG about the status of the ICT requisition form a staff in his department has request.
                if t.department=='GOV':
                    subject2 = 'ICT Requisition'
                    template2 = render_to_string('director_dss/email_template_approved_gov.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list2 =[]
                    for role in Role.objects.filter(roles='GOV'):
                        recipient_list2.append(role.user.email)
                    send_mail( subject2, template2, email_from, recipient_list2,fail_silently=False)
                
                #Notify FRD Director about the status of the ICT requisition form a staff in his department has request.
                if t.department=='FRD':
                    subject3 = 'ICT Requisition'
                    template3 = render_to_string('director_dss/email_template_approved_frd.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list3 =[]
                    for role in Role.objects.filter(roles='FRD_Director'):
                        recipient_list3.append(role.user.email)
                    send_mail( subject3, template3, email_from, recipient_list3,fail_silently=False)
                
                if t.department=='FMD':
                    subject4 = 'ICT Requisition'
                    template4 = render_to_string('director_dss/email_template_approved_fmd.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list4 =[]
                    for role in Role.objects.filter(roles='FMD_Director'):
                        recipient_list4.append(role.user.email)
                    send_mail( subject4, template4, email_from, recipient_list4,fail_silently=False)

                if t.department=='ERD':
                    subject5 = 'ICT Requisition'
                    template5 = render_to_string('director_dss/email_template_approved_erd.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list5 =[]
                    for role in Role.objects.filter(roles='ERD_Director'):
                        recipient_list5.append(role.user.email)
                    send_mail( subject5, template5, email_from, recipient_list5,fail_silently=False)
                

            if t.dss_dir_decision=='Disapproved':
                subject = 'ICT Requisition'
                template = render_to_string('director_dss/email_template_disapproved.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list =[t.user.email]
                send_mail( subject, template, email_from, recipient_list,fail_silently=False)

                
                #Notify Governor / DG about the status of the ICT requisition form a staff in his department has request.
                if t.department=='GOV':
                    subject2 = 'ICT Requisition'
                    template2 = render_to_string('director_dss/email_template_disapproved_gov.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list2 =[]
                    for role in Role.objects.filter(roles='GOV'):
                        recipient_list2.append(role.user.email)
                    send_mail( subject2, template2, email_from, recipient_list2,fail_silently=False)
                
                #Notify FRD Director about the status of the ICT requisition form a staff in his department has request.
                if t.department=='FRD':
                    subject3 = 'ICT Requisition'
                    template3 = render_to_string('director_dss/email_template_disapproved_frd.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list3 =[]
                    for role in Role.objects.filter(roles='FRD_Director'):
                        recipient_list3.append(role.user.email)
                    send_mail( subject3, template3, email_from, recipient_list3,fail_silently=False)
                
                if t.department=='FMD':
                    subject4 = 'ICT Requisition'
                    template4 = render_to_string('director_dss/email_template_disapproved_fmd.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list4 =[]
                    for role in Role.objects.filter(roles='FMD_Director'):
                        recipient_list4.append(role.user.email)
                    send_mail( subject4, template4, email_from, recipient_list4,fail_silently=False)

                if t.department=='ERD':
                    subject5 = 'ICT Requisition'
                    template5 = render_to_string('director_dss/email_template_disapproved_erd.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list5 =[]
                    for role in Role.objects.filter(roles='ERD_Director'):
                        recipient_list5.append(role.user.email)
                    send_mail( subject5, template5, email_from, recipient_list5,fail_silently=False)
                

            messages.success(request, 'Updated Successfully')
            return redirect("authorization")  

        else:

            return render(request, 'director_dss/more_and_approval.html', {"data": data})
    else:
        return render(request,"unathorized.html")


#Director FRD Approval 
@login_required 
def fmd_director_approval(request, id):
    if request.user.role.roles == "FMD_Director":

        data = ICTRequisitionForm.objects.get(id=id)
        t = ICTRequisitionForm.objects.get(id=id)
        if request.method == 'POST':
           
            t.resp_dir_comments = request.POST.get('resp_dir_comments')
            t.resp_dir_decision = request.POST.get('resp_dir_decision')
            t.save() 

            #Approved sent mail to the requestor
            if t.resp_dir_decision=='Approved':
                subject = 'ICT Requisition'
                template = render_to_string('director_fmd/email_template_approved.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list =[t.user.email]
                send_mail( subject, template, email_from, recipient_list,fail_silently=False)

            #Notify DSS Director about the new ICT Requisition Form Approved by FMD Director

                subject1 = 'ICT Requisition'
                template1 = render_to_string('director_dss/email_template_pending.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list1 =[]
                for role in Role.objects.filter(roles='DSS_Director'):
                    recipient_list1.append(role.user.email)

                send_mail( subject1, template1, email_from, recipient_list1,fail_silently=False)
           
           

            #Disapproved sent mail to the requestor
            if t.resp_dir_decision=='Disapproved':
                subject = 'ICT Requisition'
                template = render_to_string('director_fmd/email_template_disapproved.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list =[t.user.email]

                send_mail( subject, template, email_from, recipient_list,fail_silently=False)
            messages.success(request, 'Updated Successfully') 
            return redirect("authorization") 
           
        else:

            return render(request, 'director_fmd/more_and_approval.html', {"data": data,'t':t})
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

            #Approved sent mail to the requestor
            if t.resp_dir_decision=='Approved':
                subject = 'ICT Requisition'
                template = render_to_string('director_frd/email_template_approved.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list =[t.user.email]
                send_mail( subject, template, email_from, recipient_list,fail_silently=False)

            #Notify DSS Director about the new ICT Requisition Form Approved by FRD Director

                subject1 = 'ICT Requisition'
                template1 = render_to_string('director_dss/email_template_pending.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list1 =[]
                for role in Role.objects.filter(roles='DSS_Director'):
                    recipient_list1.append(role.user.email)

                send_mail( subject1, template1, email_from, recipient_list1,fail_silently=False)
            
            #Disapproved sent mail to the requestor
            if t.resp_dir_decision=='Disapproved':
                subject = 'ICT Requisition'
                template = render_to_string('director_frd/email_template_disapproved.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list =[t.user.email]

                send_mail( subject, template, email_from, recipient_list,fail_silently=False)
            messages.success(request, 'Updated Successfully')
            return redirect("authorization")  

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
            
            #Approved sent mail to the requestor
            if t.resp_dir_decision=='Approved':
                subject = 'ICT Requisition'
                template = render_to_string('gov/email_template_approved.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list =[t.user.email]
                send_mail( subject, template, email_from, recipient_list,fail_silently=False)

            #Notify DSS Director about the new ICT Requisition Form Approved by the Gov or DG

                subject = 'ICT Requisition'
                template = render_to_string('director_dss/email_template_pending.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list1 =[]
                for role in Role.objects.filter(roles='DSS_Director'):
                    recipient_list1.append(role.user.email)

                send_mail( subject, template, email_from, recipient_list1,fail_silently=False)
            
            #Disapproved sent mail to the requestor
            if t.resp_dir_decision=='Disapproved':
                subject = 'ICT Requisition'
                template = render_to_string('gov/email_template_disapproved.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list =[t.user.email]

                send_mail( subject, template, email_from, recipient_list,fail_silently=False)

            messages.success(request, 'Updated Successfully')
            return redirect("authorization")  

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
           

            #Approved sent mail to the requestor
            if t.resp_dir_decision=='Approved':
                subject = 'ICT Requisition'
                template = render_to_string('director_erd/email_template_approved.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list =[t.user.email]
                send_mail( subject, template, email_from, recipient_list,fail_silently=False)

            #Notify DSS Director about the new ICT Requisition Form Approved by the Gov or DG

                subject = 'ICT Requisition'
                template = render_to_string('director_dss/email_template_pending.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list1 =[]
                for role in Role.objects.filter(roles='DSS_Director'):
                    recipient_list1.append(role.user.email)

                send_mail( subject, template, email_from, recipient_list1,fail_silently=False)
            
            #Disapproved sent mail to the requestor
            if t.resp_dir_decision=='Disapproved':
                subject = 'ICT Requisition'
                template = render_to_string('director_erd/email_template_disapproved.html',{'firstname':t.user.first_name,'lastname':t.user.last_name})
                email_from = settings.EMAIL_HOST_USER
                recipient_list =[t.user.email]

                send_mail( subject, template, email_from, recipient_list,fail_silently=False)
            
            messages.success(request, 'Updated Successfully')
            return redirect("authorization")  
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
    
    pendingrequests = (ICTRequisitionForm.objects.filter (user_id = request.user.id,resp_dir_decision="Pending") | ICTRequisitionForm.objects.filter (user_id = request.user.id,resp_dir_decision="Approved",dss_dir_decision="Pending") 
        | ICTRequisitionForm.objects.filter (user_id = request.user.id,resp_dir_decision="Approved",dss_dir_decision="Approved",manager_ict_decision="Pending")).count() 
   
    approvedrequest = ICTRequisitionForm.objects.filter(user_id = request.user.id,resp_dir_decision="Approved",dss_dir_decision="Approved",manager_ict_decision="Approved").count() 
   
    disapprovedrequest = (ICTRequisitionForm.objects.filter (user_id = request.user.id,resp_dir_decision="Disapproved") | ICTRequisitionForm.objects.filter (user_id = request.user.id,dss_dir_decision="Disapproved")
    | ICTRequisitionForm.objects.filter (user_id = request.user.id,manager_ict_decision ="Disapproved")).count() 


    return render(request,"dashboard.html",{'requisitionforms':requisitionforms,'totalrequests':totalrequests,'approvedrequest':approvedrequest,'pendingrequests':pendingrequests,'disapprovedrequest':disapprovedrequest})


# @login_required
# def requisitionform_ict_manger_approval(request, id):
       
#     data = ICTRequisitionForm.objects.get(id=id)
#     return render(request, 'manager_ict/approval.html', {"data": data})

#Manager
@login_required
def authorization(request):

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

@login_required   
def more_authorization_pdf(request,id):
   
    data = ICTRequisitionForm.objects.get(id=id)
    
    return render(request, 'manager_ict/pdfview.html', {"data": data})


@login_required   
def more_approved_pdf(request,id):
   
    data = ICTRequisitionForm.objects.get(id=id)
    
    return render(request, 'staff_ict/pdfview.html', {"data": data})
 

        
@login_required
def more_user_pdf(request,id):
   
    data = ICTRequisitionForm.objects.get(id=id)
    
    return render(request, 'pdfview.html', {"data": data})
  


@login_required
def approved(request):

    if request.user.unit.unit == "ICT_Unit":
        requisitionforms = ICTRequisitionForm.objects.filter(resp_dir_decision="Approved",dss_dir_decision="Approved",manager_ict_decision="Approved") 
        return render(request,"staff_ict/dashboard.html",{'requisitionforms':requisitionforms})
    
    else:
        return render(request,"unathorized.html")
