from django import forms


class RoomFacilityAssignForm(forms.Form):
	
	class Meta:
		# model = HotelFacilitiesMiddle
		fields = [
			"roomfaclities",
			"available_checkbox",
			"price_checkbox",
			"description",
		]
