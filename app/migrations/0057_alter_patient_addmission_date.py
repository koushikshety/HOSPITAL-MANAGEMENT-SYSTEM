# Generated by Django 4.2.11 on 2024-05-17 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0056_patient_addmission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='addmission_date',
            field=models.CharField(max_length=100),
        ),
    ]