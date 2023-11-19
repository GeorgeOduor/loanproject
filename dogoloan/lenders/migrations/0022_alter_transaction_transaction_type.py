# Generated by Django 4.2.3 on 2023-11-18 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenders', '0021_alter_transaction_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('Loan Disbursement', 'Loan Disbursement'), ('Interest Charges', 'Interest Charges'), ('Excise Duty', 'Excise Duty'), ('Loan Repayment', 'Loan Repayment')], max_length=20),
        ),
    ]
