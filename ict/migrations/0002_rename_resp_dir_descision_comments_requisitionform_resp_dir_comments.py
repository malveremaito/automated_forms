# Generated by Django 4.0.2 on 2022-04-16 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ict', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requisitionform',
            old_name='resp_dir_descision_comments',
            new_name='resp_dir_comments',
        ),
    ]
