from django.db import models


class FAQ(models.Model):
	question = models.TextField(blank=True, null=True)
	answer = models.TextField(blank=True, null=True)
	device = models.CharField(max_length=200,blank=True, null=True)
	
	class Meta:
		verbose_name_plural = "FAQs"
