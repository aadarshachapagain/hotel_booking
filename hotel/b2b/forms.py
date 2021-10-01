from django import forms
from hotel.b2b.models import B2B
from hotel.models import Hotels

STATUS = [
    ('True', 'Active'),
    ('False', 'Inactive'),
]


class B2BForm(forms.ModelForm):
    hotel = forms.ModelChoiceField(queryset=Hotels.objects.all(), widget=forms.Select(
        attrs={'class': "form-control custom-input-box myselect"}), )
    status = forms.CharField(widget=forms.RadioSelect(choices=STATUS))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'class': "myDatePicker"}), )
    end_date = forms.DateField(widget=forms.DateInput(attrs={'class': "myDatePicker"}), )
    group_size = forms.IntegerField(min_value=0)
    price = forms.DecimalField(min_value=0.0, label='Percentage Discount')

    class Meta:
        model = B2B
        fields = [
            "hotel",
            "third_party_name",
            "price",
            "start_date",
            "end_date",
            "group_size",
            "status",
        ]
