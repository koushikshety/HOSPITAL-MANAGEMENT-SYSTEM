# Generated by Django 4.2.11 on 2024-04-21 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_rename_p_id_appoint_pa_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appoint',
            old_name='doctor_name',
            new_name='d_name',
        ),
        migrations.RenameField(
            model_name='appoint',
            old_name='patient_name',
            new_name='p_name',
        ),
    ]
