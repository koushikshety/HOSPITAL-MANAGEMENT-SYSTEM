# Generated by Django 4.2.11 on 2024-05-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_alter_doctor_age_alter_doctor_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='p_add',
            field=models.CharField(default='None', max_length=100),
            preserve_default=False,
        ),
    ]
