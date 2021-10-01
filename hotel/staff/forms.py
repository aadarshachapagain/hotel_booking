from django import forms
from ..models import Hotels
# from ..amenities.models import HotelAmenities
from .models import HotelStaff

class HotelStaffForm(forms.ModelForm):
    class Meta:
        model = HotelStaff
        fields = ["name","contact","image","address","owner_id","created_at"] 