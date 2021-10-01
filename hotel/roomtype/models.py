from django.db import models


class HotelRoomType(models.Model):
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = "Hotel Room Type"
