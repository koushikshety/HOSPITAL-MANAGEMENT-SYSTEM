# Generated by Django 4.2.11 on 2024-04-19 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_p_id_doctor_d_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='d_id',
        ),
    ]
