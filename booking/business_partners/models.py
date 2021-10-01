from django.db import models
from datetime import datetime
from users.models import User


class BusinessPartners(models.Model):
    type = models.CharField(blank=True, null=True, max_length=200)
    # type is possible partnership option such as gold business partner, platinum business partner, diamond business partner

    setupcost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # Account setup fee
    renewalcost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # Account renewal fee
    acctransferable = models.BooleanField(null=True, blank=True)
    # Is account ownership is transferable  or not for particular business type.
    refundable = models.BooleanField(null=True, blank=True, default=False)
    # Is account setup is refundable  or not for particular business type.
    flightincludedCb = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # cash bouns(CB) earned while selling package which includes flightticket
    flightexcludedCb = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # cash bouns earned  while selling package which excludes flightticket
    flightincludedVb = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # Virtual Bouns(VB) earned  while selling package which includes flightticket

    package_worth = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # while selling similar type of package of certain quantity a package worth of same amount is given free
    # for the partner of particular type
    count = models.IntegerField(blank=True, null=True)
    #count is for the number of such package

    return_ticket_worth = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # while selling flight ticket of certain quantity a return ticket worth of 25000 is given free
    # for the partner of particular type
    countforreturnticket = models.IntegerField(blank=True, null=True)
    # countforreturnticket is for the quantity of such flight(100 specified in doc)
    credit_point_for_old = models.IntegerField(null=True, default=0)
    # point gained by user for referring  partnership (Gold partnership, Platinum partnership, Diamond partnership)
    # to other partner(credit point is gained by referrer only)




    def __int__(self):
        return self.type

    # def save(self, *args, **kwargs):
    #
    #     count = CreditPoint.objects.exclude(id=self.id).filter(user=self.user.user_id).count()
    #     print(count)
    #     if count > 0:
    #         reward_instance = CreditPoint.objects.exclude(id=self.id).filter(user=self.user.user_id).latest(
    #             'created_at')
    #         self.net_total = reward_instance.net_total + self.transaction_amount
    #
    #     else:
    #         self.net_total = self.transaction_amount
    #     return super(CreditPoint, self).save()

    class Meta:
        verbose_name_plural = "BusinessPartners"
