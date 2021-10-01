from datetime import datetime
from django.db import models

from hotel.inventory.models import HotelInventory
from hotel.models import Hotels
from travel.utils import all_percentage_complete


class cribsPolicy(models.Model):
	hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name="cribs")
	age_category = models.CharField(max_length=200, blank=True, null=True)
	age_start = models.IntegerField(blank=True, null=True)
	age_end = models.IntegerField(blank=True, null=True)
	cost_status = models.CharField(max_length=200, blank=True, null=True)
	cost = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	unit = models.CharField(max_length=200, blank=True, null=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	status = models.BooleanField(default=False)
	hotelInventory = models.ForeignKey(HotelInventory, on_delete=models.CASCADE, blank=True, null=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
	change_status = models.CharField(blank=True, null=True, max_length=20)
	
	# for season and off-season
	season_start_date = models.DateTimeField(null=True, blank=True)
	season_end_date = models.DateTimeField(blank=True, null=True)
	day = models.CharField(blank=True, null=True, max_length=300)
	
	class Meta:
		verbose_name_plural = "Cribs Policy"
	
	# @property
	# def percentage_complete(self):
	# 	return all_percentage_complete(self)
