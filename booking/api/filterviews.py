from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.utils import json
from hotel.city.models import City
from hotel.address.models import HotelAddress
from hotel.inventory.models import HotelInventory
from hotel.models import Hotels
from hotel.reviews.models import HotelReview
from hotel.inventory_bed_type.models import Inventory_Bed_Type
from booking.api import utils
from django.db.models import Avg
from hotel.inventory.utils import formatInventory
from hotel.bedType.models import BedType
from hotel.hotel_facilities.models import HotelFacilities

# from hotel.models import Hotels
from django.db.models import Avg, Max, Min
from booking.utils import HotelList


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def filterandreturninventory(request):
    invsent = []
    dict_inv = {}
    userRatingIdList = []
    hotelfacIdList = []
    roomFacIDList = []
    bedPreferenceIdList = []
    min_price = 0
    max_price = 100000
    hotelStarlist = []

    if request.method == "POST":
        received_json_data = json.loads(request.body)
        noofrooms = received_json_data['noofrooms']
        checkin = received_json_data['checkin']
        checkout = received_json_data['checkout']
        location = received_json_data['location']
        no_child = received_json_data['no_child']
        no_adult = received_json_data['no_adult']
        no_infant = received_json_data['no_infant']
        userRating = received_json_data['userrating']
        hotelFacilities = received_json_data['hotelfacilities']
        roomFacilities = received_json_data['roomfacilities']
        bedPreferences = received_json_data['bedpreference']
        hotelStars = received_json_data['starrating']
        min_price = received_json_data['min_price']
        max_price = received_json_data['max_price']
        sorting = received_json_data['sorting']

        if not received_json_data['limit']:
            limit = 10
        else:
            limit = int(received_json_data['limit'])

        if not received_json_data['page']:
            page = 1
        else:
            page = int(received_json_data['page'])

        for ur in userRating:
            userRatingIdList.append(ur['value'])

        for fl in hotelFacilities:
            hotelfacIdList.append(fl['id'])

        for rf in roomFacilities:
            roomFacIDList.append(rf['id'])

        for bp in bedPreferences:
            bedPreferenceIdList.append(bp['id'])

        for hs in hotelStars:
            hotelStarlist.append(hs['value'])

        obtained_tuple = utils.getMatchingInventory(location, checkin, checkout, no_child, no_adult, no_infant)

        # obtained_inv_list = utils.getMatchingInventory(location, checkin, checkout, no_child, no_adult, no_infant)

        filterByNoRooms = filterInventoryNoOfRooms(obtained_tuple, noofrooms)
        # obtained_inv_list = obtained_tuple[0]
        # number_of_avail_room = obtained_tuple[1]

        obtained_inv_list = filterByNoRooms[0]
        number_of_avail_room = filterByNoRooms[1]

        filteredinvByHotelFacs = filterInventoryByHotelFacilitiesNStar(obtained_inv_list, hotelfacIdList, hotelStarlist)
        filteredinvByUserRating = filterInventoryByUserRating(filteredinvByHotelFacs, userRatingIdList)
        filteredinvByRoomFac = filterInventoryByRoomFacNPrice(filteredinvByUserRating, roomFacIDList, min_price,
                                                              max_price)
        filteredinvByBedPref = filterInventoryByBedPref(filteredinvByRoomFac, bedPreferenceIdList)

        if sorting == 'starrating':
            sortedData = sortByStar(filteredinvByBedPref)
        elif sorting == 'pricereverse':
            sortedData = sortByprice(filteredinvByBedPref, order='reverse')
        elif sorting == 'price':
            sortedData = sortByprice(filteredinvByBedPref)
        else:
            sortedData = filteredinvByBedPref
    return sortedData, obtained_inv_list, number_of_avail_room, limit, page


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def filterinventory(request):
    invsent = []
    dict_inv = {}
    userRatingIdList = []
    hotelfacIdList = []
    roomFacIDList = []
    bedPreferenceIdList = []
    min_price = 0
    max_price = 100000
    hotelStarlist = []

    if request.method == "POST":
        received_json_data = json.loads(request.body)
        noofrooms = received_json_data['noofrooms']
        checkin = received_json_data['checkin']
        checkout = received_json_data['checkout']
        location = received_json_data['location']
        no_child = received_json_data['no_child']
        no_adult = received_json_data['no_adult']
        no_infant = received_json_data['no_infant']
        userRating = received_json_data['userrating']
        hotelFacilities = received_json_data['hotelfacilities']
        roomFacilities = received_json_data['roomfacilities']
        bedPreferences = received_json_data['bedpreference']
        hotelStars = received_json_data['starrating']
        min_price = received_json_data['min_price']
        max_price = received_json_data['max_price']
        sorting = received_json_data['sorting']

        if not received_json_data['limit']:
            limit = 10
        else:
            limit = int(received_json_data['limit'])

        if not received_json_data['page']:
            page = 1
        else:
            page = int(received_json_data['page'])

        for ur in userRating:
            userRatingIdList.append(ur['value'])

        for fl in hotelFacilities:
            hotelfacIdList.append(fl['id'])

        for rf in roomFacilities:
            roomFacIDList.append(rf['id'])

        for bp in bedPreferences:
            bedPreferenceIdList.append(bp['id'])

        for hs in hotelStars:
            hotelStarlist.append(hs['value'])

        obtained_tuple = utils.getMatchingInventory(location, checkin, checkout, no_child, no_adult, no_infant)

        # obtained_inv_list = utils.getMatchingInventory(location, checkin, checkout, no_child, no_adult, no_infant)

        filterByNoRooms = filterInventoryNoOfRooms(obtained_tuple, noofrooms)
        # obtained_inv_list = obtained_tuple[0]
        # number_of_avail_room = obtained_tuple[1]

        obtained_inv_list = filterByNoRooms[0]
        number_of_avail_room = filterByNoRooms[1]

        filteredinvByHotelFacs = filterInventoryByHotelFacilitiesNStar(obtained_inv_list, hotelfacIdList, hotelStarlist)
        filteredinvByUserRating = filterInventoryByUserRating(filteredinvByHotelFacs, userRatingIdList)
        filteredinvByRoomFac = filterInventoryByRoomFacNPrice(filteredinvByUserRating, roomFacIDList, min_price,
                                                              max_price)
        filteredinvByBedPref = filterInventoryByBedPref(filteredinvByRoomFac, bedPreferenceIdList)

        if sorting == 'starrating':
            sortedData = sortByStar(filteredinvByBedPref)
        elif sorting == 'pricereverse':
            sortedData = sortByprice(filteredinvByBedPref, order='reverse')
        elif sorting == 'price':
            sortedData = sortByprice(filteredinvByBedPref)
        else:
            sortedData = filteredinvByBedPref

    # result = filterandreturninventory(request)
    # sortedData = result[0]
    # obtained_inv_list = result[1]
    # number_of_avail_room = result[2]
    # limit = result[3]
    # page = result[4]

    for id in sortedData:
        if id in obtained_inv_list:
            index = obtained_inv_list.index(id)
            number_of_room = number_of_avail_room[index]
            dict_inv = formatInventory(id, number_of_room)
            invsent.append(dict_inv)

    data = utils.paginate(invsent, limit, page)
    return JsonResponse(data, safe=False)


