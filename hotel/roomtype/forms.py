from django import forms
from .models import HotelRoomType


class HotelRoomTypeForm(forms.ModelForm):
	class Meta:
		model = HotelRoomType
		fields = [
			"name",
		]
