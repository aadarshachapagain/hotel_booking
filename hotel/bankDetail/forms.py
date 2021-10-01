from django import forms

from hotel.bankDetail.models import BankDetail


class BankDetailForm(forms.ModelForm):
    class Meta:
        model = BankDetail
        fields = [
            "bankCountry",
            "swiftCode",
            "accountName",
            "accountNumber",
            "bankName",
            "invoiceTo",
            "hotel"
        ]
