from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Department
from datetime import datetime

# Create your models here.


class AfterHoursForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form_name = models.CharField(max_length=20,
        default='After Hours Form',choices=[('After Hours Form','After Hours Form')]
        )
    department = models.CharField( max_length=6)
    start_date = models.DateField()
    end_date = models.TextField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TextField(null=True,blank=True)
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
    manager_ict_tasks_to_ICT_staffs = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    