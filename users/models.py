from django.db import models
from datetime import datetime
from django.core.validators import MaxValueValidator
from django.core.validators import RegexValidator
from account.models import User


# Create your models here.

class Users(models.Model):
    contact = models.BigIntegerField(validators=[MaxValueValidator(9999999999)], null=True)
    image = models.ImageField(default='default.png', blank=True)
    gender = models.CharField(max_length=8, null=True)
    dob = models.DateField(default=datetime.today)
    created_at: datetime = models.DateTimeField(default=datetime.now, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Users"


class Address(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    contactno = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    name = models.CharField(max_length=80)
    is_primary = models.CharField(max_length=1, default='0')
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Address"
