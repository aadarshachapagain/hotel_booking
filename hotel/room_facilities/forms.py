from django import forms
from .models import RoomFacilities


class RoomFacilitiesForm(forms.ModelForm):
    class Meta:
        model = RoomFacilities
        fields = [
            "name",
            "image",
            "created_at",
            "chargeable",
            "category"
        ]
