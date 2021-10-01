from django import forms
from hotel.PaymentPolicies.models import PaymentPolicies


class PaymentPoliciesForm(forms.ModelForm):
	class Meta:
		model = PaymentPolicies
		fields = [
			"hotel",
			"created_at",
			"credit_card"
		]
	

