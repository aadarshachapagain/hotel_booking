from django.db import models
from hotel.Country.models import Country
from datetime import datetime


class Charges(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    vat = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sc = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    citytax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=datetime.now, blank=True)


class Meta:
    verbose_name_plural = "Charges"
