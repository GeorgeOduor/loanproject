from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

from django.db import models
from users.models import User
from scripts.automations import TransactionManager


class LenderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # lender profile
    lending_mobile_no = models.CharField(max_length=12, null=True, blank=True)
    paybillno         = models.CharField(max_length=50, null=True, blank=True)
    brand             = models.CharField(max_length=50, null=True, blank=True)
    # addres details
    zip_code          = models.CharField(max_length=50, null=True, blank=True)
    county            = models.CharField(max_length=50, null=True, blank=True)
    country           = models.CharField(max_length=50, null=True, blank=True,default="Kenya")
    # # account details
    # account_name      = models.CharField(max_length=50, null=True, blank=True)
    # account_number    = models.CharField(max_length=50, null=True, blank=True)
    # bank_name         = models.CharField(max_length=50, null=True, blank=True)
    # lending preferences
    industry          = models.CharField(max_length=50, null=True, blank=True)
    date_created      = models.DateField(auto_now_add=True)
    lending_as        = models.CharField(max_length=50, null=True, blank=True)
    # lender status
    status            = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ],default='Inactive')
    

    def __str__(self):
        return self.brand
    class Meta:
        verbose_name = 'Lender Profile'
        verbose_name_plural = 'Lender Profile'

class Agents(models.Model):
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE)
    agent_location = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.agent_location

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'

class LoanProduct(models.Model):
    lender              = models.ForeignKey(LenderProfile, on_delete=models.CASCADE)
    name                = models.CharField(max_length=50, null=True, blank=True,unique=True)
    interest_rate       = models.IntegerField( null=True, blank=True,validators=[MinValueValidator(1),MaxValueValidator(100)])
    penalties           = models.IntegerField( null=True, blank=True,validators=[MinValueValidator(1),MaxValueValidator(100)])
    min_loan_amount     = models.CharField(max_length=50, null=True, blank=True)
    max_loan_amount     = models.CharField(max_length=50, null=True, blank=True)
    repayment_term      = models.CharField(max_length=50, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True,max_length=1000)
    status              = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ],default='Active')
    created_on          = models.DateField(auto_now_add=True)
    modified_on         = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class LoanApplications(models.Model):
    lender       = models.ForeignKey(LenderProfile, on_delete=models.CASCADE)
    loan_product = models.ForeignKey(LoanProduct, on_delete=models.CASCADE)
    borrower     = models.ForeignKey(User, on_delete=models.CASCADE)
    principle    = models.DecimalField( max_digits=10, decimal_places=2)
    interest     = models.DecimalField( max_digits=10, decimal_places=2)
    fees         = models.DecimalField( max_digits=10, decimal_places=2)
    total        = models.DecimalField( max_digits=10, decimal_places=2)
    application_status = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    ])
    has_previous_loan = models.BooleanField(default=False)
    remarks      = models.TextField(null=True, blank=True,max_length=1000)
    created_on   = models.DateField(auto_now_add=True)
    modified_on  = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Loan Application'
        verbose_name_plural = 'Loan Applications'


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Loan Disbursement', 'Loan Disbursement'),
        ('Interest Charges', 'Interest Charges'),
        ('Excise Duty', 'Excise Duty'),
        ('Loan Repayment', 'Loan Repayment'),
        )
    borrower         = models.ForeignKey(User, on_delete=models.CASCADE)
    product          = models.ForeignKey(LoanProduct, on_delete=models.CASCADE)
    lender           = models.ForeignKey(LenderProfile, on_delete=models.CASCADE)
    transaction_id   = models.AutoField(primary_key=True)
    # loan_id          = models.IntegerField( null=False, blank=False)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    transaction_date = models.DateTimeField(auto_now=True)
    debit            = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    credit           = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description      = models.TextField()
    balance          = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}"

    class Meta:
        ordering = ['transaction_date']

    objects = TransactionManager()


class LoansCounter(models.Model):
    lender         = models.ForeignKey(LenderProfile, on_delete=models.CASCADE)
    applied_loans  = models.IntegerField(default=0)
    approved_loans = models.IntegerField(default=0)
    created_on     = models.DateField(auto_now_add=True)
    modified_on    = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Loan Counter'
        verbose_name_plural = 'Loans Counter'