from django import forms

from .models import HotelFacilities
from hotel.models import HotelFacilitiesMiddle


class HotelFacilitiesForm(forms.ModelForm):
    class Meta:
        model = HotelFacilities
        fields = ["name", "image", "created_at", "category"]

        def clean_name(self):
            return self.cleaned_data["name"].upper()


class HotelFeatureForm(forms.Form):
    price = forms.DecimalField(required=False)

    class Meta:
        # model = HotelFacilitiesMiddle
        fields = [
            "featureexists",
            "hotels",
            "hotelsfacilities",
            "freeorpaid",
            "description",
            "price",
            "isrecomended",
        ]

        # def clean_name(self):
        #     return self.cleaned_data["name"].upper()
