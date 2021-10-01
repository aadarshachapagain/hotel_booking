from django import forms
from hotel.CommissionPaymentPolicies.models import CommissionPaymentPolicies


class CommissionPaymentPoliciesForm(forms.ModelForm):
	class Meta:
		model = CommissionPaymentPolicies
		fields = [
			"hotel",
			"commission_percentage",
			"invoice_name",
			"primary_address",
			"alternative_address",
			"created_at",
		]
	

