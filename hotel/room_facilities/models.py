from django.db import models
from datetime import datetime


class RoomFacilities(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True, blank=True)
    chargeable = models.BooleanField(default=0, null=True, blank=True)
    image = models.ImageField(blank=True, default='default.png')
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Room Facilities"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
