from django import forms

from .models import HotelBooking

class HotelBookingForm(forms.ModelForm):
    class Meta:
        model = HotelBooking
        fields = ["hotelinventory_id", "user_id", "checkin_date", "checkout_date",
                  "price", "no_of_adult", "no_of_room", "pay_mode", "pay_status","no_of_child"]
