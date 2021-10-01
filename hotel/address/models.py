from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime

from hotel.Country.models import Country
from hotel.state.models import State
from travel.utils import all_percentage_complete
from ..models import Hotels
from hotel.landmark.models import Landmark
from hotel.city.models import City


class HotelAddress(models.Model):
    hotel = models.OneToOneField(Hotels, related_name='address', on_delete=models.CASCADE, primary_key=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=80, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{3}\-?1?\d{7,15}$',
                                 message="Phone number must be entered in the format: '+977-9849755595'. Up to 15 digits allowed.")

    contact1 = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                null=True)  # validators should be a list
    contact2 = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                null=True)  # validators should be a list
    latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    longitude = models.DecimalField(max_digits=22, decimal_places=16, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    landmarks = models.ManyToManyField(Landmark, related_name='hotellandmarks')
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.address

    @property
    def percentage_complete(self):
        return all_percentage_complete(self)

    class Meta:
        verbose_name_plural = "Address"
