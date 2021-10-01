from django.db import models


class TeamLeader(models.Model):
	type = models.CharField(blank=True, null=True, max_length=200)
	# Gold Team Leader, Platinum Team leader, Diamond Team Leader
	bonus_credit_point = models.IntegerField(blank=True, null=True)
	
	def __int__(self):
		return self.type
	
	class Meta:
		verbose_name_plural = "team_leader"
