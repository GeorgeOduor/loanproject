# Generated by Django 4.2.3 on 2023-08-21 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_profile_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='monthly_income',
        ),
    ]
