from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime
from django.core.files.storage import FileSystemStorage


from account.owner_profile.models import OwnerProfile
# from ..owner.models import HotelOwner
from hotel.models import Hotels
from account.models import User


class StaffProfile(models.Model):
	name = models.CharField(max_length=80, blank=True,null=True)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
	                             message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	contact = models.CharField(validators=[phone_regex], max_length=17, blank=True,null=True)  # validators should be a list
	# email = models.EmailField(unique=True)
	# password = models.CharField(max_length = 30)
	image = models.ImageField(default='default.png')
	address = models.CharField(max_length=80, blank=True,null=True)
	module = models.CharField(max_length=80, blank=True,null=True)
	owner = models.ForeignKey(OwnerProfile, on_delete=models.CASCADE, null=True)
	company_id = models.IntegerField(null=True)
	# hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE,null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	
	def __str__(self):
		return self.name
	
	def delete(self, *args, **kwargs):
		self.image.delete()
		super().delete(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Staff Profile"
