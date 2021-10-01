from datetime import datetime
from django.db import models
from hotel.inventory.models import HotelInventory
from hotel.models import Hotels
from travel.utils import all_percentage_complete


class GroupRate(models.Model):
	hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name="grouprate")
	range_start = models.IntegerField(blank=True, null=True)
	range_end = models.IntegerField(blank=True, null=True)
	map_cost = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	ap_cost = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	status = models.BooleanField(default=False)

	
	class Meta:
		verbose_name_plural = "GroupRate"
	
	# @property
	# def percentage_complete(self):
	# 	return all_percentage_complete(self)
