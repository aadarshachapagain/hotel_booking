from django.db import models
from datetime import datetime
from booking.booking_table.models import BookingTable
from booking.customer.models import Customer
from booking.module_booking.models import ModuleBooking
from users.models import User


class PointsLog(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='pointsfor')
    type = models.CharField(blank=True, null=True, max_length=50)
    points = models.IntegerField(null=True, blank=True, default=0)
    available = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(blank=True, null=True, max_length=50)

    def __int__(self):
        return self.customer

    class Meta:
        verbose_name_plural = "PointsLog"
