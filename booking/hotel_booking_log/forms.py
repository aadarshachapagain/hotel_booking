from django import forms
from booking.hotel_booking_log.models import HotelBookingLog


class HotelBookingLogForm(forms.ModelForm):
	class Meta:
		model = HotelBookingLog
		fields = [
			'booking',
			'staff',
			'checkin_date',
			'checkout_date',
			'status',
			'created_at'
		]
