from django import forms
from hotel.charges.models import Charges
from hotel.Country.models import Country



class ChargesForm(forms.ModelForm):
    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        widget=forms.Select(attrs={'class': "form-control custom-input-box myselect"}),
        help_text="Select Country from dropdown below.")
    vat = forms.DecimalField(
        label='VAT',
        help_text="This value will be calculated in %")
    sc = forms.DecimalField(
        label='Service Charge(SC)',
        help_text="This value will be calculated in %")
    citytax = forms.DecimalField(
        label='City Tax',
        help_text=" This value will be calculated in%")

    class Meta:
        model = Charges
        fields = [
            "country",
            "vat",
            "sc",
            "citytax",
        ]
