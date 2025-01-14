# Generated by Django 4.2.11 on 2024-04-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_doctor_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='APPOINT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('doctor_name', models.CharField(max_length=100)),
                ('appointment_date', models.CharField(max_length=100)),
                ('time_slot', models.CharField(max_length=100)),
                ('token_number', models.CharField(max_length=100)),
                ('problem', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='role',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='role',
        ),
    ]
