import json
from decimal import Decimal
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from rest_framework import pagination
from rest_framework.response import Response

from booking.api.views import shouldsendinv
from booking.module_booking.models import ModuleBooking
from booking.utils import check_booking_available
from hotel.address.models import HotelAddress
from hotel.city.models import City
from hotel.inventory.models import HotelInventory
from hotel.models import Hotels


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)


class FirstPackageList:

    def __init__(self, Package):
        self.best_time = self.to_array(Package.best_time)
        self.description = Package.description
        self.name = Package.package_name
        self.banner_image = Package.banner_image.url
        self.tour_cost = json.dumps(Decimal(Package.tour_cost), cls=DecimalEncoder)
        self.start_city = Package.start_city.name
        self.distination_city = Package.distination_city.name
        self.day_count = Package.day_count
        self.night_count = Package.night_count
        self.group_size = Package.group_size
        self.company = Package.company.name

        galleries = Package.travelPackage.filter()
        self.gallery = []
        for gallery in galleries:
            temp = PackageGallery(gallery)
            self.gallery.append(temp)

        itinerary = Package.iternary.filter()
        self.itinerary = []
        for i in itinerary:
            temp = PackageItinerary(i)
            self.itinerary.append(temp)

        included = Package.included.filter()
        self.included = []
        for i in included:
            temp = PackageInclude(i)
            self.included.append(temp)

        exclude = Package.excluded.filter()
        self.exclude = []
        for e in exclude:
            temp = PackageExclude(e)
            self.exclude.append(temp)

        theme = Package.theme.filter()
        self.theme = []
        for t in theme:
            temp = PackageTheme(t)
            self.theme.append(temp)

        addonhotels = Package.addonhotel.filter()
        self.addonhotels = []
        for addonhotel in addonhotels:
            temp = PackageAddOnHotel(addonhotel)
            self.addonhotels.append(temp)

        addtransports = Package.addtransport.filter()
        self.addtransports = []
        for addtransport in addtransports:
            temp = PackageAddOnTransportation(addtransport)
            self.addtransports.append(temp)

        addon_activities = Package.addon_actvities.filter()
        self.addon_activities = []
        for addon_activity in addon_activities:
            temp = PackageAddOnActivities(addon_activity)
            self.addon_activities.append(temp)

        addon_cuisine = Package.addon_cuisine.filter()
        self.addon_cuisine = []
        for addon_food in addon_cuisine:
            temp = PackageAddOnCuisine(addon_food)
            self.addon_cuisine.append(temp)

        facilities = Package.facilities.filter()
        self.facilities = []
        for facility in facilities:
            temp = PackageFacilities(facility)
            self.facilities.append(temp)

    def __str__(self):
        return self.name

    def to_array(self, text):
        value = text.split(",")
        return value


class PackageGallery:

    def __init__(self, Gallery):
        self.image = Gallery.image.url
        self.title = Gallery.title

    def __str__(self):
        return self.title


class PackageItinerary:

    def __init__(self, Itinerary):
        self.day = Itinerary.day
        self.description = Itinerary.description
        self.image = Itinerary.image.url

    def __str__(self):
        return self.day


class PackageInclude:

    def __init__(self, Include):
        self.description = Include.description

    def __str__(self):
        return self.description


class PackageTheme:

    def __init__(self, Theme):
        self.title = Theme.title
        self.image = Theme.image.url

    def __str__(self):
        return self.title


class PackageExclude:

    def __init__(self, Exclude):
        self.description = Exclude.description

    def __str__(self):
        return self.description


class PackageAddOnHotel:

    def __init__(self, addonhotels):
        self.name = addonhotels.name
        self.description = addonhotels.description
        self.price = json.dumps(Decimal(addonhotels.price), cls=DecimalEncoder)

    def __str__(self):
        return self.name


class PackageAddOnTransportation:

    def __init__(self, addtransports):
        self.name = addtransports.name
        self.description = addtransports.description
        self.price = json.dumps(Decimal(addtransports.price), cls=DecimalEncoder)

    def __str__(self):
        return self.name


class PackageAddOnActivities:

    def __init__(self, addon_activities):
        self.name = addon_activities.name
        self.description = addon_activities.description
        self.price = json.dumps(Decimal(addon_activities.rate), cls=DecimalEncoder)

    def __str__(self):
        return self.name


class PackageAddOnCuisine:

    def __init__(self, addon_cuisine):
        self.name = addon_cuisine.name
        self.description = addon_cuisine.description
        self.price = json.dumps(Decimal(addon_cuisine.rate), cls=DecimalEncoder)

    def __str__(self):
        return self.name


class PackageFacilities:

    def __init__(self, facility):
        self.name = facility.name
        self.image = facility.image.url

    def __str__(self):
        return self.name


def convert_to_dict(obj):
    """
    A function takes in a custom object and returns a dictionary representation of the object.
    This dict representation includes meta data such as the object's module and class names.
    """

    #  Populate the dictionary with object meta data
    obj_dict = {
        # "__class__": obj.__class__.__name__,
        # "__module__": obj.__module__
    }

    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)

    return obj_dict


