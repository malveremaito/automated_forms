# Generated by Django 4.0.4 on 2022-04-27 00:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ict', '0005_alter_requisitionform_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisitionform',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 11, 51, 20, 749505)),
        ),
        migrations.AlterField(
            model_name='requisitionform',
            name='end_time',
            field=models.CharField(blank=True, default='None', max_length=20, null=True),
        ),
    ]