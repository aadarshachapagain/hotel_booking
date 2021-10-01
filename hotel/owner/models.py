from django.db import models
from datetime import datetime
from account.models import User

class HotelOwner(models.Model):
    name = models.CharField(max_length=80,null=True)    
    contact = models.BigIntegerField(null=True)    
    # email = models.EmailField(unique=True,null=True)
    # password = models.CharField(max_length = 30,null=True)
    image = models.ImageField(default='default.png')
    address = models.CharField(max_length=80,null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    current_hotel = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs) 

    class Meta:
        verbose_name_plural = "Hotel Owners"
