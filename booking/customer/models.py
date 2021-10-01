from django.db import models
from datetime import datetime

from hotel.Country.models import Country
from hotel.city.models import City
from hotel.state.models import State
from account.models import User
from django.core.validators import RegexValidator
from datetime import date
from django.core.exceptions import ValidationError
from points.membership_plan.models import Membership_plan
from booking.business_partners.models import BusinessPartners



def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('DOB cannot be in the future.')


class Customer(models.Model):
    name = models.CharField(max_length=60, null=True)
    # email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17, blank=True,
                               null=True)  # validators should be a list
    status = models.IntegerField(null=True, default=0, blank=True)
    address = models.CharField(max_length=80, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    # state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    # city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=10, null=True)
    dob = models.DateField(validators=[no_future], blank=True, null=True)
    # validator for future date
    image = models.ImageField(blank=True, default='default.png')
    reward = models.IntegerField(null=True, default=0, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    memplan = models.ForeignKey(Membership_plan, on_delete=models.CASCADE, null=True, blank=True,
                                related_name='membership')
    partnerplan = models.ForeignKey(BusinessPartners, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='partnership')
    uniqtoken = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.name == None:
            return "default"
        if self.image == None:
            return "default.png"
        return self.name

    class Meta:
        verbose_name_plural = "Customer"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        dob = str(self.dob)
        dob = dob.replace('-', '')
        self.uniqtoken = str(self.user.id) + dob
        
        # if self.image==None:
        #     self.image =
        return super(Customer, self).save()
