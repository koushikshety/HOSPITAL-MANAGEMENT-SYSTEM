# Generated by Django 4.2.11 on 2024-05-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_boss_name', models.CharField(max_length=100)),
                ('boss_photo', models.ImageField(blank=True, upload_to='boss_photos/')),
                ('company_name', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=200)),
                ('services_offered', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('contract_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contract_period', models.CharField(max_length=100)),
                ('our_profit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('client_name', models.CharField(max_length=100)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_phone', models.CharField(max_length=15)),
            ],
        ),
    ]
