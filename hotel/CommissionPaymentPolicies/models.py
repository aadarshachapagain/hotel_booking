from django.db import models
from datetime import datetime

from hotel.address.models import HotelAddress
from hotel.models import Hotels
from hotel.propertyDetail.models import PropertyDetail


class CommissionPaymentPolicies(models.Model):
	hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE,blank=True, null=True)
	commission_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	invoice_name = models.ForeignKey(PropertyDetail, on_delete=models.CASCADE,blank=True, null=True)
	primary_address = models.ForeignKey(HotelAddress, on_delete=models.CASCADE,blank=True, null=True)
	alternative_address = models.CharField(max_length=500, null=True, blank=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	
	def __str__(self):
		return self.commission_percentage
	
	class Meta:
		verbose_name_plural = "Commission Payment Policies"
