# Generated by Django 4.2.11 on 2024-05-09 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_rename_phone_payment_phone1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='phone1',
        ),
        migrations.AddField(
            model_name='payment',
            name='phone',
            field=models.CharField(default=9876543210, max_length=100),
            preserve_default=False,
        ),
    ]