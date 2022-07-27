from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Department
from datetime import datetime

# Create your models here.


class AfterHoursForm(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Form_name = models.CharField(max_length=20,
        default='After Hours Form',choices=[('After Hours Form','After Hours Form')]
        )
    Department = models.CharField( max_length=6)
    Unit_OR_Section = models.TextField(null=True,blank=True)
    Purpose = models.TextField(null=True,blank=True)
    Purpose_Reason = models.TextField(null=True,blank=True)
    IT_Services = models.TextField()
    Start_date = models.DateField()
    End_date = models.TextField()
    Start_time = models.TimeField()
    End_time = models.TextField()
    reason_for_request = models.TextField()
    Access_and_Network_Decission= models.CharField(
        max_length=11,
        default='Pending',
        choices=[('Approved','Approved'),('Disapproved','Disapproved'),('Pending','Pending')]
    )
    resp_dir_decision= models.CharField(
        max_length=11,
        default='Pending',
        choices=[('Approved','Approved'),('Disapproved','Disapproved'),('Pending','Pending')]
    )
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
    manager_ict_tasks_to_ICT_staffs = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    