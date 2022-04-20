from django.db import models
from django.contrib.auth.models import User
from accounts.models import Department
import datetime
# Create your models here.

class RequisitionForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form_name = models.CharField(max_length=20,
        default='Requisition Form',choices=[('Requisition Form','Requisition Form')]
        )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateTimeField()
    service_requested = models.TextField()
    other_service = models.TextField(null=True, blank=True)
    reason_for_request = models.TextField()
    resp_dir_descision= models.CharField(
        max_length=11,
        default='Pending',
        choices=[('Approved','Approved'),('Disapproved','Disapproved'),('Pending','Pending')]
    )
    resp_dir_comments = models.TextField(null=True, blank=True)
    dss_director_descision = models.CharField(
            max_length=11,
            default='Pending',
            choices=[('Approved','Approved'),('Disapproved','Disapproved'),('Pending','Pending')])
    dss_director_comments = models.TextField(null=True, blank=True)
    mangaer_ict_descision = models.CharField(
            max_length=11,
            default='Pending',
            choices=[('Approved','Approved'),('Disapproved','Disapproved'),('Pending','Pending')])
    mangaer_ict_comments = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
def get_first_name(self):
    return self.first_name + " " + self.last_name
User.add_to_class("__str__", get_first_name)

def get_department_name(self):
    return self.department

Department.add_to_class("__str__", get_department_name)
