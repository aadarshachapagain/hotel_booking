from django.db import models
from hotel.inventory.models import HotelInventory
from hotel.offers.models import Offers
from datetime import datetime



class InventoryOffers(models.Model):
    hotel_inventory = models.ForeignKey(HotelInventory, on_delete=models.CASCADE, blank=True, related_name='inv_offer')
    offer = models.ForeignKey(Offers, on_delete=models.CASCADE, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    
    def __str__(self):
        return self.offer.offer_name

    class Meta:
        verbose_name_plural = "Inventory Offers"
