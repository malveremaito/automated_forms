from django.db import models

# Create your models here.

class form(models.Model):
    form_name = models.TextField()
    form_description = models.TextField()
    link = models.TextField()
