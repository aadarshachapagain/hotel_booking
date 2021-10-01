from django.db import models
from datetime import datetime

from hotel.CreditCard.models import CreditCard
from hotel.models import Hotels


class PaymentPolicies(models.Model):
	credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, blank=True,null=True)
	hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE,blank=True, null=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	
	def __str__(self):
		return self.credit_card.name
	
	class Meta:
		verbose_name_plural = "Payment Policy"
