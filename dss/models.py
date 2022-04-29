from django.db import models
from django.contrib.auth.models import User
from accounts.models import Department
from datetime import datetime 
# Create your models here.

class form(models.Model):
    form_name = models.TextField()
    form_description = models.TextField()
    link = models.TextField()


class ICTRequisitionForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form_name = models.CharField(max_length=20,
        default='ICT Requisition Form',choices=[('ICT_Requisition_Form','ICT Requisition Form')]
        )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TextField(null=True, blank=True)
    service_requested = models.TextField()
    other_service = models.TextField(blank=True)
    reason_for_request = models.TextField()
    resp_dir_decision= models.CharField(
        max_length=11,
        default='Pending',
        choices=[('Approved','Approved'),('Disapproved','Disapproved'),('Pending','Pending')]
    )
    resp_dir_comments = models.TextField(null=True, blank=True)
    dss_dir_decision = models.CharField(
            max_length=11,
            default='Pending',
            choices=[('Approved','Approved'),('Disapproved','Disapproved'),('Pending','Pending')])
    dss_director_comments = models.TextField(null=True, blank=True)
    manager_ict_decision = models.CharField(
            max_length=11,
            default='Pending',
            choices=[('Approved','Approved'),('Disapproved','Disapproved'),('Pending','Pending')])
    manager_ict_comments = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    
    
    
def get_first_name(self):
    return self.first_name + " " + self.last_name
User.add_to_class("__str__", get_first_name)

def get_department_name(self):
    return self.department

Department.add_to_class("__str__", get_department_name)

