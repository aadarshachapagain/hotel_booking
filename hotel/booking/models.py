from django.db import models
from datetime import datetime
from users.models import Users
from ..inventory.models import HotelInventory
from django.core.validators import MaxValueValidator, MinValueValidator
# from .booking.models import HotelBooking


class HotelBooking(models.Model):
    hotelinventory_id = models.ForeignKey(
    HotelInventory, on_delete=models.CASCADE)
    user_id = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    no_of_adult=models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)])
    no_of_child=models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)]) 
    
    no_of_room = models.DecimalField(max_digits=3, decimal_places=0)
    pay_mode = models.CharField(max_length=10)
    pay_status = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Hotel Bookings"