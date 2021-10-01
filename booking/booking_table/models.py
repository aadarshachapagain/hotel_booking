from django.db import models
from datetime import datetime

from django.db.models.signals import pre_save

from account.api.serializers import generateOTP
from booking.customer.models import Customer
from booking.guestdetail.models import GuestDetail


class BookingTable(models.Model):
	payment_method = models.CharField(max_length=250, null=True)
	payment_type = models.CharField(max_length=250, null=True)
	payment_status = models.CharField(max_length=250, null=True)
	total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	total_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	total_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	booked_date = models.DateField(max_length=60, null=True, blank=True)
	status = models.CharField(max_length=250, null=True)
	seenStatus = models.BooleanField(default=False)
	special_request = models.TextField(blank=True, null=True)
	pin = models.IntegerField(max_length=4, blank=True, null=True)
	confirmation_number = models.CharField(max_length=19, blank=True, null=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	
	# foreign key
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, related_name='customer_booking')
	guest = models.ForeignKey(GuestDetail, on_delete=models.CASCADE, blank=True, null=True, related_name='parent_guest')
	# foreign key
	
	def __int__(self):
		return self.customer
	
	class Meta:
		verbose_name_plural = "Booking Table"


def pre_save_pin(instance, sender, *args, **kwargs):
	if not instance.pin:
		instance.pin = generateOTP(4)


pre_save.connect(pre_save_pin, sender=BookingTable)