def filterInventoryByHotelFacilitiesNStar(invIdList, facIdList, hotelStarlist):
    hotelsid = []
    hotelinvsid = []
    allfacs = HotelFacilities.objects.all()

    if len(facIdList) is 0:
        for fac in allfacs:
            facIdList.append(fac.id)

    if len(hotelStarlist) is 0:
        hotelStarlist = ['Tourist Standard', '1 Star', '2 Star', '3 Star', '4 Star', '5 Star', '6 Star', '7 Star']

    #     facIdList = ['']

    hotels_with_facs = Hotels.objects.filter(facilities__in=facIdList, star_rating__in=hotelStarlist)

    if hotels_with_facs:
        for hotel in hotels_with_facs:
            if hotel.id not in hotelsid:
                hotelsid.append(hotel.id)
    if hotelsid:
        inv_with_hotel_facs = HotelInventory.objects.filter(hotel_id__in=hotelsid)
        for inv in inv_with_hotel_facs:
            if inv.id not in hotelinvsid:
                hotelinvsid.append(inv.id)
    # finalinvlist = (list(set(hotelinvsid) - set(invIdList)))
    finalinvlist = (list(set(invIdList) & set(hotelinvsid)))
    return finalinvlist


# Member.objects.aggregate(Avg('wins'))

