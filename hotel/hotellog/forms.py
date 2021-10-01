from django import forms

from .models import HotelLog

class HotelLogForm(forms.ModelForm):
    class Meta:
        model = HotelLog
        fields = [ "user_id", "logs", "created_at"]
