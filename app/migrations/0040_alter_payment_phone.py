# Generated by Django 4.2.11 on 2024-05-09 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_remove_payment_phone1_payment_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