def filterInventoryByUserRating(invIdlist, starIdList):
    filteredInvsID = []
    invs = HotelReview.objects.filter(module='hotel')
    un_sorted_rating_array = []
    un_sorted_inv_list = []

    if len(starIdList) is 0:
        starIdList = [1, 2, 3, 4, 5]
        finalinvlist = invIdlist
    else:
        for inv in invs:
            if inv.inventory_id not in filteredInvsID:
                averagestar = HotelReview.objects.filter(inventory_id=inv.inventory_id, module='hotel').aggregate(
                    Avg('rating'))
                int_averagestar = int(averagestar['rating__avg'])
                if int_averagestar in starIdList:
                    un_sorted_rating_array.append(int_averagestar)
                    un_sorted_inv_list.append(inv.inventory_id)
                    filteredInvsID.append(inv.inventory_id)
        finalinvlist = (list(set(filteredInvsID) & set(invIdlist)))
    return finalinvlist


from hotel.amenities.models import HotelAmenities


def filterInventoryByRoomFacNPrice(invIdlist, roomFacIDList, lower_price, upper_price):
    filteredInvsID = []

    if len(roomFacIDList) is 0:
        all_amenities = HotelAmenities.objects.all()
        for amen in all_amenities:
            roomFacIDList.append(amen.id)

    invs = HotelInventory.objects.filter(amenities__in=roomFacIDList, price__range=(lower_price, upper_price))
    for inv in invs:
        if inv.id not in invs:
            filteredInvsID.append(inv.id)
    finalinvlist = (list(set(invIdlist) & set(filteredInvsID)))
    return finalinvlist


def filterInventoryByBedPref(filteredinvByRoomFac, bedPreferenceIdList):
    filteredInvsID = []

    if len(bedPreferenceIdList) is 0:
        finalinvlist = filteredinvByRoomFac
    else:
        all_bedPreference = BedType.objects.all()
        for bedpreference in all_bedPreference:
            bedPreferenceIdList.append(bedpreference.id)
        invs = Inventory_Bed_Type.objects.filter(bed_type_id__in=bedPreferenceIdList)
        for inv in invs:
            if inv.id not in filteredInvsID:
                filteredInvsID.append(inv.inventory.id)
        finalinvlist = (list(set(filteredinvByRoomFac) & set(filteredInvsID)))

    return finalinvlist


def filterInventoryNoOfRooms(obtained_tuple, noofrooms):
    obtained_inv_list = obtained_tuple[0]
    number_of_avail_room = obtained_tuple[1]

    req_number_of_rooms = []
    req_inv_ids = []
    index = []

    i = -1
    for room in number_of_avail_room:
        i = i + 1
        if noofrooms <= room:
            index.append(i)

    for ind in index:
        req_inv_ids.append(obtained_inv_list[ind])
        req_number_of_rooms.append(number_of_avail_room[ind])

    return req_inv_ids, req_number_of_rooms


def sortByStar(filteredinvByBedPref):
    unsortedInvsID = []
    un_sorted_rating_array = []
    un_sorted_inv_list = []
    for inv in filteredinvByBedPref:
        if inv not in unsortedInvsID:
            averagestar = HotelReview.objects.filter(inventory_id=inv, module='hotel').aggregate(
                Avg('rating'))
            int_averagestar = int(averagestar['rating__avg'])
            un_sorted_rating_array.append(int_averagestar)
            un_sorted_inv_list.append(inv)
    mapped_dict = dict(zip(un_sorted_inv_list, un_sorted_rating_array))
    sorted_dict = {k: v for k, v in sorted(mapped_dict.items(), key=lambda item: item[1])}
    sorted_list = list(sorted_dict)
    reverse_list = sorted_list[::-1]

    return reverse_list


def sortByprice(filteredinvByBedPref, order='None'):
    invs = HotelInventory.objects.filter(id__in=filteredinvByBedPref).order_by('price')

    unsorted_list = []
    for inv in invs:
        unsorted_list.append(inv.id)
    if order == 'reverse':
        sorted_list = unsorted_list[::-1]
    else:
        sorted_list = unsorted_list
    return sorted_list


