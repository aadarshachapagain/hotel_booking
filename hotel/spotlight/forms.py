from django import forms

# from ..amenities.models import HotelAmenities
from .models import Spotlight



class SpotlightForm(forms.ModelForm):
    class Meta:
        model = Spotlight
        fields = [
            "hotel",
            "start_date",
            "end_date",
            "nameofdepositor",
            "price",
            "contact1",
            "status",
            "created_at"
        ]
