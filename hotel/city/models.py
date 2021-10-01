from django.db import models

from hotel.state.models import State
from hotel.Country.models import Country


class City(models.Model):
    image = models.ImageField(default='default.png')
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True,)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True)

    class Meta:
        verbose_name_plural = "City"

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
