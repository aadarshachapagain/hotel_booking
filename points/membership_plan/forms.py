from django import forms
from points.membership_plan.models import Membership_plan


class Membership_planForm(forms.ModelForm):
    class Meta:
        model = Membership_plan
        fields = [
            "type",
            "purchase_price",
            "renewal_cost",
            "reward_point",
            "maturity_time",
            "renewal_cond",
            "expiry_cond",
            "reward_point",
            "virtual_point",
            "virtual_point_for_old",
            "credit_point_for_old",
            "upgrade_reward_point",
            "position",
            "created_at",
            "status",
        ]

