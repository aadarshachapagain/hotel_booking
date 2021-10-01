from django.db import models
from datetime import datetime
from booking.booking_table.models import BookingTable
from booking.customer.models import Customer
from points.membership_plan.models import Membership_plan
from booking.business_partners.models import BusinessPartners
from booking.module_booking.models import ModuleBooking
from users.models import User


class RefereeAndReferred(models.Model):
    by = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='by')
    to = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='to', unique=True)
    status = models.CharField(blank=True, null=True, max_length=50)
    # wannabeType = models.CharField(blank=True, null=True, max_length=50)
    # membership = models.ForeignKey(Membership_plan, on_delete=models.CASCADE, related_name='memtype', blank=True,
    #                                null=True)
    partnership = models.ForeignKey(BusinessPartners, on_delete=models.CASCADE, related_name='partnertype', blank=True,
                                    null=True)

    def __int__(self):
        return self.by

    class Meta:
        verbose_name_plural = "referee_and_referred"
