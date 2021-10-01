from django.db import models
from datetime import datetime

from hotel.inventory.models import HotelInventory
from hotel.models import Hotels
from travel.utils import all_percentage_complete


class Cancellation_Policy(models.Model):
    cancellation_type_id = models.IntegerField(blank=True, null=True)
    cancellation_type = models.CharField(max_length=50,blank=True, null=True)
    hour = models.CharField(blank=True, null=True, max_length=200)
    price = models.CharField(blank=True, null=True, max_length=200)
    no_show = models.CharField(blank=True, null=True, max_length=200)
    
    # for storing policies that is being currently used
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(blank=True, null=True)
    
    # for season and off-season
    season_start_date = models.DateTimeField(null=True,blank=True)
    season_end_date = models.DateTimeField(blank=True, null=True)
    day = models.CharField(blank=True, null=True, max_length=400)
    
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, related_name="cancellation",blank=True, null=True)
    hotelInventory = models.ForeignKey(HotelInventory, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.cancellation_type

    class Meta:
        verbose_name_plural = "Cancellation Policy"

    @property
    def percentage_complete(self):
        return all_percentage_complete(self)
