from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, msisdn, password, **extra_fields):
        if not msisdn:
            raise ValueError('Users require an functional mobile number')
        user = self.model(msisdn = self.format_msisdn(msisdn), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, msisdn, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        return self._create_user(msisdn, password, **extra_fields)

    def create_superuser(self, msisdn, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_agent', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(msisdn, password, **extra_fields)
    
    def format_msisdn(self,msisdn):
        msisdn = f"254{str(msisdn)[-9:]}"
        print(msisdn)
        return msisdn

class User(AbstractUser):
    username = None
    msisdn = models.CharField(_('mobile number'), unique=True, max_length=12)

    objects = UserManager()

    USERNAME_FIELD = 'msisdn'
    REQUIRED_FIELDS = []

class Profile(models.Model):
    user                      = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name                = models.CharField(max_length=50, null=True, blank=True)
    last_name                 = models.CharField(max_length=50, null=True, blank=True)
    gender                    = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('Male', 'Male'),('Female', 'Female')])
    date_of_birth             = models.DateField(null=True, blank=True)
    email_address             = models.EmailField(null=True, blank=True)
    town                      = models.CharField(max_length=50, null=True, blank=True)
    # monthly_income            = models.CharField(max_length=50, null=True, blank=True)
    social_reach              = models.CharField(max_length=50, null=True, blank=True)
    national_id               = models.CharField(max_length=12, null=True, blank=True)
    # social_reach            = models.CharField(max_length=50, null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('borrower', 'Borrower'),
        ('lender', 'Lender'),
        ('admin', 'Admin')
    ])
    type = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('loan_disbursement', 'Loan Disbursement'),
        ('loan_repayment', 'Loan Repayment'),
        ('loan_request', 'Loan Request'),
        ('complaint', 'Complaint'),
        ('message', 'Message'),
        ('other', 'Other')
    ])
    title = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_on']
        