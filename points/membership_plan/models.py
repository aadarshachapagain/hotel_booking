from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import datetime


class Membership_plan(models.Model):
    type = models.CharField(max_length=100, null=True)

    #     #guest, gold team leader/member/partner, platinum leader/member/partner, diamond member/leader/partner
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    renewal_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    # price to be paid while renewal of account.
    reward_point = models.IntegerField(null=True, default=0)
    # point gained by user when subscribing for membership(Gold membership, Platinum membership, Diamond membership)
    # this rp is gained only by user who sign up for membership not by the one who refers other member.(referer)
    virtual_point = models.IntegerField(null=True, default=0)
    # point gained by user when subscribing for membership(Gold membership, Platinum membership, Diamond membership)
    virtual_point_for_old = models.IntegerField(null=True, default=0)
    # point gained by user for referring  membership (Gold membership, Platinum membership, Diamond membership)
    # to other member(virtual point is shared by both parties.(referrer and  referred one))
    credit_point_for_old = models.IntegerField(null=True, default=0)
    # point gained by user for referring  membership (Gold membership, Platinum membership, Diamond membership)
    # to other member(credit point is gained by referrer only)
    upgrade_reward_point = models.IntegerField(null=True, default=0)
    # reward point assigned while upgrading from one membership to another.
    position = models.IntegerField(null=True)
    # if gold: [1] , platinum :[2], diamond :[3]
    #     # price for account ownership
    renewal_cond = models.IntegerField(null=True,
                                       validators=[MaxValueValidator(100), MinValueValidator(12)])
    #     #12 months, 24months
    expiry_cond = models.IntegerField(null=True,
                                      validators=[MaxValueValidator(100), MinValueValidator(12)])
    #     # 12 months, 24months
    maturity_time = models.IntegerField(null=True,
                                        validators=[MaxValueValidator(100), MinValueValidator(12)])
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    # status = models.IntegerField(null=True, default=0, blank=True)
    status = models.BooleanField(blank=True, null=True, default=False)


def __str__(self):
    return self.type


class Meta:
    verbose_name_plural = "Membership_plan"
