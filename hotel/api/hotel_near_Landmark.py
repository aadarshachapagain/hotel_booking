import geopy.distance
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from booking.api.utils import paginate
from booking.utils import HotelList
from hotel.address.models import HotelAddress
from hotel.city.models import City
from hotel.landmark.models import Landmark
from hotel.models import Hotels


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def gethotelnearLandmark(request):
    if request.method == 'POST':
        landmark = request.POST.get('landmark')
        limit = request.POST.get('limit')
        page = request.POST.get('page')

        print(landmark)

        hotel_list = []

        if Landmark.objects.filter(name=landmark):
            landmark_list = Landmark.objects.get(name=landmark)
            landmark_latitude = Landmark.objects.get(name=landmark).latitude
            landmark_longitude = Landmark.objects.get(name=landmark).longitude

            landmark_xy = (landmark_latitude, landmark_longitude)

            print("landmark geo")
            print(landmark_xy)

            landmark_id = Landmark.objects.get(name=landmark).id
            hotel_near_landmark_list = HotelAddress.objects.filter(landmarks=landmark_id)
            print(hotel_near_landmark_list)

            for hotel in hotel_near_landmark_list:
                dict_distance_landmark_hotel = {}
                hotel_xy = (hotel.latitude, hotel.longitude)
                print('hotel geo')
                print(hotel_xy)

                distance = geopy.distance.vincenty(landmark_xy, hotel_xy).km
                print(distance)

                dict_distance_landmark_hotel['distancefromlandmark'] = distance
                dict_distance_landmark_hotel['hotel'] = HotelList(hotel.hotel)

                hotel_list.append(dict_distance_landmark_hotel)
                print(hotel_list)

            sortedlist = sorted(hotel_list, key=lambda k: k['distancefromlandmark'], reverse=False)

            data = paginate(sortedlist, limit, page)
            if not data:
                return HttpResponse('Sorry requested page donot exist')

    return JsonResponse(data, safe=False)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def globalSearch(request):
    if request.method == 'POST':
        global_search = request.POST.get('global_search')
        limit = request.POST.get('limit')
        page = request.POST.get('page')

        global_search_list = []

        if Landmark.objects.filter(name__icontains=global_search):
            landmark_list = Landmark.objects.filter(name__icontains=global_search)

            for landmark in landmark_list:
                dict_landmark = {}
                dict_landmark['id'] = landmark.id
                dict_landmark['name'] = landmark.name
                dict_landmark['category'] = 'landmark'
                global_search_list.append(dict_landmark)

        if City.objects.filter(name__icontains=global_search):
            city_list = City.objects.filter(name__icontains=global_search)

            for city in city_list:
                dict_city = {}
                dict_city['id'] = city.id
                dict_city['name'] = city.name
                dict_city['category'] = 'city'
                global_search_list.append(dict_city)

        if Hotels.objects.filter(name__icontains=global_search):
            hotel_list = Hotels.objects.filter(name__icontains=global_search)

            for hotel in hotel_list:
                dict_hotel = {}
                dict_hotel['id'] = hotel.id
                dict_hotel['name'] = hotel.name
                dict_hotel['category'] = 'hotel'
                global_search_list.append(dict_hotel)

        data = paginate(global_search_list, limit, page)
        if not data:
            return HttpResponse('Sorry requested page donot exist')

        return JsonResponse(data, safe=False)
