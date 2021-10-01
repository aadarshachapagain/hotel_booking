from django.db import models

from account.owner_profile.models import OwnerProfile


class Offers(models.Model):
    offer_name = models.CharField(max_length=80, null=True, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    banner_image = models.ImageField(default='default.png')
    rate = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    status = models.BooleanField(default=False)
    module = models.CharField(max_length=80, null=True, blank=True)
    creator = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE, blank=True, related_name='creator', null=True)
    
    def __str__(self):
        return self.offer_name
    
    def module_without_underscore(self):
        return self.module.replace('_', ' ')

    class Meta:
        verbose_name_plural = "Offers"
