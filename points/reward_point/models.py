from django.db import models
from datetime import datetime
from django.utils import timezone
from booking.booking_table.models import BookingTable
from booking.customer.models import Customer
from booking.module_booking.models import ModuleBooking
from users.models import User

class RewardPoint(models.Model):
    transaction = models.ForeignKey(BookingTable, on_delete=models.CASCADE)
    booking = models.ForeignKey(ModuleBooking, on_delete=models.CASCADE,blank=True, null=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    transaction_amount = models.IntegerField(blank=True, null=True)
    net_total = models.IntegerField(blank=True, null=True)
    remark = models.CharField(blank=True, null=True, max_length=200)
    status = models.BooleanField(blank=True, null=True, default=False)

    def __int__(self):
        return self.transaction
    
    def save(self, *args, **kwargs):
        
        count=RewardPoint.objects.exclude(id=self.id).filter(user=self.user.user_id).count()
        if count > 0:
            reward_instance = RewardPoint.objects.exclude(id=self.id).filter(user=self.user.user_id).latest('created_at')
            self.net_total = reward_instance.net_total + self.transaction_amount
            
        else:
            self.net_total = self.transaction_amount
        return super(RewardPoint, self).save()
        

    class Meta:
        verbose_name_plural = "Reward Points"

   