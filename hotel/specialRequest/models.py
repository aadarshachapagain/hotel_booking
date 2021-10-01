from datetime import datetime
from django.db import models
from hotel.models import Hotels
from travel.utils import all_percentage_complete


class specialRequest(models.Model):

	# nisham suggested that special request are assigned by admin not vendor 03/24/2020
	# hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name="specialRequest")
	item = models.CharField(max_length=200, blank=True, null=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	status = models.BooleanField(default=False)
	
	class Meta:
		verbose_name_plural = "Special Request"
	
	# @property
	# def percentage_complete(self):
	# 	return all_percentage_complete(self)
