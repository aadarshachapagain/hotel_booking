from django import forms
from hotel.inventoryUpdate.models import InventoryUpdate
from hotel.inventory.models import HotelInventory
from hotel.models import Hotels

OpenorClosed = [
    ('Open', 'Open'),
    ('Closed', 'Closed'),
]


class InventoryUpdateForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'class': "myDatePicker"}), required=False,
                           label='Price applicable from')

    european_plan = forms.DecimalField(label='European Plan',
                                       widget=forms.TextInput(attrs={'placeholder': 'EP price'}),
                                       required=False
                                       )
    bedandbreakfast_plan = forms.DecimalField(label='Bed & Breakfast Plan',
                                              widget=forms.TextInput(attrs={'placeholder': 'BB price'}),
                                              required=False
                                              )
    quantity = forms.IntegerField(
        label='Quantity',
        required=False,
    )

    status = forms.ChoiceField(widget=forms.Select(
        attrs={'class': "form-control custom-input-box myselect"}), choices=OpenorClosed, label='Status',
        required=False)

 
    class Meta:
        model = InventoryUpdate
        fields = [
            "hotel",
            "inventory",
            "date",
            "quantity",
            "european_plan",
            "bedandbreakfast_plan",
            "status",

        ]

        widgets = {
            'inventory': forms.HiddenInput(),
            'hotel': forms.HiddenInput()
        }
