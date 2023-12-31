# Generated by Django 4.2.3 on 2023-11-01 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lenders', '0017_remove_loanapplications_loan_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trx_type', models.CharField(choices=[('DR', 'Debit'), ('CR', 'Credit')], max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trx_date', models.DateTimeField(auto_now_add=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenders.lenderprofile')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lenders.loanproduct')),
            ],
        ),
    ]
