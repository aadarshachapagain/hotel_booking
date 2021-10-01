from django.db.models import Min
from django.forms import model_to_dict
from django.http import JsonResponse

from account.Language.models import Language
from booking.customer.models import Customer
from hotel.address.models import HotelAddress
from hotel.amenities.models import HotelAmenities
from hotel.gallery.models import HotelGallery
from hotel.hotel_facilities.models import HotelFacilities
from hotel.inventory.models import HotelInventory
import json
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
import decimal

from hotel.inventory_bed_type.models import Inventory_Bed_Type
from hotel.inventorygallery.models import InventoryGallery
from hotel.landmark.models import Landmark
from hotel.models import Hotels
from hotel.reviews.models import HotelReview
from hotel.roomfeature.models import HotelRoomFeature
from hotel.roomtype.models import HotelRoomType


def check_booking_available(arr, dept, n, k, room, flag):
    # sort arrival and departure array for easy search
    ans = []
    final_array = []
    temp_var = 0
    check_out = "0"
    check_in = "0"
    for i in range(0, n):
        if flag[i] == 0:
            ans.append((arr[i], 1, 0, room[i]))
            check_in = arr[i]
            ans.append((dept[i], 0, 2, room[i]))
            check_out = dept[i]
        elif flag[i] == 1:
            ans.append((arr[i], 1, 1, room[i]))
            ans.append((dept[i], 0, 1, room[i]))

    # sort
    ans.sort()
    curr_active, max_active, = 0, 0
    max_active_after_ci = []
    flag = 0

    for i in range(0, len(ans)):
        if ans[i][1] == 1:
            curr_active = curr_active + ans[i][3]
            max_active = max(max_active, curr_active)
        else:
            curr_active = curr_active - ans[i][3]

    if k >= max_active:
        for i in range(0, n - 1):
            if dept[i] > check_in and arr[i] < check_out:
                max_active_after_ci.append((arr[i], 1, room[i]))
                temp_room = -1 * room[i]
                max_active_after_ci.append((dept[i], 0, temp_room))
                max_active_after_ci.sort()

            else:
                final_array.append(0)
        # max_active_after_ci.insert(0,0)
        for j in range(0, len(max_active_after_ci)):
            temp_var = max_active_after_ci[j][2] + temp_var
            final_array.append(temp_var)
        return k - max(final_array)
    else:
        return 0


def InventoryDetail(hotel_id, inventory_id):
    # inventory_id = request.POST.get('inventory')
    # hotel_id = request.POST.get('hotel')
    inventory = {}
    custom_bed = []
    parent_gallery = []
    parent_inventory = []
    parent_facilities = []
    parent_room_facilities = []
    parent_room_type = []
    bed_type = []
    inv_count = HotelInventory.objects.filter(id=inventory_id, hotel=hotel_id).count()
    print('count')
    print(inv_count)
    if inv_count > 0:
        inventory_basic = HotelInventory.objects.get(id=inventory_id, hotel=hotel_id)
        inv_id = inventory_basic.id
        dict_inventory = model_to_dict(inventory_basic)
        del dict_inventory['priceforadult']
        del dict_inventory['amenities']
        del dict_inventory['roomfeatures']
        del dict_inventory['hoteladdress']
        del dict_inventory['roomtype']
        del dict_inventory['created_at']
        del dict_inventory['image']
        dict_inventory.update({'priceforadult': json.loads(inventory_basic.priceforadult)})
        dict_inventory.update({'main_image': inventory_basic.image.url})

        # for review
        reviews = HotelReview.objects.filter(inventory_id=inv_id)
        parent_reviews = []
        if reviews:
            for review in reviews:
                dict_review = model_to_dict(review)
                customer = Customer.objects.get(user_id=review.user_id_id)
                inventory_new = HotelInventory.objects.get(id=review.inventory_id)
                company = Hotels.objects.get(id=review.company_id)
                del dict_review['user_id']
                del dict_review['inventory_id']
                del dict_review['company_id']
                dict_review.update({'user': customer.name})
                dict_review.update({'user_avatar': customer.image.url})
                dict_review.update({'company': company.name})
                dict_review.update({'inventory': inventory_new.room_name})
                parent_reviews.append(dict_review)
                dict_inventory.update({'reviews': parent_reviews})
        else:
            dict_inventory.update({'reviews': None})

        # for gallery
        galleries = InventoryGallery.objects.filter(hotel_inventory_id=inv_id)
        if galleries:
            for gallery in galleries:
                url = gallery.image.url
                dict_gallery = model_to_dict(gallery)
                del dict_gallery['image']
                del dict_gallery['hotel_inventory_id']
                dict_gallery.update({'image': url})
                parent_gallery.append(dict_gallery)

            dict_inventory.update({'gallery': parent_gallery})
        else:
            dict_inventory.update({'gallery': None})
        # for gallery

        # for facilities
        facilities = HotelAmenities.objects.filter(hotelinventory=inv_id)
        if facilities:
            for facility in facilities:
                url = facility.image.url
                dict_facility = model_to_dict(facility)
                del dict_facility['image']
                del dict_facility['created_at']
                dict_facility.update({'image': url})
                parent_facilities.append(dict_facility)
            dict_inventory.update({'facilities': parent_facilities})
        else:
            dict_inventory.update({'facilities': None})

        # for facilities

        # for HotelRoomFeature
        roomfeatures = HotelRoomFeature.objects.filter(hotelinventory=inv_id)
        if roomfeatures:
            for roomfeature in roomfeatures:
                dict_room_facility = model_to_dict(roomfeature)
                parent_room_facilities.append(dict_room_facility)
            dict_inventory.update({'room features': parent_room_facilities})
        else:
            dict_inventory.update({'room features': None})

        # for HotelRoomFeature

        # for HotelRoomType
        roomtypes = HotelRoomType.objects.filter(hotelinventory=inv_id)
        if roomtypes:
            for roomtype in roomtypes:
                dict_room_type = model_to_dict(roomtype)
                parent_room_type.append(dict_room_type)
            dict_inventory.update({'room type': parent_room_type})
        else:
            dict_inventory.update({'room type': None})

        # for HotelRoomType

        # for Bed Type
        bedtypes = Inventory_Bed_Type.objects.filter(inventory=inv_id)
        if bedtypes:
            for bedtype in bedtypes:
                dict_bed_type = model_to_dict(bedtype)
                del dict_bed_type['created_at']
                del dict_bed_type['inventory']
                del dict_bed_type['bed_type']
                dict_bed_type.update({'bed_type': bedtype.bed_type.name})
                bed_type.append(dict_bed_type)
            dict_inventory.update({'bed type': bed_type})
        else:
            dict_inventory.update({'bed type': None})

        # for Bed Type
        inventory['inventory'] = dict_inventory
        return inventory
    else:
        inventory['inventory'] = None
        return inventory


