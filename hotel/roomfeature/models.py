from django.db import models


class HotelRoomFeature(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Hotel Room Features"
