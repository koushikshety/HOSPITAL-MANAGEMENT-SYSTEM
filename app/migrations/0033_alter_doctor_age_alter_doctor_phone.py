# Generated by Django 4.2.11 on 2024-04-30 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_doctor_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
