from django import forms
from hotel.mealPlan.models import MealPlan



class MealPlanForm(forms.ModelForm):
    plan = forms.CharField(
        label='Plan Name',
        help_text="Example:BB or EP")
    full_form = forms.CharField(
        label='Full Form',
        help_text="Example:Bed And Breakfast",
        required=False
    )
    status = forms.BooleanField(
        label='Status',
        required=False,
    )

    class Meta:
        model = MealPlan
        fields = [
            "plan",
            "full_form",
            "status",
        ]
