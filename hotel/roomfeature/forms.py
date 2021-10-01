from django import forms

from .models import HotelRoomFeature


class HotelRoomFeatureForm(forms.ModelForm):
    class Meta:
        model = HotelRoomFeature
        fields = ["name", "status"]


