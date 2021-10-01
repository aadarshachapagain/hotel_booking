from django.db import models
from datetime import datetime
from ..owner.models import HotelOwner
from hotel.models import Hotels
from account.models import User

class HotelStaff(models.Model):
    name = models.CharField(max_length=80,null=True)    
    contact = models.BigIntegerField(unique=True,null=True)    
    # email = models.EmailField(unique=True)
    # password = models.CharField(max_length = 30)
    image = models.ImageField(default='default.png')
    address = models.CharField(max_length=80,null=True)
    owner_id = models.ForeignKey(HotelOwner, on_delete=models.CASCADE,null=True)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs) 

    class Meta:
        verbose_name_plural = "Hotel Staffs"
