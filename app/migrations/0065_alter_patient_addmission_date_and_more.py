# Generated by Django 4.2.11 on 2024-05-17 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0064_alter_payment_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='addmission_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
