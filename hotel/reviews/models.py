from django.db import models
from datetime import datetime

# from .amenities.models import HotelAmenities
from account.models import User
from booking.customer.models import Customer
from ..models import Hotels


class HotelReview(models.Model):
    # module = models.IntegerField(blank=True, null=True)
    module = models.CharField(max_length=50, null=True, blank=True)
    company_id = models.IntegerField(blank=True, null=True)
    inventory_id = models.IntegerField(blank=True, null=True)
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField(blank=True)

    def __str__(self):
        return self.user_id.email

    class Meta:
        verbose_name_plural = "Review and Rating"
