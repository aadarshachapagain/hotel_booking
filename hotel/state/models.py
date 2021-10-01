from django.db import models

from hotel.Country.models import Country


class State(models.Model):
    name = models.CharField(max_length=200)
    # country = models.ForeignKey(, on_delete=models.CASCADE, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True)
    class Meta:
        verbose_name_plural = "State"
        
    def __str__(self):
        return self.name
    #
    # def delete(self, *args, **kwargs):
    #     self.image.delete()
    #     super().delete(*args, **kwargs)