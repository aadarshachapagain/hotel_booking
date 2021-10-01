from django import forms
from hotel.similarSystems.models import SimilarSystems


class SimilarSystemsForm(forms.ModelForm):
    name = forms.CharField(
        label='System Name',
        help_text="Example:Booking.com")
    status = forms.BooleanField(
        label='Status',
        required=False,
    )

    class Meta:
        model = SimilarSystems
        fields = [
            "name",
            "status",
        ]
