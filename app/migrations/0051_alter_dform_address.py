# Generated by Django 4.2.11 on 2024-05-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0050_rename_newdoctorform_dform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dform',
            name='address',
            field=models.TextField(default=''),
        ),
    ]