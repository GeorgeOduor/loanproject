# Generated by Django 4.2.3 on 2023-09-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenders', '0007_loanproduct_penalties'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanproduct',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=50, null=True),
        ),
    ]