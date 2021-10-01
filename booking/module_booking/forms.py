from django import forms
from booking.module_booking.models import ModuleBooking

class ModuleBookingForm(forms.ModelForm):
    class Meta:
        model = ModuleBooking
        fields = [
            "module_name",
            "quantity",
            "start_date",
            "end_date",
            "sub_total",
            "discount",
            "tax",
            "status",
            "company_id",
            "inventory_id",
            'booking',
            "created_at"
        ]
