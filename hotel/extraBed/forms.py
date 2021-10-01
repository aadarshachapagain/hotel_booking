from django import forms
from hotel.extraBed.models import ExtraBedPolicy
from hotel.models import Hotels

UNIT = [
	('per person per night', 'per person per night'),
	('per person per stay', 'per person per stay'),
]

CATEGORY = [
	('From', 'From'),
	('Up To', 'Up To'),
	('Over', 'Over'),
	('Any', 'Any'),
	('Adult', 'Adult'),
]

PRICE = [
	('Free', 'Free'),
	('Percentage', 'Percentage'),
]

AGE = [
	('0', '0'),
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
	('6', '6'),
	('7', '7'),
	('8', '8'),
	('9', '9'),
	('10', '10'),
	('11', '11'),
	('12', '12'),
	('13', '13'),
	('14', '14'),
	('15', '15'),
	('16', '16'),
	('17', '17'),
	('Adult (18 +)', 'Adult (18 +)')
]

Day = (
	('Sunday', 'Sunday'),
	('Monday', 'Monday'),
	('Tuesday', 'Tuesday'),
	('Wednesday', 'Wednesday'),
	('Thursday', 'Thursday'),
	('Friday', 'Friday'),
	('Saturday', 'Saturday')
)

class ExtraBedPolicyForm(forms.ModelForm):
	hotel = forms.ModelChoiceField(widget=forms.HiddenInput, queryset=Hotels.objects.all(), empty_label=None)
	unit = forms.ChoiceField(widget=forms.Select(
		attrs={'class': "form-control custom-input-box myselect"}), choices=UNIT, label='Price', required=False)
	age_category = forms.ChoiceField(widget=forms.Select(
		attrs={'class': "form-control custom-input-box myselect"}), choices=CATEGORY, label='Age')
	age_start = forms.ChoiceField(widget=forms.Select(
		attrs={'class': "form-control custom-input-box myselect"}), choices=AGE, label='Age')
	age_end = forms.ChoiceField(widget=forms.Select(
		attrs={'class': "form-control custom-input-box myselect"}), choices=AGE, label='Age',required=False)
	cost_status = forms.ChoiceField(widget=forms.Select(
		attrs={'class': "form-control custom-input-box myselect"}), choices=PRICE, label='Price')
	cost = forms.DecimalField(label='Price',widget=forms.TextInput(attrs={'style':'height:28px'}), required=False )
	season_start_date = forms.DateField(widget=forms.DateInput(attrs={'class': "myDatePicker"}), required=False,
	                                    label='Policy applicable from?')
	season_end_date = forms.DateField(widget=forms.DateInput(attrs={'class': "myDatePicker"}), required=False,
	                                  label='Policy applicable till?')
	day = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class': 'customDay'}), choices=Day,
	                                label='Select days if this policy is applicable on day basis.', required=False, )
	
	def __init__(self, hotel,action ,*args, **kwargs):
		super(ExtraBedPolicyForm, self).__init__(*args, **kwargs)
		self.fields['hotel'].initial = hotel
		self.fields['cost'].initial = 0
		self.name = 'childSupplementForm'
		self.action = action
	
	
	
	class Meta:
		model = ExtraBedPolicy
		fields = [
			"age_category",
			"age_start",
			"age_end",
			"cost_status",
			"cost",
			"unit",
			"hotel",
			"season_start_date",
			"season_end_date",
			"day"
		]
		
		
	class Media:
		js = ('js/hotelInventoryChildSupplement.js',)
