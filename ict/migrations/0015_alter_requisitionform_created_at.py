# Generated by Django 4.0.4 on 2022-04-27 23:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ict', '0014_alter_requisitionform_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisitionform',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 28, 10, 31, 23, 224764)),
        ),
    ]
