# Generated by Django 4.2.3 on 2023-08-18 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_alter_loanproduct_interest_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowerprofile',
            name='alternative_mobile_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='borrowerprofile',
            name='referer_mobile_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
