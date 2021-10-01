from django.db import models
from users.models import User


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    module = models.CharField(max_length=80, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    inventory_id = models.IntegerField(blank=True, null=True)
    favourite = models.BooleanField(default=False)
    saved = models.BooleanField(default=False)


    def __str__(self):
        return self.module

    class Meta:
        verbose_name_plural = "Favourites"
