# Generated by Django 5.0.4 on 2024-04-17 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_password_change',
        ),
    ]
