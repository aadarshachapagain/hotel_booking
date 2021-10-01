from django import forms
from hotel.favourites_saved.models import Favourites


class FavouritesForm(forms.ModelForm):
    class Meta:
        model = Favourites
        fields = [
            "user",
            "module",
            "company_id",
            "inventory_id",
            "favourite",
            "saved",
        ]

