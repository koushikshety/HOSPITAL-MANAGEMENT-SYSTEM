# Generated by Django 5.0.4 on 2024-04-20 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_delete_appoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='role',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
