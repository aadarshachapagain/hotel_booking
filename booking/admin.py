from django.contrib import admin

from booking.module_booking.models import ModuleBooking
from booking.booking_table.models import BookingTable
from booking.reward.models import Reward

from booking.customer.models import Customer
from booking.guestdetail.models import GuestDetail
from booking.guestdocdetail.models import GuestDocDetail
from booking.team_leader.models import TeamLeader
from booking.points_on_sale.models import PointsOnSale
from booking.business_partners.models import BusinessPartners
from booking.referee_and_referred.models import RefereeAndReferred
from booking.business_cash_bonus.models import BusinessCashBonus
from booking.hotel_booking_log.models import HotelBookingLog


# Register your models here.

admin.site.register(Customer)
admin.site.register(GuestDetail)
admin.site.register(GuestDocDetail)


admin.site.register(ModuleBooking)
admin.site.register(BookingTable)
admin.site.register(Reward)

admin.site.register(TeamLeader)
admin.site.register(PointsOnSale)
admin.site.register(BusinessPartners)
admin.site.register(RefereeAndReferred)
admin.site.register(BusinessCashBonus)
admin.site.register(HotelBookingLog)
