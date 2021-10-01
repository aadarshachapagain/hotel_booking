import json

from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse

from booking.customer.models import Customer
from hotel.amenities.models import HotelAmenities
from hotel.inventory.models import HotelInventory
from hotel.inventory_bed_type.models import Inventory_Bed_Type
from hotel.inventorygallery.models import InventoryGallery
from hotel.models import Hotels
from hotel.reviews.models import HotelReview
from hotel.roomfeature.models import HotelRoomFeature
from hotel.roomtype.models import HotelRoomType
from hotel.models import Hotels
from hotel.inventoryOffers.models import InventoryOffers
from hotel.offers.models import Offers


# def formatInventory(id, roomsavailable):
def formatInventory(id, roomavailable='no_of_rooms'):
    parent_gallery = []
    parent_facilities = []
    offerlist = []
    parent_room_facilities = []
    parent_room_type = []
    bed_type = []
    inventory = {}
    inventory_basic = HotelInventory.objects.get(id=id)
    if roomavailable == 'no_of_rooms':
        roomavailable = inventory_basic.no_of_rooms

    hotelid = inventory_basic.hotel_id
    hotel = Hotels.objects.get(id=hotelid)

    dict_inventory = model_to_dict(inventory_basic)

    del dict_inventory['priceforadult']
    del dict_inventory['amenities']
    del dict_inventory['roomfeatures']
    del dict_inventory['roomtype']
    del dict_inventory['created_at']
    del dict_inventory['image']

    dict_inventory.update({'hotel': hotel.name})
    dict_inventory.update({'hotel_id': hotel.id})
    dict_inventory.update({'hoteladdress': hotel.address.address})
    dict_inventory.update({'availableroom': roomavailable})
    dict_inventory.update({'priceforadult': json.loads(inventory_basic.priceforadult)})
    dict_inventory.update({'main_image': inventory_basic.image.url})

    # for offer
    offers = InventoryOffers.objects.filter(hotel_inventory=id)
    if offers.exists:
        for offer in offers:
            currentoffer = Offers.objects.get(id=offer.offer_id)
            dict_offer = model_to_dict(currentoffer)
            dict_offer.update({'banner_image': currentoffer.banner_image.url})
            # del dict_offer['banner_image']
            offerlist.append(dict_offer)
        dict_inventory.update({'offers': offerlist})
    else:
        dict_inventory.update({'offers': []})
    # for offer

    # for review
    reviews = HotelReview.objects.filter(inventory_id=id).order_by('-rating')
    if reviews:
        review = reviews[0]
    else:
        review = False

    parent_reviews = []
    if review:
        dict_review = model_to_dict(review)
        if Customer.objects.filter(user_id=review.user_id).exists():
            customer = Customer.objects.get(user_id=review.user_id)
            inventory_new = HotelInventory.objects.get(id=review.inventory_id)
            company = Hotels.objects.get(id=review.company_id)
            del dict_review['user_id']
            del dict_review['inventory_id']
            del dict_review['company_id']
            dict_review.update({'user': customer.name})
            dict_review.update({'user_avatar': customer.image.url})
            dict_review.update({'company': company.name})
            dict_review.update({'inventory': inventory_new.room_name})
            dict_inventory.update({'reviews': parent_reviews})
            parent_reviews.append(dict_review)
    else:
        dict_inventory.update({'reviews': []})

    # for gallery
    galleries = InventoryGallery.objects.filter(hotel_inventory_id=id)
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
        dict_inventory.update({'gallery':[]})
    # for gallery

    # for facilities
    facilities = HotelAmenities.objects.filter(hotelinventory=id)
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
        dict_inventory.update({'facilities': []})
    # for facilities

    # for HotelRoomFeature
    roomfeatures = HotelRoomFeature.objects.filter(hotelinventory=id)
    if roomfeatures:
        for roomfeature in roomfeatures:
            dict_room_facility = model_to_dict(roomfeature)
            parent_room_facilities.append(dict_room_facility)
        dict_inventory.update({'room_features': parent_room_facilities})
    else:
        dict_inventory.update({'room_features':[]})
        # for HotelRoomFeature

        # for HotelRoomType
        roomtypes = HotelRoomType.objects.filter(hotelinventory=id)
        if roomtypes:
            for roomtype in roomtypes:
                dict_room_type = model_to_dict(roomtype)
                parent_room_type.append(dict_room_type)
            dict_inventory.update({'room_type': parent_room_type})
        else:
            dict_inventory.update({'room_type':[]})
            # for HotelRoomType
            # for Bed Type
            bedtypes = Inventory_Bed_Type.objects.filter(inventory=id)
            if bedtypes:
                for bedtype in bedtypes:
                    dict_bed_type = model_to_dict(bedtype)
                    del dict_bed_type['created_at']
                    del dict_bed_type['inventory']
                    del dict_bed_type['bed_type']
                    dict_bed_type.update({'bed_type': bedtype.bed_type.name})
                    bed_type.append(dict_bed_type)
                dict_inventory.update({'bed_type': bed_type})
            else:
                dict_inventory.update({'bed_type': []})
            # for Bed Type

    inventory.update(dict_inventory)
    # return JsonResponse(inventory, safe=False)
    return inventory
    # return id





