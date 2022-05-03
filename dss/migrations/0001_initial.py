# Generated by Django 4.0.4 on 2022-05-03 02:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.TextField()),
                ('form_description', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ICTRequisitionForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_name', models.CharField(choices=[('ICT_Requisition_Form', 'ICT Requisition Form')], default='ICT Requisition Form', max_length=20)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TextField(blank=True, null=True)),
                ('service_requested', models.TextField()),
                ('other_service', models.TextField(blank=True)),
                ('reason_for_request', models.TextField()),
                ('resp_dir_decision', models.CharField(choices=[('Approved', 'Approved'), ('Disapproved', 'Disapproved'), ('Pending', 'Pending')], default='Pending', max_length=11)),
                ('resp_dir_comments', models.TextField(blank=True, null=True)),
                ('dss_dir_decision', models.CharField(choices=[('Approved', 'Approved'), ('Disapproved', 'Disapproved'), ('Pending', 'Pending')], default='Pending', max_length=11)),
                ('dss_director_comments', models.TextField(blank=True, null=True)),
                ('manager_ict_decision', models.CharField(choices=[('Approved', 'Approved'), ('Disapproved', 'Disapproved'), ('Pending', 'Pending')], default='Pending', max_length=11)),
                ('manager_ict_comments', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 5, 3, 13, 25, 15, 67832))),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
