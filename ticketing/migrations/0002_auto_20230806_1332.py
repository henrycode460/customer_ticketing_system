# Generated by Django 3.2.6 on 2023-08-06 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivity',
            name='device_info',
        ),
        migrations.RemoveField(
            model_name='useractivity',
            name='user_agent_string',
        ),
    ]
