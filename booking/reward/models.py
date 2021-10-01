from django.db import models
from datetime import datetime
from booking.booking_table.models import BookingTable

from booking.customer.models import Customer


class Reward(models.Model):
	reward_type = models.CharField(max_length=250, null=True, blank=True)
	total_reward = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	status = models.BooleanField(default=False)
	
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	
	# foreign key
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True, related_name='customer_reward')
	booking = models.ForeignKey(BookingTable, on_delete=models.CASCADE, null=True, related_name='booking_reward')
	# foreign key
	
	def __str__(self):
		return self.reward_type
	
	class Meta:
		verbose_name_plural = "Reward"
