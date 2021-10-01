from django.db import models
from datetime import datetime


class MealPlan(models.Model):
    plan = models.CharField(max_length=50, blank=True, null=True)
    full_form = models.CharField(max_length=50, blank=True, null=True)
    status = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.plan


class Meta:
    verbose_name_plural = "MealPlan"
