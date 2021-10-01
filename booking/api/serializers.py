from django.template.base import Token
from account.models import User
from booking.booking_table.models import BookingTable
from booking.customer.models import Customer
from rest_framework.authtoken.models import Token

from rest_framework.serializers import (
	CharField,
	EmailField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError
)

# for customer profile
from booking.guestdetail.models import GuestDetail
from booking.guestdocdetail.models import GuestDocDetail


class CustomerProfileSerializer(ModelSerializer):
	class Meta:
		model = Customer
		# fields required to return back
		fields = [
			"name",
			"contact",
			"status",
			"address",
			"country",
			# "state",
			# "city",
			"gender",
			"dob",
			"image",
			"reward",
			# "user",
			# "token"
		]


# for customer profile

# for guest detail
class GuestDetailSerializer(ModelSerializer):
	class Meta:
		model = GuestDetail
		# fields required to return back
		fields = [
			"name",
			"email",
			"contact",
			"status",
			"address",
			"country",
			"state",
			"city",
			"gender",
			"dob",
			"booking",
			"customer"
		]


# for guest detail

# for guest document detail
class GuestDocDetailSerializer(ModelSerializer):
	class Meta:
		model = GuestDocDetail
		# fields required to return back
		fields = [
			"document_type",
			"status",
			"document_number",
			"issuing_country",
			"doc_file",
			"visa_required",
			"visa_expiry",
			"guest_detail"
		]
# for guest document detail


# for payment
class PaymentSerializer(ModelSerializer):
	class Meta:
		model = BookingTable
		# fields required to return back
		fields = [
			"payment_method",
			"payment_status",
			"payment_type",
			"total_price",
			"total_discount",
			"total_tax",
			"booked_date",
			"status",
			"customer",
		]
# for payment



from rest_framework import serializers

class BookingDetailForUserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    moduleName = serializers.CharField(max_length=200)
    propName = serializers.CharField(max_length=200)
    type = serializers.CharField(max_length=200)
    checkin = serializers.DateField()
    checkout = serializers.DateField()
    customer = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField()
    address = serializers.CharField(max_length=200)
    contact = serializers.CharField(max_length=200)
    lat = serializers.CharField(max_length=200)
    long = serializers.CharField(max_length=200)
    booking_id = serializers.IntegerField()
