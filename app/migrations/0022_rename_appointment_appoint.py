# Generated by Django 4.2.11 on 2024-04-20 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_appointment_a_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Appointment',
            new_name='Appoint',
        ),
    ]