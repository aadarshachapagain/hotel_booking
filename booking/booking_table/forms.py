from django import forms
from booking.booking_table.models import BookingTable

class BookingTableForm(forms.ModelForm):
    class Meta:
        model = BookingTable
        fields = [
            "payment_method",
            "payment_status",
            "payment_type",
            "total_price",
            "total_discount",
            "total_tax",
            "booked_date",
            "status",
            "customer",
            "created_at",
            "seenStatus",
            "special_request"
        ]
