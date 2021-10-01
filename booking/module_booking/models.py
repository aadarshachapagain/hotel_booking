from django.db import models
from datetime import datetime

from booking.booking_table.models import BookingTable
from booking.customer.models import Customer


class ModuleBooking(models.Model):
	module_name = models.CharField(max_length=250, null=True)
	quantity = models.IntegerField(blank=True)
	start_date = models.DateField(max_length=60, null=True, blank=True)
	end_date = models.DateField(max_length=60, null=True, blank=True)
	
	sub_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	discount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	tax = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	
	status = models.CharField(max_length=250, null=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	updated_at = models.DateTimeField(default=datetime.now, blank=True)
	company_id = models.IntegerField(blank=True, null=True)
	inventory_id = models.IntegerField(blank=True, null=True)
	
	# foreign key
	booking = models.ForeignKey(BookingTable, on_delete=models.CASCADE, blank=True, null=True, related_name='module_booking')
	# customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, related_name='customer')
	# foreign key
	
	def __str__(self):
		return self.module_name
	
	class Meta:
		verbose_name_plural = "Module Booking"
