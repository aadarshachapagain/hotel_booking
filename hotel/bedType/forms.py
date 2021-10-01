from django import forms
from hotel.bedType.models import BedType


class BedTypeForm(forms.ModelForm):
    class Meta:
        model = BedType
        fields = [
            "name",
            "description",
            "count",
            "roomtype",
            "status"
        ]