def HotelList(hotel_id):
    hoteladdress = HotelAddress.objects.filter(hotel=hotel_id)
    mainlist = []

    for addr in hoteladdress:
        hotel = {}
        temphotel = Hotels.objects.get(id=addr.hotel_id)
        hotel_dict = model_to_dict(Hotels.objects.get(id=addr.hotel_id))
        inventories = HotelInventory.objects.filter(hotel=addr.hotel_id)
        roughstartingPrice = inventories.aggregate(Min('price'))['price__min']
        startingPrice = inventories.aggregate(Min('price'))['price__min']

        if roughstartingPrice is None:
            startingPrice = decimal.Decimal('0.00')
        else:
            decimal.Decimal(inventories.aggregate(Min('price'))['price__min'])

        del hotel_dict['image']
        del hotel_dict['facilities']
        del hotel_dict['languages']
        del hotel_dict['owner_id']
        hotel_dict.update({'owner': temphotel.owner_id.name})
        hotel_dict.update({'startingPrice': startingPrice})
        hotel_dict.update({'owner_avatar': temphotel.owner_id.image.url})
        hotel_dict.update({'image': temphotel.image.url})

        # for review
        reviews = HotelReview.objects.filter(company_id=addr.hotel_id, module='hotel')

        parent_reviews = []
        if reviews:
            for review in reviews:
                dict_review = model_to_dict(review)
                if Customer.objects.filter(user_id=review.user_id).exists():
                    customer = Customer.objects.get(user_id=review.user_id)
                    if review.inventory_id != None:
                        inventory_new = HotelInventory.objects.get(id=review.inventory_id)
                        dict_review.update({'inventory': inventory_new.room_name})
                    company = Hotels.objects.get(id=review.company_id)
                    del dict_review['inventory_id']
                    del dict_review['user_id']
                    del dict_review['company_id']

                    dict_review.update({'user': customer.name})
                    dict_review.update({'user_avatar': customer.image.url})
                    dict_review.update({'company': company.name})
                    parent_reviews.append(dict_review)
        # else:
        #     parent_reviews.append(None)
        # Appending None will append NULL in parent review.

        hotelgalleries = HotelGallery.objects.filter(hotel_id=addr.hotel_id)
        hotelgallery = {}
        hotelgallerylist = []
        for hg in hotelgalleries:
            hgurl = hg.image.url
            hotelgallery = model_to_dict(hg)
            hotelgallery.update({'image': hgurl})
            hotelgallery.update({'title': hg.title})
            hotelgallerylist.append(hotelgallery)
        hotelfacilities = HotelFacilities.objects.filter(facilitiess=addr.hotel_id)
        hotelfacs = {}
        hotelfaclst = []
        for hf in hotelfacilities:
            hfurl = hf.image.url
            hotelfacs = model_to_dict(hf)
            hotelfacs.update({'image': hfurl})
            hotelfaclst.append(hotelfacs)
        languages = Language.objects.filter(languages=addr.hotel_id)
        languagespoken = {}
        lslst = []
        for lang in languages:
            languagespoken = model_to_dict(lang)
            lslst.append(languagespoken)

        state = addr.state.name
        city = addr.city.name
        country = addr.country.name
        addressdict = model_to_dict(addr)
        addressdict.update({'state': state})
        addressdict.update({'city': city})
        addressdict.update({'country': country})
        del addressdict['landmarks']
        hotellandmarks = Landmark.objects.filter(hotellandmarks=addr.hotel_id)
        hotellmks = {}
        hotelmklst = []
        for hlm in hotellandmarks:
            hotellmks = model_to_dict(hlm)
            # lmurl = hlm.image.url
            # hotellmks.update({'image': lmurl})
            hotelmklst.append(hotellmks)
        hotel['hotel'] = hotel_dict
        hotel['facilities'] = hotelfaclst
        hotel['reviews'] = parent_reviews
        hotel['gallery'] = hotelgallerylist
        hotel['languages'] = lslst
        hotel['address'] = addressdict
        hotel['landmarks'] = hotelmklst
    return hotel
