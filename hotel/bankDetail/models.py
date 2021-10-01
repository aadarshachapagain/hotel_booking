from django.db import models
from hotel.Country.models import Country
from hotel.models import Hotels
from travel.utils import all_percentage_complete


class BankDetail(models.Model):
    bankCountry = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    bankName = models.CharField(max_length=200,blank=True, null=True)
    swiftCode = models.CharField(blank=True, null=True,max_length=200)
    accountNumber = models.CharField(max_length=200,blank=True, null=True)
    accountName = models.CharField(max_length=200,blank=True, null=True)
    invoiceTo = models.CharField(max_length=200,blank=True, null=True)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE, null=True)

    
    class Meta:
        verbose_name_plural = "Bank Detail"

    @property
    def percentage_complete(self):
        return all_percentage_complete(self)
    