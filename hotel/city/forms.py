from django import forms
from .models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = [
            "country",
            "name",
            "state",
            "image",
            "latitude",
            "longitude",
        ]
