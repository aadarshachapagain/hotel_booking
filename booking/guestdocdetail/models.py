from django.db import models
from datetime import datetime

from booking.customer.models import Customer
from booking.guestdetail.models import GuestDetail
from hotel.Country.models import Country
from hotel.city.models import City
from hotel.state.models import State
from users.models import User
from django.core.validators import RegexValidator
from datetime import date
from django.core.exceptions import ValidationError


def no_past(value):
    today = date.today()
    if value < today:
        raise ValidationError('Visa Expiry  cannot be in Past.')


class GuestDocDetail(models.Model):
    document_type = models.CharField(max_length=60, null=True)
    status = models.IntegerField(null=True, default=0, blank=True)
    #for contingency
    document_number = models.CharField(max_length=60, null=True)
    issuing_country = models.CharField(max_length=60, null=True)
    doc_file = models.FileField(upload_to='documents/')
    visa_required = models.CharField(max_length=60, null=True)
    visa_expiry = models.DateField(validators=[no_past], blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    # booking = models.CharField(max_length=10, null=True, blank=True)
    guest_detail = models.ForeignKey(GuestDetail, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self. document_type

    class Meta:
        verbose_name_plural = "Guest Document Detail"
    #
    # def delete(self, *args, **kwargs):
    #     self.image.delete()
    #     super().delete(*args, **kwargs)
