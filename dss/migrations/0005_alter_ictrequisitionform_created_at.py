# Generated by Django 4.0.4 on 2022-05-03 02:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss', '0004_alter_ictrequisitionform_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ictrequisitionform',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 3, 13, 27, 38, 572556)),
        ),
    ]