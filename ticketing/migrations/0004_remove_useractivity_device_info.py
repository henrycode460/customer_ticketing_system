# Generated by Django 3.2.6 on 2023-08-06 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0003_useractivity_device_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivity',
            name='device_info',
        ),
    ]
