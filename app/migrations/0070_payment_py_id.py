# Generated by Django 4.2.11 on 2024-05-18 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0069_remove_doctor_address_remove_doctor_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='py_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]