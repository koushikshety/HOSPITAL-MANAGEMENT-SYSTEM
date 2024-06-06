# Generated by Django 4.2.11 on 2024-04-19 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_patient_p_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_Name', models.CharField(max_length=100)),
                ('date_of_birth', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('doctor_details', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('p_id', models.CharField(max_length=100)),
            ],
        ),
    ]
