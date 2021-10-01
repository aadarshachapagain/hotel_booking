from django import forms
from points.credit_point.models import CreditPoint



class CreditPointForm(forms.ModelForm):
    class Meta:
        model = CreditPoint
        fields = ["transaction","transaction_amount","user","booking","net_total","remark","status","created_at"]
