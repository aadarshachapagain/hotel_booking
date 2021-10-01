from django.db import models
from datetime import datetime


class CreditCard(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    class Meta:
        verbose_name_plural = "Credit Cards"

    def __str__(self):
        return self.name
