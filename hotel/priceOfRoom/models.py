from django.db import models
from datetime import datetime
from hotel.similarSystems.models import SimilarSystems
from hotel.mealPlan.models import MealPlan
from hotel.inventory.models import HotelInventory


class PriceInDiffSys(models.Model):
    other_systems = models.ForeignKey(SimilarSystems, related_name='other_sys', on_delete=models.CASCADE)
    meal_plans = models.ForeignKey(MealPlan, related_name='meal_other_sys', on_delete=models.CASCADE)
    inventory = models.ForeignKey(HotelInventory, related_name='inventory_other_sys', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True)
    status = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)


class Meta:
    verbose_name_plural = "PriceInDiffSys"
