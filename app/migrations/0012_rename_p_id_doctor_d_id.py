# Generated by Django 4.2.11 on 2024-04-19 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_doctor_p_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='p_id',
            new_name='d_id',
        ),
    ]