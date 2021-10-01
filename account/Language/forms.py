from django import forms
from account.Language.models import Language


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ["name"]
