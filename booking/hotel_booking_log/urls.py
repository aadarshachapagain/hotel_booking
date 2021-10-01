from django.urls import path, include
from booking.hotel_booking_log import views

urlpatterns = [
	path('delete/<int:pk>', views.HotelBookingLogDelete.as_view(), name="hotel-booking-log-delete"),
	path('<int:pk>', views.HotelBookingLogView.as_view(), name="hotel-booking-log"),
	path('create/', views.HotelBookingLogCreate.as_view(), name="hotel-booking-log-create"),
	path('show/<int:pk>', views.HotelBookingLogDetail.as_view(), name="hotel-booking-log-show"),
	path('update/<int:pk>', views.HotelBookingLogUpdate.as_view(), name="hotel-booking-log-update"),
]
