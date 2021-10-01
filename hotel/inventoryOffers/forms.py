from django import forms
from hotel.inventoryOffers.models import InventoryOffers


class InventoryOffersForm(forms.ModelForm):
    class Meta:
        model = InventoryOffers
        fields = [
            "hotel_inventory",
            "offer",
            "status",
            "created_at"
        ]
