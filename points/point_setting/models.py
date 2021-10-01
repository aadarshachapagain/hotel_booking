from decimal import Decimal

from django.db import models
from datetime import datetime
from booking.booking_table.models import BookingTable
from booking.module_booking.models import ModuleBooking
from users.models import User


class PointSetting(models.Model):
    frompoint = models.CharField(max_length=200)
    topoint = models.CharField(max_length=200)
    conversion_ratio = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('1.00'))
    maturity_time = models.IntegerField(default=12)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    status = models.BooleanField(blank=True, null=True, default=False)

    def __int__(self):
        return self.conversion_ratio

    class Meta:
        verbose_name_plural = "Point Setting"
