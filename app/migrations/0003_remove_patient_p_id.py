# Generated by Django 5.0.4 on 2024-04-16 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_patient_p_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='p_id',
        ),
    ]