from django.db import models
from travel.utils import all_percentage_complete
from hotel.inventory.models import HotelInventory
from hotel.amenities.models import HotelAmenities


class AddOnServices(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flatorpercent = models.BooleanField(default=False, blank=True)
    inventory = models.ForeignKey(HotelInventory, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=False, blank=True)
    amenities = models.ForeignKey(HotelAmenities, on_delete=models.CASCADE, null=True)
    is_recommended = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.price

    @property
    def percentage_complete(self):
        return all_percentage_complete(self)

    class Meta:
        verbose_name_plural = "AddOnServices"
