from django import forms
from points.reward_point.models import RewardPoint



class RewardPointForm(forms.ModelForm):
    class Meta:
        model = RewardPoint
        fields = ["transaction","transaction_amount","user","booking","net_total","remark","status","created_at"]
