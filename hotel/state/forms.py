from django import forms
from .models import State


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ["name","country"]
