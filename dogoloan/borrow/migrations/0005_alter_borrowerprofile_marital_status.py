# Generated by Django 4.2.3 on 2023-09-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrow', '0004_alter_borrowerprofile_employment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowerprofile',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('married', 'Married'), ('single', 'Single'), ('divorced', 'Divorced'), ('widowed', 'Widowed'), ('other', 'Other')], max_length=50, null=True),
        ),
    ]
