from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

from django.db import models
from users.models import User


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
    loan_amount  = models.CharField(max_length=50, null=True, blank=True)
    application_status = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    ])
    has_previous_loan = models.BooleanField(default=False)
    remarks = models.TextField(null=True, blank=True,max_length=1000)
    created_on   = models.DateField(auto_now_add=True)
    modified_on  = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Loan Application'
        verbose_name_plural = 'Loan Applications'