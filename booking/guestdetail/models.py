from django.db import models
from datetime import datetime

from booking.customer.models import Customer
from hotel.Country.models import Country
from hotel.city.models import City
from hotel.state.models import State
from users.models import User
from django.core.validators import RegexValidator
from datetime import date
from django.core.exceptions import ValidationError


def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('DOB cannot be in the future.')


class GuestDetail(models.Model):
    name = models.CharField(max_length=60, null=True)
    email = models.EmailField(null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                               null=True)  # validators should be a list
    status = models.IntegerField(null=True, default=0, blank=True)
    # address = models.CharField(max_length=80, blank=True, null=True)
    country = models.CharField(max_length=80, blank=True, null=True)
    # city = models.CharField(max_length=80, blank=True, null=True)
    # gender = models.CharField(max_length=10, null=True)
    # dob = models.DateField(validators=[no_future], blank=True, null=True)
    # validator for future date
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    # booking = models.ForeignKey(BookingTable, on_delete=models.CASCADE, blank=True, null=True, related_name='guest_booking')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    parent_status = models.BooleanField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Guest Detail"
    #
    # def delete(self, *args, **kwargs):
    #     self.image.delete()
    #     super().delete(*args, **kwargs)