def paginate(clist, limit, page):
    datacount = len(clist)
    paginator = Paginator(clist, limit)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # return HttpResponse('Sorry requested page is not available:')
        objects = paginator.page(1)
    except EmptyPage:
        return False
    # return HttpResponse('Sorry requested page is not available:')
    # objects = paginator.page(paginator.num_pages)
    data = {
        'previous_page': objects.has_previous() and objects.previous_page_number() or None,
        'next_page': objects.has_next() and objects.next_page_number() or None,
        'totaldatacount': datacount,
        'data': list(objects),
    }
    return data



def getMatchingInventory(location, checkin, checkout,  no_child, no_adult, no_infant):
    arr = []
    dept = []
    room = []
    flag = []
    check_array = []
    check_room_array = []
    semi_room_array = []
    in_booking = []
    total_inv = []
    location = location
    check_in = checkin
    check_out = checkout
    child_max = no_child
    adult_max =  no_adult
    infant_max = no_infant
    final_invs = []
    final_rooms = []
    module_name = 'hotel'
    
    # access address table to filter location
    print("location")
    print(location)
    try:
        city_instance = City.objects.get(name=location)
    except City.DoesNotExist:
        return final_invs , final_rooms
    
    address_count = HotelAddress.objects.filter(city=city_instance.id).count()
    
    if address_count > 0:
        # get hotel id
        matching_hotel_count = HotelAddress.objects.filter(city=city_instance.id).count()
        
        if matching_hotel_count > 0:
            matching_hotel_instance = HotelAddress.objects.filter(city=city_instance.id)
            for hotel_instance in matching_hotel_instance:
                # filter by adult_max and child_max
                inventory_count = HotelInventory.objects.filter(hotel=hotel_instance.hotel_id).count()
                
                if inventory_count > 0:
                    inventory_instance = HotelInventory.objects.filter(hotel=hotel_instance.hotel_id)
                    for inventory in inventory_instance:
                        min_room_required = shouldsendinv(queryadult=adult_max, queryinfant=infant_max,
                                                          querychild=child_max, inv_id=inventory.pk)
                        temp_1 = inventory_instance.filter(no_of_rooms__gte=min_room_required)
                        
                    for inventory in temp_1:
                        total_inv.append(inventory.pk)
                        company_id = inventory.hotel.id
                        inventory_id = inventory.pk
                        booking_count = ModuleBooking.objects.filter(module_name=module_name,
                                                                     company_id=company_id,
                                                                     inventory_id=inventory_id).count()
                        
                        if booking_count > 0:
                            # for same inventory use booking algorithm
                            booking_instance = ModuleBooking.objects.filter(module_name=module_name,
                                                                            company_id=company_id,
                                                                            inventory_id=inventory_id)
                            
                            for instance in booking_instance:
                                in_booking.append(instance.inventory_id)
                                arr.append(instance.start_date.strftime('%Y-%m-%d'))
                                dept.append(instance.end_date.strftime('%Y-%m-%d'))
                                room.append(instance.quantity)
                                flag.append(1)
                            
                            arr.append(check_in)
                            dept.append(check_out)
                            flag.append(0)
                            # room.append(int(quantity))
                            room.append(min_room_required)
                            n = len(arr)
                            inventory_instance = HotelInventory.objects.get(hotel=company_id, id=inventory_id)
                            k = inventory_instance.no_of_rooms
                            available_room_count=check_booking_available(arr, dept, n, k, room, flag)
                            if available_room_count:
                                arr = []
                                dept = []
                                room = []
                                check_array.append(inventory_id)
                                check_room_array.append(available_room_count)
                            else:
                                arr = []
                                dept = []
                                room = []
            
            final_invs = list(set(total_inv).symmetric_difference(set(in_booking)))
            for invs in final_invs:
                room = HotelInventory.objects.get(id = invs)
                semi_room_array.append(room.no_of_rooms)
            final_invs = final_invs + check_array
            final_rooms = semi_room_array + check_room_array
            return final_invs , final_rooms
        else:
            return final_invs , final_rooms
    else:
        return final_invs , final_rooms


class MyBookingList:
    
    def __init__(self, Booking):
        self.id = Booking.id
        self.booked_date = Booking.booked_date.strftime('%Y-%m-%d')
        self.total_amount = json.dumps(Decimal(Booking.total_price), cls=DecimalEncoder)
        self.discount = json.dumps(Decimal(Booking.total_discount), cls=DecimalEncoder)
        self.tax = json.dumps(Decimal(Booking.total_tax), cls=DecimalEncoder)
        self.payment_method = Booking.payment_method
        self.payment_type = Booking.payment_type
        self.payment_status = Booking.payment_status
        self.status = Booking.status
        self.customer_name = Booking.customer.name
        
        modules = Booking.module_booking.filter()
        self.modules = []
        for module in modules:
            temp = Modules(module)
            self.modules.append(temp)
    
    def __str__(self):
        return self


class Modules:
    
    def __init__(self, module):
        self.module_name = module.module_name
        self.quantity = module.quantity
        self.start_date = module.start_date.strftime('%Y-%m-%d')
        self.end_date = module.end_date.strftime('%Y-%m-%d')
        self.sub_total = json.dumps(Decimal(module.sub_total), cls=DecimalEncoder)
        self.discount = json.dumps(Decimal(module.discount), cls=DecimalEncoder)
        self.tax = json.dumps(Decimal(module.tax), cls=DecimalEncoder)
        self.company_name = Hotels.objects.get(id=module.company_id).name
        self.inventory_name = HotelInventory.objects.get(id=module.inventory_id).room_name
    
    def __str__(self):
        return self.module_name


