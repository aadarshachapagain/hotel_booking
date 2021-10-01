from django import forms

from booking.guestdetail.models import GuestDetail
from booking.guestdocdetail.models import GuestDocDetail



class GuestDocDetailForm(forms.ModelForm):
    class Meta:
        model = GuestDocDetail
        fields = [
            "document_type",
            "status",
            "document_number",
            "issuing_country",
            "doc_file",
            "visa_required",
            "visa_expiry",
            "guest_detail",
            "created_at",
        ]
