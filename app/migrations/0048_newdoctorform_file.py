# Generated by Django 4.2.11 on 2024-05-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_newdoctorform_address_newdoctorform_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newdoctorform',
            name='file',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]