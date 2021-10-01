from django.db import models
from hotel.roomtype.models import HotelRoomType


class BedType(models.Model):
	name = models.CharField(max_length=200, blank=True)
	description = models.TextField(blank=True, max_length=500, null=True)
	count = models.IntegerField(blank=True, null=True)
	roomtype = models.ForeignKey(HotelRoomType, on_delete=models.CASCADE, blank=True, null=True)
	status = models.CharField(max_length=20, blank=True, null=True)
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = "Bed Type"
