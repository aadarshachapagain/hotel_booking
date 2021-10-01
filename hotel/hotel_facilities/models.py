from django.db import models
from datetime import datetime


class HotelFacilities(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, default='default.png')
    category = models.CharField(default='Basic',max_length=50)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name



    class Meta:
        verbose_name_plural = "Hotel Amenities"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
