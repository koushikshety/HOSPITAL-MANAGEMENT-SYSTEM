# Generated by Django 4.2.11 on 2024-05-09 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_payment_phone_payment_srvice_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='phone',
            new_name='phone1',
        ),
    ]