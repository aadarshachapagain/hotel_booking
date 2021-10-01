from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=200, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    # code refers to dial code
    currency_code = models.CharField(max_length=20, blank=True, null=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True)


    class Meta:
        verbose_name_plural = "Country"

    def __str__(self):
        return self.name
