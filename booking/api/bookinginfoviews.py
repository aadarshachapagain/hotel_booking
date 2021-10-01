from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from account.models import User
from account.owner_profile.models import OwnerProfile
from hotel.models import Hotels
from hotel.address.models import HotelAddress

# from rental.rental_company.models import RentalCompany
# from rental.rental_company_address.models import RentalCompanyAddress
# from restaurant.restaurant_company.models import RestaurantCompany
# from restaurant.restaurant_company_address.models import RestaurantCompanyAddress
# from travel_tour.tour_company.models import TravelCompany
# from travel_tour.tour_company_address.models import TourCompanyAddress
from booking.module_booking.models import ModuleBooking
from booking.booking_table.models import BookingTable
from booking.customer.models import Customer
# from listing.api.serializers import listedPropSerializer
# from listing.api.serializers import BookingDetailSerializer
from hotel.inventory.models import HotelInventory
from django.forms import model_to_dict
from rest_framework.authtoken.models import Token
from booking.api.serializers import BookingDetailForUserSerializer


class BookingDetailForUser:
    def __init__(self, id=0, moduleName='', propName='', type='', checkin='', checkout='', customer='', created_at='',
                 address='', lat='', long='', contact='', booking_id=0):
        self.id = id
        self.moduleName = moduleName
        self.propName = propName
        self.type = type
        self.checkin = checkin
        self.checkout = checkout
        self.customer = customer
        self.created_at = created_at
        self.address = address
        self.lat = lat
        self.long = long
        self.contact = contact
        self.booking_id = booking_id


@csrf_exempt
def booking_tilldate(request):
    if request.method == "POST":
        dict_listedprop = {}
        attempted_booking = []
        token_user = request.POST.get('token_user')
        user_id = Token.objects.get(key=token_user).user_id
        bookedByUser = ModuleBooking.objects.filter(module_name='hotel', customer_id=user_id)

        for bbu in bookedByUser:
            inv_instance = HotelInventory.objects.get(id=bbu.inventory_id)
            hotel_name = inv_instance.hotel.name
            hotel_id = inv_instance.hotel.id
            inv_name = inv_instance.room_name

            if user_id:
                obj = BookingDetailForUser()
                obj.moduleName = bbu.module_name
                obj.id = bbu.id
                obj.propName = hotel_name
                obj.type = inv_name
                obj.booking_id = bbu.booking_id
                obj.checkin = bbu.start_date
                obj.created_at = bbu.created_at
                obj.checkout = bbu.end_date
                customer_name = Customer.objects.get(user_id=bbu.customer_id)
                obj.customer = customer_name
                obj.address = HotelAddress.objects.get(hotel_id=hotel_id).address
                obj.lat = HotelAddress.objects.get(hotel_id=hotel_id).latitude
                obj.long = HotelAddress.objects.get(hotel_id=hotel_id).longitude
                obj.contact = HotelAddress.objects.get(hotel_id=hotel_id).contact1
                serializer = BookingDetailForUserSerializer(obj)
                attempted_booking.append(serializer.data)
        return JsonResponse(attempted_booking, safe=False)


# from rest_framework import serializers


# class BookingDetailForUserSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     moduleName = serializers.CharField(max_length=200)
#     propName = serializers.CharField(max_length=200)
#     type = serializers.CharField(max_length=200)
#     checkin = serializers.DateField()
#     checkout = serializers.DateField()
#     customer = serializers.CharField(max_length=200)
#     created_at = serializers.DateTimeField()
#     address = serializers.CharField(max_length=200)
#     contact = serializers.CharField(max_length=200)
#     lat = serializers.CharField(max_length=200)
#     long = serializers.CharField(max_length=200)
#     booking_id = serializers.IntegerField()
