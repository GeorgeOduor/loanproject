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
        user = self.model(msisdn=msisdn, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, msisdn, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_agent', False)
        return self._create_user(msisdn, password, **extra_fields)

    def create_superuser(self, msisdn, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_agent', False)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(msisdn, password, **extra_fields)



class User(AbstractUser):
    username = None
    msisdn = models.CharField(_('mobile number'), unique=True, max_length=12)

    objects = UserManager()

    USERNAME_FIELD = 'msisdn'
    REQUIRED_FIELDS = []
    
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('Male', 'Male'),
        ('Female', 'Female')
    ])
    date_of_birth = models.DateField(null=True, blank=True)
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
    email_address = models.EmailField(null=True, blank=True)
    alternative_mobile_number = models.CharField(max_length=12, null=True, blank=True)
    town = models.CharField(max_length=50, null=True, blank=True)
    monthly_income = models.CharField(max_length=50, null=True, blank=True)
    referer_mobile_number = models.CharField(max_length=12, null=True, blank=True)
    social_reach = models.CharField(max_length=50, null=True, blank=True)
    nationa_id = models.CharField(max_length=12, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Agents(models.Model):
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE)
    agent_location = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'

        