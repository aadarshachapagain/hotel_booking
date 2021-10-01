from django import forms
from hotel.offers.models import Offers


class OffersForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = [
            "offer_name",
            "description",
            "status",
            "start_date",
            "end_date",
            "banner_image",
            "rate",
            "module",
            "creator"
        ]
