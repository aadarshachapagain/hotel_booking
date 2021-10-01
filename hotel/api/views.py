import random
from datetime import datetime

from django.db.models import Min, Max

from account.Language.models import Language
from booking.customer.models import Customer
from booking.utils import HotelList
# import datetime
from hotel.Country.models import Country
from hotel.amenities.models import HotelAmenities
from hotel.api.serializers import HotelSerializer, CommentSerializer, MyNewSerializer, CityListSerializaer, \
    HotelSearchSerializer, HotelAddressSerializer, InventorySearchSerializer, HotelCountrySerializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from hotel.inventoryOffers.models import InventoryOffers
from hotel.inventory_bed_type.models import Inventory_Bed_Type
from hotel.models import Hotels, HotelFacilitiesMiddle
from hotel.owner.models import HotelOwner
from hotel.city.models import City
from hotel.landmark.models import Landmark
from hotel.inventory.models import HotelInventory
from account.models import User
from hotel.reviews.models import HotelReview
from hotel.roomfeature.models import HotelRoomFeature
from hotel.roomtype.models import HotelRoomType
from hotel.staff.models import HotelStaff
from hotel.address.models import HotelAddress
from hotel.api.serializers import HotelInventoryListSerializer
from hotel.api.serializers import HotelCitySerializer
from hotel.api.serializers import HotelOwnerListSerializaer
from hotel.api.serializers import HotelNameSerializer
from hotel.api.serializers import HotelLandmarkSerializer
# from hotel.api.serializers import HotelQuerySerializer
from hotel.api.serializers import HotelListSerializaer
from hotel.api.serializers import HotelAddressListSerializer
from hotel.api.serializers import HotelGalleryListSerializaer
from hotel.inventorygallery.models import InventoryGallery
from django.forms.models import model_to_dict
from hotel.hotel_facilities.models import HotelFacilities
from hotel.spotlight.models import Spotlight
# from hotel.api import serializers
from django.core import serializers
from hotel.inventory.utils import formatInventory
from booking.utils import HotelList

from django.views.decorators.csrf import csrf_exempt

import json
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from django.http import HttpResponse, JsonResponse
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

import geopy.distance

# from rental.vehicleOffers.models import VehicleOffers
from travel.devsettings import MEDIA_ROOT
# from travel_tour.packageOffers.models import PackageOffers
from booking.api.utils import paginate
from django.db.models import Avg, Max, Min, Sum



class HotelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hotels.objects.all().order_by('created_at')
    serializer_class = HotelSerializer


class HotelCitySet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = City.objects.all()
    serializer_class = HotelCitySerializer


class HotelNameSet(viewsets.ModelViewSet):
    # queryset = Hotels.objects.values('name')
    serializer_class = HotelNameSerializer



# class CountrySet(viewsets.ModelViewSet):
#     queryset = Country.objects.values('name', 'id')
#     serializer_class = HotelCountrySerializer


def CountrySet(request):
    maindict = {}
    list = []
    countrieslist = (Country.objects.all())
    for country in countrieslist:
        list.append(model_to_dict(country))

    maindict['countries'] = list
    return JsonResponse(maindict, safe=False)


class HotelLandmarkSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Landmark.objects.all()
    serializer_class = HotelLandmarkSerializer


# class HotelQueryAPIView(APIView):
#     permission_classes = [AllowAny]
#     serializer_class  = HotelQuerySerializer
#     # since we are using base api view we need to define every method we use
#
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer  = HotelQuerySerializer(data = data)
#         if serializer.is_valid(raise_exception = True):
#             new_data = serializer.data
#             print(new_data)
#             return Response(new_data, status=HTTP_200_OK)
#
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class HotelListAddressAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = HotelAddress.objects.all()
    serializer_class = HotelAddressListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['state', 'city']


class HotelListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Hotels.objects.all()
    serializer_class = HotelListSerializaer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'id']


class HotelOwnerListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = HotelOwner.objects.all()
    serializer_class = HotelOwnerListSerializaer
    filter_backends = [SearchFilter]


# search_fields = ['state','city']


class HotelInventoryListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = HotelInventory.objects.all()
    serializer_class = HotelInventoryListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['hoteladdress__city']


class HotelGalleryListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = InventoryGallery.objects.all()
    serializer_class = HotelGalleryListSerializaer
    filter_backends = [SearchFilter]
    search_fields = ['hotel_inventory_id__hoteladdress__city__name']


