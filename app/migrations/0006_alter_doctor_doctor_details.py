# Generated by Django 4.2.11 on 2024-04-19 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_details',
            field=models.TextField(),
        ),
    ]