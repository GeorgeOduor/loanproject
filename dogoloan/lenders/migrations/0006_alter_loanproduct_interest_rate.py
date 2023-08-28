# Generated by Django 4.2.3 on 2023-08-27 18:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenders', '0005_loanproduct_created_on_loanproduct_modified_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanproduct',
            name='interest_rate',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
