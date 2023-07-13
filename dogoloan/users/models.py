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
        return self._create_user(msisdn, password, **extra_fields)

    def create_superuser(self, msisdn, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

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
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True,choices=[
        ('Male', 'Male'),
        ('Female', 'Female')
    ])
    phone_number = models.CharField(max_length=12, null=True, blank=True)
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