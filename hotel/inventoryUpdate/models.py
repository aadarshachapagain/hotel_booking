from django.db import models

from hotel.inventory.models import HotelInventory
from hotel.models import Hotels
from datetime import datetime


class InventoryUpdate(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, null=True)
    inventory = models.ForeignKey(HotelInventory, on_delete=models.CASCADE, null=True)
    cancellation_type = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=80, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    is_booked = models.BooleanField(blank=True, null=True)
    is_available = models.CharField(max_length=80, null=True, default='checked')
    european_plan = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    bedandbreakfast_plan = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.hotel.prop_id.business_name

    class Meta:
        verbose_name_plural = "Inventory Updates"
