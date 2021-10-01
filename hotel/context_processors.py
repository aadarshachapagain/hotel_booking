from account.models import User
from account.staff_profile.models import StaffProfile
from booking.booking_table.models import BookingTable
from hotel.inventory.models import HotelInventory
# from rental.rental_company.models import RentalCompany
# from rental.vehicleInventory.models import VehicleInventory
# from restaurant.restaurant_company.models import RestaurantCompany
# from restaurant.restaurant_inventory.models import RestaurantInventory
from travel import settings
from .models import Hotels
from hotel.owner.models import HotelOwner


def hotelDashboard(request):
    if request.user.is_authenticated:
        usertmp = request.user.account_type.all()
        for user_account in usertmp:
            if user_account.type is not None:
                if user_account.type == 'hotel_owner' and request.user.is_verified == True:
                    user_id = request.user.id
                    if 'current_hotel' in request.COOKIES:
                        current_hotel = request.COOKIES.get("current_hotel")
                        hotels_active = Hotels.objects.filter(owner_id_id=user_id, is_active=1)
                        hotels_inactive = Hotels.objects.filter(owner_id_id=user_id, is_active=0)
                        if current_hotel != "empty":
                            # hotel_name = Hotels.objects.values_list('name', flat=True).get(id=current_hotel)
                            usertmp = request.user.account_type.all()
                            context = {
                                'ownedHotels': hotels_active,
                                'ownedHotels_inactive': hotels_inactive,
                                'hotel_name_current': '',
                                'usertmp': usertmp
                            }
                            return context
                        else:
                            usertmp = request.user.account_type.all()
                            context = {
                                'usertmp': usertmp,
                                'ownedHotels': hotels_active,
                                'ownedHotels_inactive': hotels_inactive,
                            }
                            return context
                    else:
                        context = {}
                        return context
                elif user_account.type == 'hotel_staff' and request.user.is_verified == True:
                    user_id = request.user.id
                    hotel = StaffProfile.objects.get(user_id=user_id, module='hotel')
                    hotel_name = Hotels.objects.get(id=hotel.company_id)
                    usertmp = request.user.account_type.all()
                    context = {
                        # 'hotelStaff': hotel,
                        'hotelStaff': hotel_name,
                        'usertmp': usertmp
                    }
                    return context

        else:
            context = {}
            return context
    else:
        context = {}
        return context


def approvalcount(request):
    hotels = Hotels.objects.filter(is_active=False)[:3]
    hotelscount = Hotels.objects.filter(is_active=False).count()

    data = {
        'hotelcount': hotelscount,
        'hotels': hotels
    }
    return data


def invcount(request):
    hotelsinv = HotelInventory.objects.filter(is_active=False)[:3]
    hotelsinvcount = HotelInventory.objects.filter(is_active=False).count()
    # print("hello form context ptocesor")
    # print(hotelsinvcount)
    data = {
        'hotelsinvcount': hotelsinvcount,
        'hotelsinv': hotelsinv
    }
    return data


# def rentalcount(request):
#     rental = RentalCompany.objects.filter(is_active=0)[:3]
#     rentalcount = RentalCompany.objects.filter(is_active=0).count()
#     # print("hello form context ptocesor")
#     # print(hotelsinvcount)
#     data = {
#         'rentalcount': rentalcount,
#         'rental': rental
#     }
#     return data


# def rentalinvcount(request):
#     rentalinv = VehicleInventory.objects.filter(is_verified=False)[:3]
#     rentalinvcount = VehicleInventory.objects.filter(is_verified=False).count()
#     # print("hello form context ptocesor")
#     # print(hotelsinvcount)
#     data = {
#         'rentalinvcount': rentalinvcount,
#         'rentalinv': rentalinv
#     }
#     return data


# def restaurantcount(request):
#     restaurants = RestaurantCompany.objects.filter(is_active=0)
#     restaurantcount = RestaurantCompany.objects.filter(is_active=0).count()
#     data = {
#         'restaurantcount': restaurantcount,
#         'restaurants': restaurants
#     }
#     return data


# def restaurantinvcount(request):
#     restaurantinvs = RestaurantInventory.objects.filter(is_verified=0)
#     restaurantinvscount = RestaurantInventory.objects.filter(is_verified=0).count()
#     data = {
#         'restaurantinvs': restaurantinvs,
#         'restaurantinvscount': restaurantinvscount,
#     }
#     return data

def hotelBookingCount(request):
    bookingList = BookingTable.objects.filter(seenStatus=False)
    bookingListCount = bookingList.count()
    data = {
        'bookingLists': bookingList,
        'bookingListCount': bookingListCount,
    }
    return data


def hotel_side_navigation(request):
    hotel_id = 0
    if 'hotel_id' in request.session:
        hotel_id = request.session['hotel_id']
    data = {
        'new_hotel_id': hotel_id
    }
    return data


from hotel.propertyDetail.models import PropertyDetail


def property_list(request):
    PropertyDetailList = PropertyDetail.objects.all()
    PropertyDetailList_pending_count = PropertyDetail.objects.filter(status='pending_approval').count()
    data = {
        'PropDetList': PropertyDetailList,
        'PropDet_pending_count': PropertyDetailList_pending_count,
    }
    return data
