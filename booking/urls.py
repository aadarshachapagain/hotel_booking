from django.urls import path
from django.conf.urls import url, include

app_name = 'booking'
urlpatterns = [
	
	path('customer/', include('booking.customer.urls')),
	path('guestdetail/', include('booking.guestdetail.urls')),
	path('guestdocdetail/', include('booking.guestdocdetail.urls')),
	path('pdf/', include('booking.pdf.urls')),
	path('module/', include('booking.module_booking.urls')),
	path('hotelBookingLog/', include('booking.hotel_booking_log.urls')),
	path('booking_table/', include('booking.booking_table.urls')),
	path('reward/', include('booking.reward.urls')),
	path('api/', include('booking.api.urls')),
	path('teamLeader/', include('booking.team_leader.urls')),
	path('businessPartners/', include('booking.business_partners.urls')),
	path('membership/',include('booking.upgrade_membership.urls')),
	path('partnership/',include('booking.upgrade_partnership.urls')),
	path('points_on_sale/',include('booking.points_on_sale.urls')),
	path('business_cash_bonus/',include('booking.business_cash_bonus.urls')),
]
