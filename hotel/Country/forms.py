from django import forms
from .models import Country


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            "name",
            "code",
            "country_code",
            "currency_code",
            "latitude",
            "longitude"
        ]
