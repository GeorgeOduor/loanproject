# Generated by Django 4.2.3 on 2023-11-18 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_rename_nationa_id_profile_national_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, choices=[('borrower', 'Borrower'), ('lender', 'Lender'), ('admin', 'Admin')], max_length=50, null=True)),
                ('type', models.CharField(blank=True, choices=[('loan_disbursement', 'Loan Disbursement'), ('loan_repayment', 'Loan Repayment'), ('loan_request', 'Loan Request'), ('complaint', 'Complaint'), ('message', 'Message'), ('other', 'Other')], max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]