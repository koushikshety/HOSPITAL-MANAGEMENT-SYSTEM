# Generated by Django 4.2.11 on 2024-05-17 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0060_alter_patient_addmission_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='addmission_date',
        ),
    ]
