from django import forms
from ..models import Hotels
from .models import HotelOwner

class HotelOwnerForm(forms.ModelForm):
    class Meta:
        model = HotelOwner
        fields = ["name","contact","image","address","created_at"] 