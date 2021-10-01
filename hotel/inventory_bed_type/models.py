from django.db import models
from datetime import datetime
from hotel.inventory.models import HotelInventory
from hotel.bedType.models import BedType


class Inventory_Bed_Type(models.Model):
    bed_type = models.ForeignKey(BedType, on_delete=models.CASCADE, related_name="bed_type")
    """
    shifted bed count to bed type table. Now admin will specify bed quantity during room type creation.
    """
    # bed_count = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    inventory = models.ForeignKey(HotelInventory, on_delete=models.CASCADE, related_name="inv_bed_type")

    def __int__(self):
        return self.bed_type

    class Meta:
        verbose_name_plural = "Inventory Bed Types"
