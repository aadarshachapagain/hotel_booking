import django_filters
from booking.booking_table.models import BookingTable


class BookingTableFilter(django_filters.FilterSet):
	booked_date = django_filters.DateFromToRangeFilter()
	
	class Meta:
		model = BookingTable
		fields = [
			'customer',
			'status',
			'booked_date',
		]
