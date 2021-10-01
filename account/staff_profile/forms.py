from django import forms
# from ..amenities.models import HotelAmenities
from .models import StaffProfile


class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ["name","contact","image","address","created_at"]