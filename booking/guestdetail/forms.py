from django import forms

from booking.guestdetail.models import GuestDetail



class GuestDetailForm(forms.ModelForm):
    class Meta:
        model = GuestDetail
        fields = [
            "name",
            "email",
            "contact",
            "status",
            "country",
            "created_at",
            "customer",
            "parent_status",
            "parent"
        ]
