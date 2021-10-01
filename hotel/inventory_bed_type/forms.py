from django import forms
from hotel.inventory_bed_type.models import Inventory_Bed_Type


class InventoryBedTypeForm(forms.ModelForm):
	class Meta:
		model = Inventory_Bed_Type
		fields = ["bed_type", "created_at", "inventory"]
