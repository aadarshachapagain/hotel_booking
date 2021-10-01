from django import forms

# from ..amenities.models import HotelAmenities
from .models import AddOnServices


class AddOnServicesForm(forms.ModelForm):
    class Meta:
        model = AddOnServices
        fields = [
            "price",
            "flatorpercent",
            "inventory",
            "amenities",
            "is_recommended",
            "status"
        ]
