from django.forms import ModelForm
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django import forms


# Create your models here.

class Department(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(
        max_length=6,
        choices=[('GOV','GOV'),('DSS','DSS'),('FRD','FRD'),('FMD','FMD'),('ERD','ERD')]
    )
    
def __str__(self):
    return self.user.username


    
    