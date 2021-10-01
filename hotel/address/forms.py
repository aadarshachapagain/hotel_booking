from django import forms

# from ..amenities.models import HotelAmenities
from .models import HotelAddress


class HotelAddressForm(forms.ModelForm):
    class Meta:
        model = HotelAddress
        fields = ["hotel", "city", "state", "country", "address", "contact1", "contact2",
                  "latitude", "longitude", "created_at"]