def inventoryByLocation(arr):
    city_list = []
    list_of_invID = []

    for a in arr:
        city_id = City.objects.get(name=a).id
        if city_id not in city_list:
            city_list.append(city_id)

    hotel_list = HotelAddress.objects.filter(city_id__in=city_list)
    for single_hotel in hotel_list:
        hotelinv = HotelInventory.objects.filter(hotel_id=single_hotel.hotel)
        for inv in hotelinv:
            if inv.id not in list_of_invID:
                list_of_invID.append(inv.id)
    print('list_of_invID')
    print(list_of_invID)

    return 0


def hotel_filter(request):
    invsent = []
    dict_inv = {}
    userRatingIdList = []
    hotelfacIdList = []
    roomFacIDList = []
    bedPreferenceIdList = []
    min_price = 0
    max_price = 100000
    hotelStarlist = []
    final_hotellist = []
    hotelsent = []

    if request.method == "GET":
        received_json_data = json.loads(request.body)
        noofrooms = received_json_data['noofrooms']
        checkin = received_json_data['checkin']
        checkout = received_json_data['checkout']
        location = received_json_data['location']
        no_child = received_json_data['no_child']
        no_adult = received_json_data['no_adult']
        no_infant = received_json_data['no_infant']
        userRating = received_json_data['userrating']
        hotelFacilities = received_json_data['hotelfacilities']
        roomFacilities = received_json_data['roomfacilities']
        bedPreferences = received_json_data['bedpreference']
        hotelStars = received_json_data['starrating']
        min_price = received_json_data['min_price']
        max_price = received_json_data['max_price']
        sorting = received_json_data['sorting']

        if not received_json_data['limit']:
            limit = 10
        else:
            limit = int(received_json_data['limit'])

        if not received_json_data['page']:
            page = 1
        else:
            page = int(received_json_data['page'])

        for ur in userRating:
            userRatingIdList.append(ur['value'])

        for fl in hotelFacilities:
            hotelfacIdList.append(fl['id'])

        for rf in roomFacilities:
            roomFacIDList.append(rf['id'])

        for bp in bedPreferences:
            bedPreferenceIdList.append(bp['id'])

        for hs in hotelStars:
            hotelStarlist.append(hs['value'])

        obtained_tuple = utils.getMatchingInventory(location, checkin, checkout, no_child, no_adult, no_infant)

        # obtained_inv_list = utils.getMatchingInventory(location, checkin, checkout, no_child, no_adult, no_infant)

        filterByNoRooms = filterInventoryNoOfRooms(obtained_tuple, noofrooms)
        # obtained_inv_list = obtained_tuple[0]
        # number_of_avail_room = obtained_tuple[1]

        obtained_inv_list = filterByNoRooms[0]
        number_of_avail_room = filterByNoRooms[1]

        filteredinvByHotelFacs = filterInventoryByHotelFacilitiesNStar(obtained_inv_list, hotelfacIdList, hotelStarlist)
        filteredinvByUserRating = filterInventoryByUserRating(filteredinvByHotelFacs, userRatingIdList)
        filteredinvByRoomFac = filterInventoryByRoomFacNPrice(filteredinvByUserRating, roomFacIDList, min_price,
                                                              max_price)
        filteredinvByBedPref = filterInventoryByBedPref(filteredinvByRoomFac, bedPreferenceIdList)

        if sorting == 'starrating':
            sortedData = sortByStar(filteredinvByBedPref)
        elif sorting == 'pricereverse':
            sortedData = sortByprice(filteredinvByBedPref, order='reverse')
        elif sorting == 'price':
            sortedData = sortByprice(filteredinvByBedPref)
        else:
            sortedData = filteredinvByBedPref
        for invid in sortedData:
            if invid not in final_hotellist:
                final_hotellist.append(invid)

        for inventoryid in final_hotellist:
            hotel_id = HotelInventory.objects.get(id=inventoryid).hotel_id
            hotelsent.append(HotelList(hotel_id))

    data = utils.paginate(hotelsent, limit, page)
    return JsonResponse(data, safe=False)
