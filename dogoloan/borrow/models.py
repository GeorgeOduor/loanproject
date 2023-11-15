from django.db import models

# Create your models here.
from users.models import User
from lenders.models import LenderProfile

class BorrowerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # agent = models.ForeignKey(Agents, on_delete=models.CASCADE, null=True, blank=True)
     # borower profile
    alternative_mobile_number = models.CharField(max_length=12, null=True, blank=True)
    referer_mobile_number     = models.CharField(max_length=12, null=True, blank=True)
    employment_status = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('employed', 'Employed'),
        ('unemployed', 'Unemployed'),
        ('self-employed', 'Self Employed'),
        ('student', 'Student'),
        ('retired', 'Retired'),
        ('other', 'Other')
        ])
    employment_sector = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('agriculture', 'Agriculture'),
        ('manufacturing', 'Manufacturing'),
        ('services', 'Services'),
        ('construction', 'Construction'),
        ('retail', 'Retail'),
        ('wholesale', 'Wholesale'),
        ('transport', 'Transport'),
        ('education', 'Education'),
        ('health', 'Health'),
        ('other', 'Other')
        ])
    marital_status = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('married', 'Married'),
        ('single', 'Single'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
        ('other', 'Other')
        ])
    education = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('primary', 'Primary School'),
        ('secondary', 'Secondary School'),
        ('tertiary', 'Tertiary'),
        ('university', 'University'),
        ('Other', 'Other')
        ])
    income_range = models.CharField(max_length=50, null=True, blank=True,
                                    choices=[('1', '0-10,000'), ('2', '10,000-20,000'), ('3', '20,000-30,000'),
                                               ('4', '30,000-40,000'), ('5', '40,000-50,000'), ('6', 'Above 50,000')])
    # addres details
    zip_code          = models.CharField(max_length=50, null=True, blank=True)
    county            = models.CharField(max_length=50, null=True, blank=True)
    country           = models.CharField(max_length=50, null=True, blank=True,default="Kenya")


    class Meta:
        verbose_name = 'Borrower Profile'
        verbose_name_plural = 'Borrower Profile'

    lender = models.ForeignKey(LenderProfile, on_delete=models.CASCADE, null=True, blank=True)
    # name = models.CharField(max_length=50, null=True, blank=True)
    # interest_rate = models.IntegerField( null=True, blank=True)
    # min_loan_amount = models.CharField(max_length=50, null=True, blank=True)
    # max_loan_amount = models.CharField(max_length=50, null=True, blank=True)
    # min_duration = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True,
                               choices=[('Active', 'Active'), ('Inactive', 'Inactive')],
                               default='Active')
    loan_limit = models.CharField(max_length=50, null=True, blank=False, default=0)

class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('borrower', 'Borrower'),
        ('lender', 'Lender'),
        ('admin', 'Admin')
    ])
    type = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('loan_disbursement', 'Loan Disbursement'),
        ('loan_repayment', 'Loan Repayment'),
    ])
    title = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
