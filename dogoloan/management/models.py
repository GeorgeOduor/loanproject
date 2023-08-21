from django.db import models
from users.models import User
from lenders.models import LenderProfile,Agents

# Create your models here.
class BorrowerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agents, on_delete=models.CASCADE, null=True, blank=True)
     # borower profile
    alternative_mobile_number = models.CharField(max_length=12, null=True, blank=True)
    referer_mobile_number     = models.CharField(max_length=12, null=True, blank=True)
    employment_status = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
        ('Self Employed', 'Self Employed'),
        ('Student', 'Student'),
        ('Retired', 'Retired'),
        ('Other', 'Other')
        ])
    marital_status = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('Married', 'Married'),
        ('Single', 'Single'),
        ])
    education = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('Primary School', 'Primary School'),
        ('Secondary School', 'Secondary School'),
        ('University', 'University'),
        ('Other', 'Other')
        ])

    class Meta:
        verbose_name = 'Borrower Profile'
        verbose_name_plural = 'Borrower Profile'

    lender = models.ForeignKey(LenderProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    interest_rate = models.IntegerField( null=True, blank=True)
    min_loan_amount = models.CharField(max_length=50, null=True, blank=True)
    max_loan_amount = models.CharField(max_length=50, null=True, blank=True)
    min_duration = models.CharField(max_length=50, null=True, blank=True)