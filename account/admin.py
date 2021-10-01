from django.contrib import admin

from account.staff_profile.models import StaffProfile
from .models import User,Account_Type
from account.owner_profile.models import OwnerProfile
from account.passwordReset.models import PasswordReset

# Register your models here.

admin.site.register(User)
admin.site.register(Account_Type)
admin.site.register(OwnerProfile)
admin.site.register(StaffProfile)
admin.site.register(PasswordReset)

# Register your models here.
