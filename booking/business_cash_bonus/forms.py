from django import forms

from booking.business_cash_bonus.models import BusinessCashBonus


class BusinessCashBonusForm(forms.ModelForm):
	class Meta:
		model = BusinessCashBonus
		fields = ["transaction",
		          "cash_bonus_amount",
		          "user",
		          "booking",
		          "net_total",
		          "remark",
		          "status",
		          "created_at"]
