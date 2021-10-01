from django import forms
from django.forms import formset_factory
from .models import InventoryGallery


class InventoryGalleryForm(forms.ModelForm):
    class Meta:
        model = InventoryGallery
        fields = ["hotel_inventory_id", "image", "title"]
