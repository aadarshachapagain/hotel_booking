from django import forms
from .models import Landmark


class LandmarkForm(forms.ModelForm):
    class Meta:
        model = Landmark
        fields = [
            # "image",
            "name",
            "latitude",
            "longitude"
            # "city"
        ]
