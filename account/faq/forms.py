from django import forms

from account.faq.models import FAQ


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = [
            "answer",
            "question",
            "device"
        ]
