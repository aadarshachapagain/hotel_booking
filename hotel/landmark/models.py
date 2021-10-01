from django.db import models

from hotel.city.models import City


class Landmark(models.Model):
    # image = models.ImageField(default='default.png')
    # as agreed by raj and shraddha image is removed from landmark
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True)

    # city = models.ForeignKey(City, related_name='landmark', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Landmarks"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
