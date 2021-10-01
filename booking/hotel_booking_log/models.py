from django.db import models
from datetime import datetime

from account.staff_profile.models import StaffProfile
from booking.booking_table.models import BookingTable
from booking.customer.models import Customer
from booking.module_booking.models import ModuleBooking


class HotelBookingLog(models.Model):
	status = models.BooleanField(default=False)
	checkin_date = models.DateField(max_length=60, null=True, blank=True)
	checkout_date = models.DateField(max_length=60, null=True, blank=True)
	created_at = models.DateTimeField(max_length=60, default=datetime.now)
	# foreign key
	booking = models.ForeignKey(BookingTable, on_delete=models.CASCADE, blank=True, null=True, related_name='booking_table')
	staff = models.ForeignKey(StaffProfile, on_delete=models.CASCADE, blank=True, null=True, related_name='staff')
	
	def __str__(self):
		return self.booking
	
	class Meta:
		verbose_name_plural = "Hotel Booking Log"