class MyData(object):
    def __init__(self, email, content, user, image):
        self.email = email
        self.content = content
        self.user = user
        self.owner_id = image,


class HotelGalleryListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = InventoryGallery.objects.all()
    serializer_class = HotelGalleryListSerializaer
    filter_backends = [SearchFilter]
    search_fields = ['hotel_inventory_id__hoteladdress__city__name']


class NewData(object):
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact


class NewHotelApi(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print('in Api')
        print(request.data['email'])
        email = request.data['email']
        content = request.data['content']
        # email=request['email']
        user = User.objects.values_list('username', flat=True).get(email=email)
        tmpimage = City.objects.all()
        print('tempimage')
        listcity = {}
        for index, d in enumerate(tmpimage):
            print(d.name)
            listcity[index] = CityListSerializaer(d).data

        # print(tmpimage)
        # onment = NewData(name="asdf", contact="0998")
        # image=CityListSerializaer(tmpimage).data
        # return  Response(listcity)
        # print(image)
        comment = MyData(email=email, content=content, user=user, image=listcity)
        serializer = CommentSerializer(comment)
        temp111 = {}
        return Response(serializer.data, status=status.HTTP_201_CREATED)


#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=ValueError):
#         serializer.create(validated_data=request.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.error_messages,
#                     status=status.HTTP_400_BAD_REQUEST)


class NewView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Hotels.objects.all()
    serializer_class = MyNewSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class HotelSearchViewSet(generics.ListAPIView):
    queryset = Hotels.objects.all().order_by('created_at')
    serializer_class = HotelSearchSerializer
    filter_backends = [SearchFilter]
    search_fields = ['id', 'name', 'facilities__name', 'address__city__name', 'address__city__landmark__name',
                     'address__address']


class HotelAddressViewSet(generics.ListAPIView):
    queryset = HotelAddress.objects.all().order_by('created_at')
    serializer_class = HotelAddressSerializer


class InventoryViewSet(generics.ListAPIView):
    queryset = HotelInventory.objects.all().order_by('created_at')
    serializer_class = InventorySearchSerializer


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def defInventoryDetailAPIView(request):
    if request.method == "POST":
        inventory_id = request.POST.get('inventory')
        hotel_id = request.POST.get('hotel')
        inventory = {}
        custom_bed = []
        parent_gallery = []
        parent_reviews = []
        parent_inventory = []
        parent_facilities = []
        parent_room_facilities = []
        parent_room_type = []
        bed_type = []
        inv_count = HotelInventory.objects.filter(id=inventory_id, hotel=hotel_id).count()
        if inv_count > 0:
            inventory_basic = HotelInventory.objects.get(id=inventory_id, hotel=hotel_id)
            inv_id = inventory_basic.id
            dict_inventory = model_to_dict(inventory_basic)
            del dict_inventory['priceforadult']
            del dict_inventory['amenities']
            del dict_inventory['roomfeatures']
            # del dict_inventory['hoteladdress']
            del dict_inventory['roomtype']
            del dict_inventory['created_at']
            del dict_inventory['image']
            dict_inventory.update({'priceforadult': json.loads(inventory_basic.priceforadult)})
            dict_inventory.update({'main_image': inventory_basic.image.url})

            # for review
            reviews = HotelReview.objects.filter(inventory_id=inv_id)
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
            return JsonResponse(inventory, safe=False)
        else:
            inventory['inventory'] = None
            return JsonResponse(inventory, safe=False)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def defInventoryAPIView(request):
    if request.method == "POST":
        hotel_id = request.POST.get('hotel')
        main = []
        inventory = {}

        inv_count = HotelInventory.objects.filter(hotel=hotel_id).count()
        if inv_count:
            inventory_basic = HotelInventory.objects.filter(hotel=hotel_id)
            for inv in inventory_basic:
                inv_id = inv.id
                print(inv_id)
                dict_inventory = model_to_dict(inv)
                del dict_inventory['priceforadult']
                del dict_inventory['amenities']
                del dict_inventory['roomfeatures']
                # del dict_inventory['hoteladdress']
                del dict_inventory['roomtype']
                del dict_inventory['created_at']
                del dict_inventory['image']
                dict_inventory.update({'priceforadult': json.loads(inv.priceforadult)})
                dict_inventory.update({'main_image': inv.image.url})

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
                parent_gallery = []
                if galleries:
                    for gallery in galleries:
                        url = gallery.image.url
                        dict_gallery = model_to_dict(gallery)
                        del dict_gallery['image']
                        del dict_gallery['hotel_inventory_id']
                        dict_gallery.update({'image': url})
                        parent_gallery.append(dict_gallery)
                        print(parent_gallery)
                    dict_inventory.update({'gallery': parent_gallery})
                else:
                    dict_inventory.update({'gallery': None})
                # for gallery

                # for facilities
                parent_facilities = []
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
                # # for facilities

                # # for HotelRoomFeature
                parent_room_facilities = []
                roomfeatures = HotelRoomFeature.objects.filter(hotelinventory=inv_id)
                if roomfeatures:
                    for roomfeature in roomfeatures:
                        dict_room_facility = model_to_dict(roomfeature)
                        parent_room_facilities.append(dict_room_facility)
                    dict_inventory.update({'room features': parent_room_facilities})
                else:
                    dict_inventory.update({'room features': None})

                # # for HotelRoomFeature

                # # for HotelRoomType
                parent_room_type = []
                roomtypes = HotelRoomType.objects.filter(hotelinventory=inv_id)
                if roomtypes:
                    for roomtype in roomtypes:
                        dict_room_type = model_to_dict(roomtype)
                        parent_room_type.append(dict_room_type)
                    dict_inventory.update({'room type': parent_room_type})
                else:
                    dict_inventory.update({'room type': None})
                # # for HotelRoomType

                # # for Bed Type
                bed_type = []
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
                # # for Bed Type

                main.append(dict_inventory)
                inventory['inventory'] = main
            return JsonResponse(inventory, safe=False)
        else:
            inventory['inventory'] = None
            return JsonResponse(inventory, safe=False)


@api_view(['POST'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def getDistance(request):
    if request.method == "POST":
        objs = HotelAddress.objects.all()
        in_lat = request.POST.get('lat')
        in_long = request.POST.get('long')
        in_xy = (in_lat, in_long)
        sortedlist = []
        mainlist = []
        if 'limit' not in request.POST:
            limit = 10
        else:
            limit = int(request.POST.get('limit'))

        if 'page' not in request.POST:
            page = 1
        else:
            page = int(request.POST.get('page'))

        for obj in objs:
            hotel_dict = {}
            dblat = obj.latitude
            dblong = obj.longitude
            db_xy = (dblat, dblong)
            distance = geopy.distance.vincenty(in_xy, db_xy).km
            hotel_dict['distancefromquery'] = distance
            hotel_dict['hotel'] = HotelList(obj.hotel_id)
            mainlist.append(hotel_dict)

        sortedlist = sorted(mainlist, key=lambda k: k['distancefromquery'], reverse=False)

        data = paginate(sortedlist, limit, page)
        if not data:
            return HttpResponse('Sorry requested page donot exist')

        return JsonResponse(data, safe=False)


# @csrf_exempt
# @permission_classes((IsAuthenticated,))
# def getByCity(request):
#     in_city = request.POST.get('city')
#     city_id = City.objects.get(name=in_city).id
#     hoteladdress = HotelAddress.objects.filter(city_id=city_id)
#     maindict = {}
#     mainlist = []
#     for addr in hoteladdress:
#         hotel = {}
#         temphotel = Hotels.objects.get(id=addr.hotel_id)
#
#         # hotel_dict = model_to_dict(Hotels.objects.get(id=addr.hotel_id))
#         inventories = HotelInventory.objects.filter(hotel=addr.hotel_id)
#         startingPrice = inventories.aggregate(Min('price'))['price__min']
#         hotel_dict = model_to_dict(Hotels.objects.get(id=addr.hotel_id))
#         del hotel_dict['image']
#         del hotel_dict['facilities']
#         del hotel_dict['languages']
#         hotel_dict.update({'image': temphotel.image.url})
#         hotel_dict.update({'startingPrice': startingPrice})
#         hotelfacilities = HotelFacilities.objects.filter(facilitiess=addr.hotel_id)
#         hotelfacs = {}
#         hotelfaclst = []
#         for hf in hotelfacilities:
#             hfurl = hf.image.url
#             hotelfacs = model_to_dict(hf)
#             hotelfacs.update({'image': hfurl})
#             hotelfaclst.append(hotelfacs)
#         languages = Language.objects.filter(languages=addr.hotel_id)
#         languagespoken = {}
#         lslst = []
#         for lang in languages:
#             languagespoken = model_to_dict(lang)
#             lslst.append(languagespoken)
#         addressdict = model_to_dict(addr)
#         del addressdict['landmarks']
#         hotellandmarks = Landmark.objects.filter(hotellandmarks=addr.hotel_id)
#         hotellmks = {}
#         hotelmklst = []
#         for hlm in hotellandmarks:
#             hotellmks = model_to_dict(hlm)
#             lmurl = hlm.image.url
#             hotellmks.update({'image': lmurl})
#             hotelmklst.append(hotellmks)
#         hotel['hotel'] = hotel_dict
#         hotel['facilities'] = hotelfaclst
#         hotel['languages'] = lslst
#         hotel['address'] = addressdict
#         hotel['landmarks'] = hotelmklst
#         mainlist.append(hotel)
#         maindict['hotelarray'] = mainlist
#     return JsonResponse(maindict, safe=False)

@csrf_exempt
@permission_classes((IsAuthenticated,))
def getByCity(request):
    in_city = request.POST.get('city')
    city_id = City.objects.get(name=in_city).id
    hoteladdress = HotelAddress.objects.filter(city_id=city_id)
    maindict = {}
    mainlist = []
    if 'limit' not in request.POST:
        limit = 10
    else:
        limit = int(request.POST.get('limit'))

    if 'page' not in request.POST:
        page = 1
    else:
        page = int(request.POST.get('page'))

    for addr in hoteladdress:
        hotel = HotelList(addr.hotel.id)
        mainlist.append(hotel)

    data = paginate(mainlist, limit, page)
    if not data:
        return HttpResponse('Sorry requested page donot exist')

    # maindict['hotel'] = mainlist
    return JsonResponse(data, safe=False)


def extract_time(json):
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        return int(json['page']['update_time'])
    except KeyError:
        return 0


@csrf_exempt
@permission_classes((IsAuthenticated,))
def getHotelsonSpotlight(request):
    allspotlights = Spotlight.objects.all()
    maindict = {}
    mainlist = []
    sortedlist = []
    for singlehotel in allspotlights:
        hotel = HotelList(singlehotel.hotel.id)
        mainlist.append(hotel)
    sortedlist = sorted(mainlist, key=lambda k: k['hotel'].get('startingPrice', 0), reverse=False)
    maindict['hotel'] = sortedlist
    return JsonResponse(maindict, safe=False)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def mostlyUsedFacilities(request):
    row = HotelFacilitiesMiddle.max_use(request)
    row_list = []
    main_dict = {}
    for r in row:
        row_dict = {}
        a = list(r)
        facility_id = HotelFacilities.objects.get(id=a[0]).name
        count = a[1]
        row_dict.update({'facility': facility_id})
        row_dict.update({'count': count})
        row_list.append(row_dict)
    main_dict['facilities'] = row_list
    return JsonResponse(main_dict, safe=False)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def hotelOffers(request):
    row_list = []
    main_dict = {}
    now = datetime.now().date()
    offer_instance = InventoryOffers.objects.filter(offer__end_date__gte=now, offer__module='hotel')
    for offer in offer_instance:
        dict_offer = model_to_dict(offer)
        dict_offer.update({'package_name': offer.hotel_inventory.room_name})
        dict_offer.update({'offer_name': offer.offer.offer_name})
        dict_offer.update({'rate': offer.offer.rate})
        dict_offer.update({'description': offer.offer.description})
        dict_offer.update({'start_date': offer.offer.start_date.strftime('%Y-%m-%d')})
        dict_offer.update({'end_date': offer.offer.end_date.strftime('%Y-%m-%d')})
        dict_offer.update({'banner_image': offer.offer.banner_image.url})
        dict_offer.update({'original_price': offer.hotel_inventory.price})
        discount_price_temp = (offer.offer.rate * offer.hotel_inventory.price) / 100
        discount_price = offer.hotel_inventory.price - discount_price_temp
        dict_offer.update({'offer_price': discount_price})
        del dict_offer['created_at']
        del dict_offer['status']
        row_list.append(dict_offer)
    main_dict['offer'] = row_list
    return JsonResponse(main_dict, safe=False)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def allofferapi(request):
    row_list = []
    hotel_list = []
    main_dict = {}
    now = datetime.now().date()
    # offer_instance = PackageOffers.objects.filter(offer__end_date__gte=now, offer__module='travel_tour')
    # for offer in offer_instance:
    #     dict_offer = model_to_dict(offer)
    #     dict_offer.update({'package_name': offer.tour_package.package_name})
    #     dict_offer.update({'offer_name': offer.offer.offer_name})
    #     dict_offer.update({'rate': offer.offer.rate})
    #     dict_offer.update({'description': offer.offer.description})
    #     dict_offer.update({'start_date': offer.offer.start_date.strftime('%Y-%m-%d')})
    #     dict_offer.update({'end_date': offer.offer.end_date.strftime('%Y-%m-%d')})
    #     dict_offer.update({'banner_image': offer.offer.banner_image.url})
    #     dict_offer.update({'original_price': offer.tour_package.tour_cost})
    #
    #     discount_price_temp = (offer.offer.rate * offer.tour_package.tour_cost) / 100
    #     discount_price = offer.tour_package.tour_cost - discount_price_temp
    #     dict_offer.update({'offer_price': discount_price})
    #
    #     del dict_offer['created_at']
    #     del dict_offer['status']
    #     row_list.append(dict_offer)
    # main_dict['traveloffer'] = row_list

    # --------------------------------------------------------------------
    offer_instance = InventoryOffers.objects.filter(offer__end_date__gte=now, offer__module='hotel')
    for offer in offer_instance:
        dict_hoteloffer = model_to_dict(offer)
        dict_hoteloffer.update({'package_name': offer.hotel_inventory.room_name})
        dict_hoteloffer.update({'offer_name': offer.offer.offer_name})
        dict_hoteloffer.update({'rate': offer.offer.rate})
        dict_hoteloffer.update({'description': offer.offer.description})
        dict_hoteloffer.update({'start_date': offer.offer.start_date.strftime('%Y-%m-%d')})
        dict_hoteloffer.update({'end_date': offer.offer.end_date.strftime('%Y-%m-%d')})
        dict_hoteloffer.update({'banner_image': offer.offer.banner_image.url})

        dict_hoteloffer.update({'original_price': offer.hotel_inventory.price})
        discount_price_temp = (offer.offer.rate * offer.hotel_inventory.price) / 100
        discount_price = offer.hotel_inventory.price - discount_price_temp
        dict_hoteloffer.update({'offer_price': discount_price})

        del dict_hoteloffer['created_at']
        del dict_hoteloffer['status']
        hotel_list.append(dict_hoteloffer)
    main_dict['hoteloffer'] = hotel_list

    # rental_list = []
    # offer_instance = VehicleOffers.objects.filter(offer__end_date__gte=now, offer__module='rental')
    # for offer in offer_instance:
    #     dict_rentaloffer = model_to_dict(offer)
    #     dict_rentaloffer.update({'package_name': offer.vehicle_inventory.name})
    #     dict_rentaloffer.update({'offer_name': offer.offer.offer_name})
    #     dict_rentaloffer.update({'rate': offer.offer.rate})
    #     dict_rentaloffer.update({'description': offer.offer.description})
    #     dict_rentaloffer.update({'start_date': offer.offer.start_date.strftime('%Y-%m-%d')})
    #     dict_rentaloffer.update({'end_date': offer.offer.end_date.strftime('%Y-%m-%d')})
    #     dict_rentaloffer.update({'banner_image': offer.offer.banner_image.url})
    #
    #     # discount_price_temp = (offer.offer.rate * offer.vehicle_inventory.price) / 100
    #     # discount_price = offer.vehicle_inventory.price - discount_price_temp
    #     # dict_rentaloffer.update({'offer_price': discount_price})
    #     #
    #     dict_rentaloffer.update({'original_priceperday': offer.vehicle_inventory.priceperday})
    #     dict_rentaloffer.update({'original_priceperkm': offer.vehicle_inventory.priceperkm})
    #     dict_rentaloffer.update({'original_priceperhr': offer.vehicle_inventory.priceperhr})
    #
    #     discount_price_priceperday_temp = (offer.offer.rate * offer.vehicle_inventory.priceperday) / 100
    #     discount_priceperday = offer.vehicle_inventory.priceperday - discount_price_priceperday_temp
    #     dict_rentaloffer.update({'offer_priceperday': discount_priceperday})
    #
    #     discount_price_priceperkm_temp = (offer.offer.rate * offer.vehicle_inventory.priceperkm) / 100
    #     discount_priceperkm = offer.vehicle_inventory.priceperkm - discount_price_priceperkm_temp
    #     dict_rentaloffer.update({'offer_priceperkm': discount_priceperkm})
    #
    #     discount_price_priceperhr_temp = (offer.offer.rate * offer.vehicle_inventory.priceperhr) / 100
    #     discount_priceperhr = offer.vehicle_inventory.priceperhr - discount_price_priceperhr_temp
    #     dict_rentaloffer.update({'offer_priceperhr': discount_priceperhr})
    #
    #     del dict_rentaloffer['created_at']
    #     del dict_rentaloffer['status']
    #     rental_list.append(dict_rentaloffer)
    # main_dict['rentaloffer'] = rental_list

    return JsonResponse(main_dict, safe=False)




@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def shuffledallofferapi(request):
    row_list = []
    hotel_list = []
    main_dict = {}
    now = datetime.now().date()
    offer_instance = PackageOffers.objects.filter(offer__end_date__gte=now, offer__module='travel_tour')
    for offer in offer_instance:
        dict_offer = model_to_dict(offer)
        dict_offer.update({'package_name': offer.tour_package.package_name})
        dict_offer.update({'offer_name': offer.offer.offer_name})
        dict_offer.update({'rate': offer.offer.rate})
        dict_offer.update({'description': offer.offer.description})
        dict_offer.update({'start_date': offer.offer.start_date.strftime('%Y-%m-%d')})
        dict_offer.update({'end_date': offer.offer.end_date.strftime('%Y-%m-%d')})
        dict_offer.update({'banner_image': offer.offer.banner_image.url})
        dict_offer.update({'original_price': offer.tour_package.tour_cost})
        discount_price = (offer.offer.rate * offer.tour_package.tour_cost) / 100
        dict_offer.update({'offer_price': discount_price})
        del dict_offer['created_at']
        del dict_offer['status']
        row_list.append(dict_offer)
    # main_dict['traveloffer'] = row_list

    # --------------------------------------------------------------------
    offer_instance = InventoryOffers.objects.filter(offer__end_date__gte=now, offer__module='hotel')
    for offer in offer_instance:
        dict_hoteloffer = model_to_dict(offer)
        dict_hoteloffer.update({'package_name': offer.hotel_inventory.room_name})
        dict_hoteloffer.update({'offer_name': offer.offer.offer_name})
        dict_hoteloffer.update({'rate': offer.offer.rate})
        dict_hoteloffer.update({'description': offer.offer.description})
        dict_hoteloffer.update({'start_date': offer.offer.start_date.strftime('%Y-%m-%d')})
        dict_hoteloffer.update({'end_date': offer.offer.end_date.strftime('%Y-%m-%d')})
        dict_hoteloffer.update({'banner_image': offer.offer.banner_image.url})
        dict_hoteloffer.update({'original_price': offer.hotel_inventory.price})
        discount_price = (offer.offer.rate * offer.hotel_inventory.price) / 100
        dict_hoteloffer.update({'offer_price': discount_price})
        del dict_hoteloffer['created_at']
        del dict_hoteloffer['status']
        row_list.append(dict_hoteloffer)
    # main_dict['hoteloffer'] = hotel_list

    rental_list = []
    # now = datetime.now().date()
    offer_instance = VehicleOffers.objects.filter(offer__end_date__gte=now, offer__module='rental')
    for offer in offer_instance:
        dict_rentaloffer = model_to_dict(offer)
        dict_rentaloffer.update({'package_name': offer.vehicle_inventory.name})
        dict_rentaloffer.update({'offer_name': offer.offer.offer_name})
        dict_rentaloffer.update({'rate': offer.offer.rate})
        dict_rentaloffer.update({'description': offer.offer.description})
        dict_rentaloffer.update({'start_date': offer.offer.start_date.strftime('%Y-%m-%d')})
        dict_rentaloffer.update({'end_date': offer.offer.end_date.strftime('%Y-%m-%d')})
        dict_rentaloffer.update({'banner_image': offer.offer.banner_image.url})
        dict_rentaloffer.update({'original_price': offer.vehicle_inventory.price})
        discount_price = (offer.offer.rate * offer.vehicle_inventory.price) / 100
        dict_rentaloffer.update({'offer_price': discount_price})
        del dict_rentaloffer['created_at']
        del dict_rentaloffer['status']
        row_list.append(dict_rentaloffer)
        random.shuffle(row_list)

    main_dict['shuffle'] = row_list

    return JsonResponse(main_dict, safe=False)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def hotelInventoryById(request):
    if request.method == "POST":
        inventory_id = request.POST.get('id')
        maindict = {}
        mainlist = []
        if HotelInventory.objects.filter(id=inventory_id).exists():
            inventory = formatInventory(inventory_id)
            mainlist.append(inventory)
        else:
            return JsonResponse('Sorry Matching inventory not found', safe=False)
        maindict['inventoryfromID'] = mainlist
    return JsonResponse(maindict, safe=False)


@csrf_exempt
@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def searchHotelByName(request):
    if request.method == "POST":
        name = request.POST.get('name')
        maindict = {}
        mainlist = []
        childdict = {}
        if name != None:
            if Hotels.objects.filter(name__icontains=name).exists():
                hotels = Hotels.objects.filter(name__icontains=name)
                for hotel in hotels:
                    childdict.update({'id': hotel.id})
                    childdict.update({'name': hotel.name})
                    mainlist.append(childdict)
                    childdict = {}
            else:
                maindict['hotel'] = mainlist
                return JsonResponse(maindict, safe=False)
        else:
            return JsonResponse('Please enter hotel keyword.', safe=False)
        maindict['hotel'] = mainlist
    return JsonResponse(maindict, safe=False)


@csrf_exempt
@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def searchHotelByID(request):
    if request.method == "POST":
        id = request.POST.get('id')
        maindict = {}
        mainlist = []
        childdict = {}
        if id != None:
            if Hotels.objects.filter(id=id).exists():
                maindict['hotel'] = HotelList(id)
            else:
                return JsonResponse('Sorry Matching Hotel not found', safe=False)
        else:
            return JsonResponse('Please enter  correct hotel Id.', safe=False)
    return JsonResponse(maindict, safe=False)


@csrf_exempt
@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def searchCityByName(request):
    if request.method == "POST":
        name = request.POST.get('name')
        maindict = {}
        mainlist = []
        childdict = {}
        if name != None:
            if City.objects.filter(name__icontains=name).exists():
                cities = City.objects.filter(name__icontains=name)
                for city in cities:
                    childdict.update({'id': city.id})
                    childdict.update({'name': city.name})
                    childdict.update({'image': city.image.url})
                    mainlist.append(childdict)
                    childdict = {}
            else:
                maindict['city'] = mainlist
                return JsonResponse(maindict, safe=False)

        else:
            return JsonResponse('Please enter city keyword.', safe=False)

        maindict['city'] = mainlist
    return JsonResponse(maindict, safe=False)


@csrf_exempt
# @permission_classes((IsAuthenticated,))
def getrooomfeatures(request):
    allroomfeatures = HotelRoomFeature.objects.all()
    maindict = {}
    mainlist = []
    sortedlist = []
    for rmf in allroomfeatures:
        rmf_dict = model_to_dict(rmf)
        mainlist.append(rmf_dict)
    # sortedlist = sorted(mainlist, key=lambda k: k['hotel'].get('startingPrice', 0), reverse=False)
    maindict['RoomFeatures'] = mainlist
    data = {
        'maindict': maindict,
        'success': True,

    }
    return JsonResponse(data, safe=False)


def addnewfeatures(request):
    if request.method == 'POST':
        # print(request.POST.get('featureslist[]'))
        features = (request.POST.getlist('featureslist[]'))

        # features = map(str, dict(request.POST)["featureslist[]"])
        # address_instance = HotelAddress.objects.get(hotel_id=address_id)
        # landmarklist = []
        mainllist = []
        mainlist = []

        for feature in features:
            f = HotelRoomFeature()
            f.name = feature.upper()
            f.save()
            mainllist.append(model_to_dict(f))

        # allroomfeatures = HotelRoomFeature.objects.all()
        # for rmf in allroomfeatures:
        #     rmf_dict = model_to_dict(rmf)
        #     mainlist.append(rmf_dict)

            # address_instance.landmarks.add(l)
        #
        # addedlandmarks = HotelAddress.objects.get(hotel_id=address_id).landmarks.filter()
        # for adl in addedlandmarks:
        #     dict_landmark = model_to_dict(adl)
        #     landmarklist.append(dict_landmark)

        data = {
            'success': True,
            'updatedlist': mainllist

        }

        return JsonResponse(data)


@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def offerCard(request):
    main_list = []
    main_dict = {}
    hotel_dict = {}
    travel_dict = {}
    rental_dict = {}
    now = datetime.now()
    # acis - offer assigned to hotel inventory
    hotel_offer_instance = InventoryOffers.objects.filter(offer__end_date__gte=now, offer__module='hotel')
    module = 'Hotel'
    max_discount = hotel_offer_instance.aggregate(Max('offer__rate'))
    number_included = hotel_offer_instance.values('hotel_inventory__hotel').distinct().count()
    banner_image = '/media/hotel_offer_back.jpg'
    hotel_dict.update({'module': module})
    hotel_dict.update({'banner_image': banner_image})
    hotel_dict.update({'number_included': number_included})
    if max_discount['offer__rate__max'] == None:
        hotel_dict.update({'max_discount': 0})
    else:
        hotel_dict.update({'max_discount': max_discount['offer__rate__max']})
    main_list.append(hotel_dict)

    # acis - offer assigned to tour package
    travel_offer_instance = PackageOffers.objects.filter(offer__end_date__gte=now, offer__module='travel_tour')
    module = 'Travel Tour'
    max_discount = travel_offer_instance.aggregate(Max('offer__rate'))
    number_included = travel_offer_instance.values('tour_package').distinct().count()
    banner_image = '/media/travel_offer_back.jpg'
    travel_dict.update({'module': module})
    travel_dict.update({'banner_image': banner_image})
    travel_dict.update({'number_included': number_included})
    if max_discount['offer__rate__max'] == None:
        travel_dict.update({'max_discount': 0})
    else:
        travel_dict.update({'max_discount': max_discount['offer__rate__max']})
    # main_dict['travel'] = travel_dict
    main_list.append(travel_dict)

    # acis - offer assigned to rental
    rental_offer_instance = VehicleOffers.objects.filter(offer__end_date__gte=now, offer__module='rental')
    module = 'Rental'
    max_discount = rental_offer_instance.aggregate(Max('offer__rate'))
    number_included = rental_offer_instance.values('vehicle_inventory').distinct().count()
    banner_image = '/media/rental_offer_back.jpg'
    rental_dict.update({'module': module})
    rental_dict.update({'banner_image': banner_image})
    rental_dict.update({'number_included': number_included})
    if max_discount['offer__rate__max'] == None:
        rental_dict.update({'max_discount': 0})
    else:
        rental_dict.update({'max_discount': max_discount['offer__rate__max']})
    # main_dict['rental'] = rental_dict
    main_list.append(rental_dict)

    main_dict.update({'offers': main_list})
    return JsonResponse(main_dict, safe=False)


from hotel.bedType.models import BedType
from hotel.amenities.models import HotelAmenities
from hotel.hotel_facilities.models import HotelFacilities


# ------------------------To Filter inventory------------------------------------

def allbedpreferences(request):
    hotels_bedtype = BedType.objects.all()
    bedtype_sent = []
    for bedtype in hotels_bedtype:
        dict_bedtype = model_to_dict(bedtype)
        bedtype_sent.append(dict_bedtype)
    return JsonResponse(bedtype_sent, safe=False)


def allroomfacilities(request):
    Roomfacs = HotelAmenities.objects.all()
    room_fac_sent = []
    for fac in Roomfacs:
        dict_fac = model_to_dict(fac)
        dict_fac.update({'image': fac.image.url})
        room_fac_sent.append(dict_fac)
    return JsonResponse(room_fac_sent, safe=False)


def allhotelfacilities(request):
    hotelfacs = HotelFacilities.objects.all()
    hotel_fac_sent = []
    for fac in hotelfacs:
        dict_fac = model_to_dict(fac)
        dict_fac.update({'image': fac.image.url})
        hotel_fac_sent.append(dict_fac)
    return JsonResponse(hotel_fac_sent, safe=False)


def min_maxprice(request):
    min_max_list = []
    min_max_dict = {}
    max_price = HotelInventory.objects.all().aggregate(Max('price'))
    min_price = HotelInventory.objects.all().aggregate(Min('price'))
    min_max_dict['max_price'] = max_price['price__max']
    min_max_dict['min_price'] = min_price['price__min']
    min_max_list.append(min_max_dict)
    return JsonResponse(min_max_dict, safe=False)

# ------------------------To Filter inventory------------------------------------
