from django.db import models
from datetime import datetime


class HotelAmenities(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(blank=True)
    status = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Hotel Amenities"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
