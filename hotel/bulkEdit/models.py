from django.db import models
from datetime import datetime


class PriceAlterLog(models.Model):
    hotel = models.BigIntegerField(blank=True, null=True)
    hotel_inventory = models.BigIntegerField(blank=True, null=True)
    altered_type = models.CharField(blank=True, null=True, max_length=50)
    altered_percent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    altered_group = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.altered_type

    class Meta:
        verbose_name_plural = "Price Altered Table"
