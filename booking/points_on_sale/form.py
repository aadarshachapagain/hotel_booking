from django import forms
from booking.reward.models import Reward
from booking.points_on_sale.models import PointsOnSale


class PointsOnSaleForm(forms.ModelForm):
    class Meta:
        model = PointsOnSale
        fields = [
            "virtualpoint",
            "credit_point",
            "sale_type",
        ]
