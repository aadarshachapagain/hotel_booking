from django import forms
from hotel.models import Hotels
from hotel.specialRequest.models import specialRequest

STATUS = [
	('True', 'Active'),
	('False', 'Inactive'),
]


class specialRequestForm(forms.ModelForm):
	
	# hotel = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=Hotels.objects.all(), empty_label=None)
	status = forms.CharField(widget=forms.RadioSelect(choices=STATUS), required=False)
	item = forms.CharField(label="Special Request Item Name *", help_text="Example: Early Check-in")
	
	def __init__(self,  action, *args, **kwargs):
		super(specialRequestForm, self).__init__(*args, **kwargs)
		self.action = action
		self.name = 'multifield'
	
	# def __init__(self, hotel, action, *args, **kwargs):
	# 	super(specialRequestForm, self).__init__(*args, **kwargs)
	# 	self.fields['hotel'].initial = hotel
	# 	self.action = action
	# 	self.name = 'multifield'
	
	class Meta:
		model = specialRequest
		fields = [
			"item",
			# "hotel",
			"status"
		]
	
	class Media:
		js = ('js/hotelInventoryChildSupplement.js',)
