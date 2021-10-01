from django import forms
from hotel.cancellation_policy.models import Cancellation_Policy


class CancellationForm(forms.ModelForm):
    
    class Meta:
        model = Cancellation_Policy
        fields = [
            "cancellation_type_id",
            "cancellation_type",
            "hour",
            "price",
            "no_show",
            "season_start_date",
            "season_end_date",
            "day",
        ]

    class Media:
        js = ('js/cancellationType.js',)
