from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models
from hotel.models import Hotels
from travel.utils import all_percentage_complete


class B2B(models.Model):
	hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, null=True)
	third_party_name = models.CharField(max_length=200, blank=True, null=True)
	price = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	group_size = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1)])
	invoiceTo = models.CharField(max_length=200, blank=True, null=True)
	start_date = models.DateTimeField(default=datetime.now, blank=True)
	end_date = models.DateTimeField(blank=True, null=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	status = models.BooleanField(default=False)
	
	class Meta:
		verbose_name_plural = "Business to Business"
	
	@property
	def percentage_complete(self):
		return all_percentage_complete(self)
