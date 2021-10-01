from django import forms

from .models import HotelReview

class HotelReviewForm(forms.ModelForm):
    class Meta:
        model = HotelReview
        fields = ["company_id",
                  "inventory_id",
                  "user_id",
                  "rating",
                  "review",
                  "module"]
