# Generated by Django 4.2.3 on 2023-09-17 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lenders', '0016_lenderprofile_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='BorrowerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alternative_mobile_number', models.CharField(blank=True, max_length=12, null=True)),
                ('referer_mobile_number', models.CharField(blank=True, max_length=12, null=True)),
                ('employment_status', models.CharField(blank=True, choices=[('Employed', 'Employed'), ('Unemployed', 'Unemployed'), ('Self Employed', 'Self Employed'), ('Student', 'Student'), ('Retired', 'Retired'), ('Other', 'Other')], max_length=50, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('Married', 'Married'), ('Single', 'Single')], max_length=50, null=True)),
                ('education', models.CharField(blank=True, choices=[('Primary School', 'Primary School'), ('Secondary School', 'Secondary School'), ('University', 'University'), ('Other', 'Other')], max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('interest_rate', models.IntegerField(blank=True, null=True)),
                ('min_loan_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('max_loan_amount', models.CharField(blank=True, max_length=50, null=True)),
                ('min_duration', models.CharField(blank=True, max_length=50, null=True)),
                ('lender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenders.lenderprofile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Borrower Profile',
                'verbose_name_plural': 'Borrower Profile',
            },
        ),
    ]
