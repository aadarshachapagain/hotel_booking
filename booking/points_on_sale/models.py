from django.db import models
from datetime import datetime
from booking.booking_table.models import BookingTable
from booking.customer.models import Customer
from booking.module_booking.models import ModuleBooking
from users.models import User


class PointsOnSale(models.Model):
	sale_type = models.CharField(blank=True, null=True, max_length=200)
	# sale  type can be  either package or different type of hotel room(no star, 1-3, star, 4 star)
	# package includes vehicle rental, tour package, trekking package, expedition package
	
	credit_point = models.IntegerField(blank=True, null=True)
	# credit point earned on sale of particular type of packages as metioned above
	
	virtualpoint = models.IntegerField(blank=True, null=True)
	
	# virtual point earned on sale of particular type of packages as metioned above
	
	# by = models.ForeignKey(Customer, on_delete=models.CASCADE)
	# model = models.ForeignKey(Customer, on_delete=models.CASCADE)
	
	# transaction = models.ForeignKey(BookingTable, on_delete=models.CASCADE)
	# booking = models.ForeignKey(ModuleBooking, on_delete=models.CASCADE)
	# user = models.ForeignKey(Customer, on_delete=models.CASCADE)
	# created_at = models.DateTimeField(default=datetime.now, blank=True)
	# transaction_amount = models.IntegerField(blank=True, null=True)
	# net_total = models.IntegerField(blank=True, null=True)
	# remark = models.CharField(blank=True, null=True, max_length=200)
	# status = models.BooleanField(blank=True, null=True, default=False)
	
	def __int__(self):
		return self.sale_type
	
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
		verbose_name_plural = "points_on_sale"
