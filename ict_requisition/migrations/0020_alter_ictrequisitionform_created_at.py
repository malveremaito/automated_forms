# Generated by Django 4.0.4 on 2022-05-16 06:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ict_requisition', '0019_alter_ictrequisitionform_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ictrequisitionform',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 16, 17, 4, 34, 354443)),
        ),
    ]
