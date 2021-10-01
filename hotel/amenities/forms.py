from django import forms

from .models import HotelAmenities


class HotelAmenityForm(forms.ModelForm):
    class Meta:
        model = HotelAmenities
        fields = ["name","category" ,"image", "created_at"]

