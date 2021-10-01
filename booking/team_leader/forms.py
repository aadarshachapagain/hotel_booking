from django import forms

from booking.team_leader.models import TeamLeader


class TeamLeaderForm(forms.ModelForm):
	class Meta:
		model = TeamLeader
		fields = [
			"type",
			"bonus_credit_point"
		]
