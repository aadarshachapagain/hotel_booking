from django import forms
from booking.reward.models import Reward

class RewardForm(forms.ModelForm):
    class Meta:
        model = Reward
        fields = [
            "reward_type",
            "total_reward",
            "status",
            "customer",
            "booking",
            "created_at"
        ]
