from django.db import models
from datetime import datetime
from django.utils import timezone
from booking.booking_table.models import BookingTable
from booking.customer.models import Customer
from booking.module_booking.models import ModuleBooking
from users.models import User

class BusinessCashBonus(models.Model):
    transaction = models.ForeignKey(BookingTable, on_delete=models.CASCADE)
    booking = models.ForeignKey(ModuleBooking, on_delete=models.CASCADE,blank=True, null=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    cash_bonus_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    net_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    remark = models.CharField(blank=True, null=True, max_length=200)
    status = models.BooleanField(blank=True, null=True, default=False)

    def __int__(self):
        return self.transaction
    
    def save(self, *args, **kwargs):
        
        count=BusinessCashBonus.objects.exclude(id=self.id).filter(user=self.user.user_id).count()
        if count > 0:
            business_cash_instance = BusinessCashBonus.objects.exclude(id=self.id).filter(user=self.user.user_id).latest('created_at')
            self.net_total = business_cash_instance.net_total + self.cash_bonus_amount
            
        else:
            self.net_total = self.cash_bonus_amount
        return super(BusinessCashBonus, self).save()
        

    class Meta:
        verbose_name_plural = "Business Cash Bonus"

   