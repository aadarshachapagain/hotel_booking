from django import forms

from account.passwordReset.models import PasswordReset


class PasswordResetForm(forms.ModelForm):
	class Meta:
		model = PasswordReset
		fields = ["code",
		          "user",
		          "status",
		          "created_at"]
