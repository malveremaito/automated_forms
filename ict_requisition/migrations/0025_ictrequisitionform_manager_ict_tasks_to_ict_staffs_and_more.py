# Generated by Django 4.0.5 on 2022-07-13 00:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ict_requisition', '0024_alter_ictrequisitionform_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='ictrequisitionform',
            name='manager_ict_tasks_to_ICT_staffs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ictrequisitionform',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 13, 11, 9, 40, 798041)),
        ),
    ]
