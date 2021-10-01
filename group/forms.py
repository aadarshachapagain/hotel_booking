from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class GroupForm(forms.ModelForm):
	class Meta(UserCreationForm.Meta):
		model = Group
		fields = (
			"name",
			"permissions"
		)
