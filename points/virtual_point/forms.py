from django import forms
from points.virtual_point.models import VirtualPoint



class VirtualPointForm(forms.ModelForm):
    class Meta:
        model = VirtualPoint
        fields = ["transaction","transaction_amount","user","booking","net_total","remark","status","created_at"]
