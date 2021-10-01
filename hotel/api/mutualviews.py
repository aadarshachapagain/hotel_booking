from django.http import JsonResponse
from rest_framework.decorators import api_view
from hotel.favourites_saved.models import Favourites
from users.models import User
from hotel.address.models import HotelAddress
from hotel.models import Hotels
# from rental.rental_company.models import RentalCompany
# from rental.rental_company_address.models import RentalCompanyAddress
# from travel_tour.tour_company.models import TravelCompany
# from travel_tour.tour_company_address.models import TourCompanyAddress
# from restaurant.restaurant_company.models import RestaurantCompany
# from restaurant.restaurant_company_address.models import RestaurantCompanyAddress
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def addfavourites(request):
    if request.method == "POST":
        module = request.POST.get('module')
        company_id = request.POST.get('company_id')
        token = request.POST.get('token')
        inventory_id = request.POST.get('inventory_id')
        if inventory_id == '':
            inventory_id = 0

        favourite = request.POST.get('favourite')
        saved = request.POST.get('saved')
        user_id = Token.objects.get(key=token).user_id
        if user_id:
            update_fav = Favourites.objects.filter(user_id=user_id, company_id=company_id, inventory_id=inventory_id,
                                                   module=module)
            if update_fav.exists():
                update_fav.update(favourite=favourite, saved=saved)
                return JsonResponse("Updated Sucessfully", safe=False)
            else:
                obj = Favourites()
                obj.user = User.objects.get(id=user_id)
                obj.module = module
                obj.company_id = company_id
                obj.inventory_id = inventory_id
                obj.favourite = favourite
                obj.saved = saved
                obj.save()
        else:
            return JsonResponse("Sorry token doesnot exists", safe=False)

        return JsonResponse("Saved Sucessfully", safe=False)


@api_view(['POST'])
def getfavourites(request):
    if request.method == "POST":
        token = request.POST.get('token')
        user_id = Token.objects.get(key=token).user_id
        inv_sent = []
        all_fav = Favourites.objects.filter(user_id=user_id)

        for fav in all_fav:
            if fav.module == 'Hotel':
                hotel_favs = Favourites.objects.filter(user_id=user_id)
                dict_hotel_fav = {}
                dict_hotel_fav['module'] = 'Hotel'
                dict_hotel_fav['company_id'] = fav.company_id
                dict_hotel_fav['inv_id'] = fav.inventory_id
                dict_hotel_fav['name'] = Hotels.objects.get(id=fav.company_id).name
                dict_hotel_fav['address'] = HotelAddress.objects.get(hotel=fav.company_id).address
                dict_hotel_fav['image'] = Hotels.objects.get(id=fav.company_id).image.url
                dict_hotel_fav['favourite'] = Favourites.objects.get(id=fav.id).favourite
                dict_hotel_fav['saved'] = Favourites.objects.get(id=fav.id).saved

                if dict_hotel_fav not in inv_sent:
                    inv_sent.append(dict_hotel_fav)
            # if fav.module == 'Rental':
            #     dict_rental_fav = {}
            #     dict_rental_fav['module'] = 'Rental'
            #     dict_rental_fav['company_id'] = fav.company_id
            #     dict_rental_fav['inv_id'] = fav.inventory_id
            #     dict_rental_fav['name'] = RentalCompany.objects.get(id=fav.company_id).name
            #     dict_rental_fav['address'] = RentalCompanyAddress.objects.get(company_id=fav.company_id).address
            #     dict_rental_fav['image'] = RentalCompany.objects.get(id=fav.company_id).image.url
            #     dict_rental_fav['favourite'] = Favourites.objects.get(id=fav.id).favourite
            #     dict_rental_fav['saved'] = Favourites.objects.get(id=fav.id).saved
            #
            #     if dict_rental_fav not in inv_sent:
            #         inv_sent.append(dict_rental_fav)
            # if fav.module == 'Travel_tour':
            #     dict_travel_tour_fav = {}
            #     dict_travel_tour_fav['module'] = 'Travel_tour'
            #     dict_travel_tour_fav['company_id'] = fav.company_id
            #     dict_travel_tour_fav['inv_id'] = fav.inventory_id
            #     dict_travel_tour_fav['name'] = TravelCompany.objects.get(id=fav.company_id).name
            #     dict_travel_tour_fav['address'] = TourCompanyAddress.objects.get(company_id=fav.company_id).address
            #     dict_travel_tour_fav['image'] = TravelCompany.objects.get(id=fav.company_id).image.url
            #     dict_travel_tour_fav['favourite'] = Favourites.objects.get(id=fav.id).favourite
            #     dict_travel_tour_fav['saved'] = Favourites.objects.get(id=fav.id).saved
            #
            #     if dict_travel_tour_fav not in inv_sent:
            #         inv_sent.append(dict_travel_tour_fav)
            #
            # if fav.module == 'Restaurant':
            #     dict_restaurant_fav = {}
            #     dict_restaurant_fav['module'] = 'Restaurant'
            #     dict_restaurant_fav['company_id'] = fav.company_id
            #     dict_restaurant_fav['inv_id'] = fav.inventory_id
            #     dict_restaurant_fav['name'] = RestaurantCompany.objects.get(id=fav.company_id).name
            #     dict_restaurant_fav['address'] = RestaurantCompanyAddress.objects.get(company_id=fav.company_id).address
            #     dict_restaurant_fav['image'] = RestaurantCompany.objects.get(id=fav.company_id).image.url
            #     dict_restaurant_fav['favourite'] = Favourites.objects.get(id=fav.id).favourite
            #     dict_restaurant_fav['saved'] = Favourites.objects.get(id=fav.id).saved
            #
            #     if dict_restaurant_fav not in inv_sent:
            #         inv_sent.append(dict_restaurant_fav)

    return JsonResponse(inv_sent, safe=False)
