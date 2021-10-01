from django.db import models
from datetime import datetime, date
from booking.booking_table.models import BookingTable
from booking.customer.models import Customer
from booking.module_booking.models import ModuleBooking
from booking.points_on_sale.models import PointsOnSale
from booking.referee_and_referred.models import RefereeAndReferred
from booking.team_leader.models import TeamLeader
from hotel.models import Hotels
from points.membership_plan.models import Membership_plan
from users.models import User


class CreditPoint(models.Model):
	transaction = models.ForeignKey(BookingTable, on_delete=models.CASCADE)
	booking = models.ForeignKey(ModuleBooking, on_delete=models.CASCADE,blank=True, null=True)
	user = models.ForeignKey(Customer, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	# transaction_amount stores points
	transaction_amount = models.IntegerField(blank=True, null=True)
	net_total = models.IntegerField(blank=True, null=True)
	remark = models.CharField(blank=True, null=True, max_length=200)
	status = models.BooleanField(blank=True, null=True, default=False)
	
	def __int__(self):
		return self.transaction
	
	def save(self, *args, **kwargs):
		# change transaction into CP according to value present in points_on_sale model
		# for hotel with star
		if self.transaction_amount == None:
			module_id = self.booking
			date_format = "%Y-%m-%d"
			b = datetime.strptime(str(module_id.end_date), date_format)
			a = datetime.strptime(str(module_id.start_date), date_format)
			night_count = (b - a).days
			star = Hotels.objects.get(id=module_id.company_id).star_rating
			credit_point_value = PointsOnSale.objects.get(sale_type__icontains=star).credit_point
			self.transaction_amount = credit_point_value * night_count
			refer_count = RefereeAndReferred.objects.filter(to=self.user_id).count()
			if refer_count > 0:
				new_credit_instance = CreditPoint()
				refer_instance = RefereeAndReferred.objects.get(to=self.user_id)
				membership = Customer.objects.get(user=refer_instance.by_id).memplan
				splitted = membership.type.split()
				mem_count = TeamLeader.objects.filter(type__icontains=splitted[0]).count()
				if mem_count > 0:
					bonus = TeamLeader.objects.get(type__icontains=splitted[0]).bonus_credit_point
					new_cp = (bonus * self.transaction_amount) / 100
					new_credit_instance.user = refer_instance.by
					new_credit_instance.transaction_id = self.transaction_id
					new_credit_instance.booking_id = self.booking_id
					new_credit_instance.remark = "from team member"
					new_credit_instance.transaction_amount = new_cp
					new_credit_instance.save()
		else:
			self.transaction_amount = self.transaction_amount
		
		count = CreditPoint.objects.exclude(id=self.id).filter(user=self.user.user_id).count()
		if count > 0:
			reward_instance = CreditPoint.objects.exclude(id=self.id).filter(user=self.user.user_id).latest(
				'created_at')
			self.net_total = reward_instance.net_total + self.transaction_amount
		
		else:
			self.net_total = self.transaction_amount
		return super(CreditPoint, self).save()
	
	class Meta:
		verbose_name_plural = "Credit Points"
