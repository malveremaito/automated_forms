# Generated by Django 4.0.4 on 2022-04-27 01:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ict', '0010_alter_requisitionform_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisitionform',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 12, 14, 48, 675776)),
        ),
    ]