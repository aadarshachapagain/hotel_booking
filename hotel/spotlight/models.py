from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime
from hotel.models import Hotels


class Spotlight(models.Model):
    hotel = models.ForeignKey(Hotels, related_name='spotlight', on_delete=models.CASCADE)
    # hotel = models.OneToOneField(Hotels, related_name='spotlight', on_delete=models.CASCADE)
    start_date = models.DateField(max_length=60, null=True, blank=True)
    # ('booked_date', models.DateField(blank=True, max_length=60, null=True)),
    end_date = models.DateField(max_length=60, null=True, blank=True)
    nameofdepositor = models.CharField(max_length=80, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact1 = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                                null=True)  # validators should be a list
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.hotel

    class Meta:
        verbose_name_plural = "Spotlight"
