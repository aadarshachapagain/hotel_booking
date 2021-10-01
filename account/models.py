from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator


class Account_Type(models.Model):
    display_name = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=200, blank=True)
    module = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.type

    def module_without_underscore(self):
        return self.module.replace('_', ' ')

    class Meta:
        verbose_name_plural = "Account Types"


# class User(AbstractUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#     )
#     is_verified = models.IntegerField(default=0)
#     # account_type = models.ForeignKey(Account_Type, on_delete=models.CASCADE, null=True)
#     device_id = models.CharField(max_length=200, default=0)
#     account_type = models.ManyToManyField(Account_Type, related_name='account_type')
#     current_module = models.CharField(max_length=200, default=0)


#########################from here################################################

class CustomUserManager(BaseUserManager):

    # def _create_user(self, email, password, **extra_fields):
    #     """
    #     Create and save a user with the given username, email, and password.
    #     """
    #     now = timezone.now()
    #     # if not username:
    #     #     raise ValueError('The given username must be set')
    #     email = self.normalize_email(email)
    #     # username = self.model.normalize_username(username)
    #     user = self.model(email=email, date_joined=now, **extra_fields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user
    #
    # def create_user(self, email=None, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', False)
    #     extra_fields.setdefault('is_superuser', False)
    #     return self._create_user(email, password, **extra_fields)
    #
    # def create_superuser(self, email, password, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #     extra_fields.setdefault('is_active', True)
    #
    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError('Superuser must have is_staff=True.')
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError('Superuser must have is_superuser=True.')
    #
    #     return self._create_user(email, password, **extra_fields)

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Enter an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = None
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                               null=True)  # validators should be a list

    is_verified = models.BooleanField(default=0)
    is_staff = models.BooleanField(default=0)
    is_superuser = models.BooleanField(default=0)
    is_staff = models.BooleanField(default=0)
    is_active = models.BooleanField(default=0)
    device_id = models.CharField(max_length=200, default=0)
    date_joined = models.DateTimeField(default=timezone.now)
    account_type = models.ManyToManyField(Account_Type, related_name='account_type')
    current_module = models.CharField(max_length=200, default=0)
    provider = models.CharField(max_length=200, default=0)
    # username = models.CharField(max_length=200, unique=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
