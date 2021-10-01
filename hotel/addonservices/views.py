from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from hotel.addonservices.models import AddOnServices
from hotel.inventory.models import HotelInventory
from hotel.amenities.models import HotelAmenities
from django.forms import model_to_dict

import decimal
import re


@csrf_exempt
@api_view(['POST'])
def addonservices(request):
    raw_faclist = request.POST['faclist']
    raw_free_fac_list = request.POST['freefaclist']
    clean_faclist = json.loads(raw_faclist)
    clean_free_fac_list = json.loads(raw_free_fac_list)
    inv_id = request.POST['inv_id']
    # freefacs = request.POST['freefaclist[]']
    inv_instance = HotelInventory.objects.get(id=inv_id)

    addedservices = []
    freeaddedservices = []
    list_of_obt_fac = []
    allfaclist = []
    allfacs = AddOnServices.objects.filter(inventory_id=inv_id)

    for fac in allfacs:
        allfaclist.append(fac.amenities.id)

    for facility in clean_faclist:
        list_of_obt_fac.append(int(facility['facid']))

    difference = list(set(allfaclist) - set(list_of_obt_fac))
    for d in difference:
        discard_amenities = HotelAmenities.objects.get(id=d)
        add_on_instance = AddOnServices.objects.get(amenities=discard_amenities,
                                                    inventory=inv_instance)
        add_on_instance.status = False
        add_on_instance.save()

    #  Paid Facilities
    for facility in clean_faclist:
        fac_id = HotelAmenities.objects.get(id=facility['facid'])
        inventory_id = HotelInventory.objects.get(id=inv_id)

        if AddOnServices.objects.filter(amenities=fac_id,
                                        inventory=inventory_id).exists():
            serv_already_exist = AddOnServices.objects.get(amenities=fac_id,
                                                           inventory=inventory_id)
            serv_already_exist.flatorpercent = facility['flatorpercent']
            serv_already_exist.price = facility['facprice']
            serv_already_exist.status = True
            serv_already_exist.save()
        else:
            obj = AddOnServices()
            obj.price = facility['facprice']
            obj.inventory = inv_instance
            obj.amenities = HotelAmenities.objects.get(id=facility['facid'])
            obj.flatorpercent = facility['flatorpercent']
            obj.status = True
            obj.save()
    #  Paid Facilities

    free_fac_id_list = []
    for freefac in clean_free_fac_list:
        id = int(re.search(r'\d+', freefac).group())
        free_fac_id_list.append(id)

    # for free Facilities Create And Update
    for clean_free_fac in free_fac_id_list:
        free_fac_id = HotelAmenities.objects.get(id=clean_free_fac)
        inventory_id = HotelInventory.objects.get(id=inv_id)
        if AddOnServices.objects.filter(amenities=free_fac_id,
                                        inventory=inventory_id).exists():
            free_serv_already_exist = AddOnServices.objects.get(amenities=free_fac_id,
                                                                inventory=inventory_id)
            free_serv_already_exist.price = 0
            free_serv_already_exist.status = True
            free_serv_already_exist.save()
        else:
            obj = AddOnServices()
            obj.price = 0
            obj.inventory = inv_instance
            obj.amenities = HotelAmenities.objects.get(id=clean_free_fac)
            obj.status = True
            obj.save()
    # for free Facilities Create And Update

    addonservices = AddOnServices.objects.filter(inventory_id=inv_id, status=True, price__gt=0)
    freeaddonservices = AddOnServices.objects.filter(inventory_id=inv_id, status=True, price=0)


    for addonserv in addonservices:
        serv_dict = model_to_dict(addonserv)
        addedservices.append(serv_dict)

    for free_serv in freeaddonservices:
        free_serv_dict = model_to_dict(free_serv)
        freeaddedservices.append(free_serv_dict)

    data = {
        'addonservices': addedservices,
        'freeaddonservices': freeaddedservices

    }
    return JsonResponse(data, safe=False)
