import json
from datetime import datetime, timedelta
from itertools import chain

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt

from hotel.inventory.models import HotelInventory
from hotel.inventoryUpdate.models import InventoryUpdate
from hotel.inventoryUpdate.services import api_call_for_booking_information
from hotel.models import Hotels
from travel.businessPolicies import send_policies


@csrf_exempt
def room_separation(request):
    """
    @param request: request from the calendar
    @return: redirect to respective function
    @logic: if cat = all redirect to getHotelDetail else getRoomCategory
    """
    if request.method == 'POST':
        room_cat_from_request = request.POST.get('room_category')
        if room_cat_from_request == "all":
            data = get_all_rooms(request)
        else:
            data = get_room_detail_by_category(request)
        return JsonResponse(data, safe=False)


@csrf_exempt
def get_all_rooms(request):
    """
    @param request: request from the calendar
    @return: returns JSON response of all rooms
    """
    main_dict = {}
    inventory_list = []
    inventory_dict = {}
    hotels = ''
    if request.method == 'POST':
        start_date_from_request = request.POST.get('start_date')
        end_date_from_request = request.POST.get('end_date')
        hotel_id_from_request = request.POST.get('hotel_id')

        # Convert string to date format, to iterate for loop using date range
        start_date_manipulation = datetime.strptime(start_date_from_request, "%Y-%m-%d").date()
        if end_date_from_request == "undefined":
            end_date_manipulation = start_date_manipulation
        else:
            end_date_manipulation = datetime.strptime(end_date_from_request, "%Y-%m-%d").date() - timedelta(days=1)

        # filter inventories from the inventoryUpdate table that matches the date range
        matching_inventories_from_sql = InventoryUpdate.objects.filter(hotel=hotel_id_from_request)

        # loop in date range
        matching_inventories_with_date = ''
        matching_inventories_with_date_id = ''
        delta = end_date_manipulation - start_date_manipulation
        for i in range(delta.days + 1):
            perfect_date = start_date_manipulation + timedelta(days=i)
            matching_inventories_with_date = matching_inventories_from_sql.filter(date=perfect_date)
            matching_inventories_with_date_id = matching_inventories_from_sql.filter(date=perfect_date).values(
                'inventory__id')

        # subtracting total matched inventories with total matched inventories with date
        remaining_matching_inventories = matching_inventories_from_sql.exclude(
            inventory__id__in=matching_inventories_with_date_id)
        matching_inventories_without_date = remaining_matching_inventories.filter(date=None)
        matching_inventories_final_list = list(
            chain(matching_inventories_with_date, matching_inventories_without_date))

        # API structuring
        modal_id = 1
        for matching_inventory_final_list in matching_inventories_final_list:
            inventory_dict.update({"modal_id": modal_id})
            get_all_policies = send_policies()
            get_all_policies = json.loads(get_all_policies)
            for item in get_all_policies:
                if matching_inventory_final_list.cancellation_type == item.get('name'):
                    item['status'] = 'checked'
                    break
                else:
                    item['status'] = ''
            modal_id += 1
            if end_date_manipulation == start_date_manipulation:
                current_bedandbreakfast_plan = matching_inventory_final_list.bedandbreakfast_plan
                current_european_plan = matching_inventory_final_list.european_plan
            else:
                current_bedandbreakfast_plan = "multiple"
                current_european_plan = "multiple"
            flag, color = check_for_booking_before(matching_inventory_final_list.hotel.id,
                                                   matching_inventory_final_list.inventory.id, start_date_manipulation,
                                                   end_date_manipulation)
            inventory_dict.update(
                {
                    "id": matching_inventory_final_list.inventory.id,
                    "hotel_id": matching_inventory_final_list.hotel.id,
                    "name": matching_inventory_final_list.inventory.room_name,
                    "current_bedandbreakfast_plan": current_bedandbreakfast_plan,
                    "bedandbreakfast_plan": matching_inventory_final_list.inventory.bedandbreakfast_plan,
                    "current_european_plan": current_european_plan,
                    "european_plan": matching_inventory_final_list.inventory.european_plan,
                    "start_date": start_date_from_request,
                    "end_date": end_date_manipulation,
                    "policies": get_all_policies,
                    "flag": flag,
                    "color": color,
                    "is_available":matching_inventory_final_list.is_available
                },
            )
            inventory_list.append(inventory_dict)
            inventory_dict = {}
        main_dict.update({"inventories": inventory_list})
        main_dict.update({"status": "all"})
        return main_dict


@csrf_exempt
def get_room_detail_by_category(request):
    """
    @param request: request from the calendar
    @return: returns JSON response of category
    """

    if request.method == 'POST':
        start_date_from_request = request.POST.get('start_date')
        end_date_from_request = request.POST.get('end_date')
        if end_date_from_request == "undefined":
            end_date_manipulation = ""
        else:
            end_date_manipulation = datetime.strptime(end_date_from_request, "%Y-%m-%d").date() - timedelta(days=1)
        hotel_id_from_request = request.POST.get('hotel_id')
        room_cat_from_request = request.POST.get('room_category')
        inventory_categories_from_sql = HotelInventory.objects.filter(hotel_id=hotel_id_from_request).values(
            'roomtype__name',
            'roomtype__id').distinct().annotate(inv_count=Count('roomtype'))
        main_dict = {}
        room_cat_list = []
        modal_id = 1
        for room_name in inventory_categories_from_sql:
            room_cat_dict = {}
            room_cat_dict.update(
                {
                    "id": room_name["roomtype__id"],
                    "category": room_name["roomtype__name"],
                    "inventory_count": room_name["inv_count"],
                    "start_date": start_date_from_request,
                    "end_date": end_date_manipulation,
                    "modal_id": modal_id,
                    "hotel_id": hotel_id_from_request,

                }
            )
            modal_id = modal_id + 1
            room_cat_list.append(room_cat_dict)
        main_dict.update({"room_categories": room_cat_list})
        main_dict.update({"status": "category"})
        return main_dict


@csrf_exempt
def separation_hotel_during_update(request):
    """
    @param request: inputs from form named inventory price update
    @return: date
    @logic: if cat then redirect to cat_update else :func:`~hotel.inventoryUpdate.views.update_inventory_detail`
    """
    if request.method == 'POST':
        flag = request.POST.get('flag')
        if flag == "category":
            data = update_inventory_category(request)
        else:
            data = update_inventory_detail(request)
        return JsonResponse(data, safe=False)


@csrf_exempt
def update_inventory_category(request):
    """
    @param request: inputs from form named inventory price update by category
    @return: date
    @logic: updates the inventory_update table according to the provided data
    """
    if request.method == 'POST':
        start_date_from_request = request.POST.get('start_date')
        end_date_from_request = request.POST.get('end_date')
        bb_plan_rate_from_request = request.POST.get('bedandbreakfast_plan')
        ep_plan_rate_from_request = request.POST.get('european_plan')
        hotel_id_from_request = request.POST.get('hotel')
        category_id_from_request = request.POST.get('category')

        # request policy's conditions from JSON file
        temp = send_policies()
        all_items = json.loads(temp)

        # calculate EP, BB price according to pre-defined policies
        # for now : 2020-08-23 By:Acis
        policy = "Non-refundable booking"
        for item in all_items:
            if item['name'] == policy:
                rate = item['room_rate_number']
                operator = item['room_rate_operator']
                bb_rate = float(bb_plan_rate_from_request)
                ep_rate = float(ep_plan_rate_from_request)

                if operator == 'sub':
                    bb_update = bb_rate - ((rate * bb_rate) / 100)
                    ep_update = ep_rate - ((rate * ep_rate) / 100)
                elif operator == 'add':
                    bb_update = bb_rate + ((rate * bb_rate) / 100)
                    ep_update = ep_rate + ((rate * ep_rate) / 100)
                else:
                    bb_update = bb_rate
                    ep_update = ep_rate
                break

        # find all the inventories that falls under the provided category
        matching_inventories_by_category = HotelInventory.objects.filter(hotel=hotel_id_from_request,
                                                                         roomtype=category_id_from_request)

        # Convert string to date format, to iterate for loop using date range
        start_date_manipulation = datetime.strptime(start_date_from_request, "%Y-%m-%d").date()
        if end_date_from_request:
            end_date_manipulation = datetime.strptime(end_date_from_request, "%Y-%m-%d").date()
        else:
            end_date_manipulation = start_date_manipulation
        delta = end_date_manipulation - start_date_manipulation
        # for now : 2020-08-23 By:Acis
        room_count = 1
        for i in range(delta.days + 1):
            perfect_date = start_date_manipulation + timedelta(days=i)

            # use the filtered inventories to search in inventoryUpdate table
            for matching_inventory_by_category in matching_inventories_by_category:
                try:
                    old_instance = InventoryUpdate.objects.get(hotel=hotel_id_from_request,
                                                               date=perfect_date,
                                                               inventory=matching_inventory_by_category.id,
                                                               cancellation_type=policy)
                    flag = check_for_booking_after(hotel_id_from_request, old_instance.inventory_id,
                                                   perfect_date)
                    if flag == "available":
                        InventoryUpdate.objects.filter(hotel=hotel_id_from_request,
                                                       inventory=matching_inventory_by_category.id,
                                                       date=perfect_date, cancellation_type=policy).update(
                            date=perfect_date,
                            bedandbreakfast_plan=bb_update,
                            european_plan=ep_update)
                    else:
                        continue
                except ObjectDoesNotExist:
                    old_instance = InventoryUpdate.objects.get(hotel=hotel_id_from_request,
                                                               date=None,
                                                               inventory=matching_inventory_by_category.id,
                                                               cancellation_type=policy)
                    flag = check_for_booking_after(hotel_id_from_request, old_instance.inventory_id,
                                                   perfect_date)
                    if flag == "available":
                        new_instance = InventoryUpdate()
                        new_instance.date = perfect_date
                        new_instance.status = None
                        new_instance.bedandbreakfast_plan = bb_update or 0.0
                        new_instance.european_plan = ep_update or 0.0
                        new_instance.hotel = Hotels.objects.get(id=hotel_id_from_request)
                        new_instance.inventory = HotelInventory.objects.get(id=matching_inventory_by_category.id)
                        new_instance.quantity = room_count
                        new_instance.cancellation_type = policy
                        new_instance.save()
                    else:
                        continue
        return {'date': start_date_from_request}


@csrf_exempt
def update_inventory_detail(request):
    """
    @param request: inputs from form named inventory price update
    @return: date
    @logic: updates the inventory_update table according to the provided data
    """
    if request.method == 'POST':
        start_date_from_request = request.POST.get('start_date')
        end_date_from_request = request.POST.get('end_date')
        bb_plan_rate_from_request = request.POST.get('bedandbreakfast_plan')
        ep_plan_rate_from_request = request.POST.get('european_plan')
        hotel_id_from_request = request.POST.get('hotel')
        inventory_id_from_request = request.POST.get('inventory')
        policy_from_request = request.POST.get('policy')

        # request policy's conditions from JSON file
        temp = send_policies()
        all_items = json.loads(temp)

        for item in all_items:
            if item['name'] == policy_from_request:
                rate = item['room_rate_number']
                operator = item['room_rate_operator']
                bb_rate = float(bb_plan_rate_from_request)
                ep_rate = float(ep_plan_rate_from_request)

                if operator == 'sub':
                    bb_update = bb_rate - ((rate * bb_rate) / 100)
                    ep_update = ep_rate - ((rate * ep_rate) / 100)
                elif operator == 'add':
                    bb_update = bb_rate + ((rate * bb_rate) / 100)
                    ep_update = ep_rate + ((rate * ep_rate) / 100)
                else:
                    bb_update = bb_rate
                    ep_update = ep_rate
                break

        # find all the inventories that falls under the provided category
        # will return multiple (date-wise, policy-wise)
        matching_inventories_by_id = InventoryUpdate.objects.filter(hotel=hotel_id_from_request,
                                                                    inventory=inventory_id_from_request)

        # Convert string to date format, to iterate for loop using date range
        start_date_manipulation = datetime.strptime(start_date_from_request, "%Y-%m-%d").date()
        if end_date_from_request:
            end_date_manipulation = datetime.strptime(end_date_from_request, "%Y-%m-%d").date()
        else:
            end_date_manipulation = start_date_manipulation
        delta = end_date_manipulation - start_date_manipulation
        # for now : 2020-08-23 By:Acis
        room_count = 1
        # TODO: Need to handle cases for remaining policy, for now the front-end only sends Non-refundable booking as
        #  policy. If previous policy was refundable, then the algo fails because the param: policy_from_request has
        #  non-refundable value.
        for i in range(delta.days + 1):
            perfect_date = start_date_manipulation + timedelta(days=i)

            try:
                # filters one entry which matches the date and policy
                old_instance = matching_inventories_by_id.get(date=perfect_date, cancellation_type=policy_from_request)
                flag = check_for_booking_after(hotel_id_from_request, old_instance.inventory_id,
                                               perfect_date)

                if flag == "available":
                    old_instance.date = perfect_date
                    old_instance.bedandbreakfast_plan = bb_update
                    old_instance.european_plan = ep_update
                    old_instance.save()
                else:
                    continue
            except ObjectDoesNotExist:
                # filters one entry with date = null i.e. universal price and policy = same as previous
                old_instance = matching_inventories_by_id.get(date=None, cancellation_type=policy_from_request)
                flag = check_for_booking_after(hotel_id_from_request, old_instance.inventory_id,
                                               perfect_date)
                if flag == "available":
                    new_instance = InventoryUpdate()
                    new_instance.date = perfect_date
                    new_instance.status = None
                    new_instance.bedandbreakfast_plan = bb_update or 0.0
                    new_instance.european_plan = ep_update or 0.0
                    new_instance.hotel = Hotels.objects.get(id=hotel_id_from_request)
                    new_instance.inventory = HotelInventory.objects.get(id=inventory_id_from_request)
                    new_instance.quantity = room_count
                    new_instance.cancellation_type = policy_from_request
                    new_instance.save()
                else:
                    continue
        return {'date': start_date_from_request}


@csrf_exempt
def check_for_booking_before(hotel_id, inventory_id, start_date, end_date):
    get_all_booking = api_call_for_booking_information(hotel_id)
    flag = ''
    color = ''
    if get_all_booking == '':
        flag = 'error'
        color = 'red'
    else:
        delta = end_date - start_date
        for i in range(delta.days + 1):
            perfect_date = start_date + timedelta(days=i)
            expected_result = [d for d in get_all_booking if
                               d['room_no'] == inventory_id and (d['start'] == perfect_date or d[
                                   'end'] == perfect_date or d['start'] < perfect_date < d['end'])]
            if expected_result:
                flag = "This room is booked for some of the dates that you have selected. " \
                       "We will update the price of the room only for available dates."
                color = "red"
                break
            else:
                flag = "This room is not booked for the selected date range. We will update the price of the " \
                       "room for all the dates."
                color = "green"
    return flag, color


@csrf_exempt
def check_for_booking_after(hotel_id, inventory_id, perfect_date):
    get_all_booking = api_call_for_booking_information(hotel_id)
    expected_result = [d for d in get_all_booking if
                       d['room_no'] == inventory_id and (d['start'] == perfect_date or d[
                           'end'] == perfect_date or d['start'] < perfect_date < d['end'])]
    if expected_result:
        flag = "booked"
    else:
        flag = "available"
    return flag


@csrf_exempt
def condition_to_update_availability(request):
    """
    @param request: request from the calendar
    @return: redirect to respective function
    @logic: if cat = all redirect to getHotelDetail else getRoomCategory
    """
    if request.method == 'POST':
        room_cat_from_request = request.POST.get('room_category')
        if room_cat_from_request == "all":
            data = update_inventory_availability_by_id(request)
        else:
            data = update_inventory_availability_by_category(request)
        return JsonResponse(data, safe=False)


@csrf_exempt
def update_inventory_availability_by_category(request):
    """
    @param request: inputs from form named inventory price update by category
    @return: date
    @logic: updates the inventory_update table according to the provided data
    """
    if request.method == 'POST':
        start_date_from_request = request.POST.get('start_date')
        end_date_from_request = request.POST.get('end_date')
        hotel_id_from_request = request.POST.get('hotel')
        category_id_from_request = request.POST.get('category')
        status_from_request = request.POST.get('is_available')

        # request policy's conditions from JSON file
        temp = send_policies()
        all_items = json.loads(temp)

        # for now : 2020-08-23 By:Acis
        policy = "Non-refundable booking"

        # find all the inventories that falls under the provided category
        matching_inventories_by_category = HotelInventory.objects.filter(hotel=hotel_id_from_request,
                                                                         roomtype=category_id_from_request)

        # Convert string to date format, to iterate for loop using date range
        start_date_manipulation = datetime.strptime(start_date_from_request, "%Y-%m-%d").date()
        if end_date_from_request:
            end_date_manipulation = datetime.strptime(end_date_from_request, "%Y-%m-%d").date()
        else:
            end_date_manipulation = start_date_manipulation
        delta = end_date_manipulation - start_date_manipulation
        # for now : 2020-08-23 By:Acis
        room_count = 1
        for i in range(delta.days + 1):
            perfect_date = start_date_manipulation + timedelta(days=i)

            # use the filtered inventories to search in inventoryUpdate table
            for matching_inventory_by_category in matching_inventories_by_category:
                try:
                    old_instance = InventoryUpdate.objects.get(hotel=hotel_id_from_request,
                                                               date=perfect_date,
                                                               inventory=matching_inventory_by_category.id,
                                                               cancellation_type=policy)
                    flag = check_for_booking_after(hotel_id_from_request, old_instance.inventory_id,
                                                   perfect_date)

                    if flag == "available":
                        InventoryUpdate.objects.filter(hotel=hotel_id_from_request,
                                                       inventory=matching_inventory_by_category.id,
                                                       date=perfect_date, cancellation_type=policy).update(
                            is_available=status_from_request)
                    else:
                        continue
                except ObjectDoesNotExist:
                    old_instance = InventoryUpdate.objects.get(hotel=hotel_id_from_request,
                                                               date=None,
                                                               inventory=matching_inventory_by_category.id,
                                                               cancellation_type=policy)

                    flag = check_for_booking_after(hotel_id_from_request, old_instance.inventory_id,
                                                   perfect_date)
                    if flag == "available":
                        new_instance = InventoryUpdate()
                        new_instance.date = perfect_date
                        new_instance.status = None
                        new_instance.is_available = status_from_request
                        new_instance.bedandbreakfast_plan = old_instance.bedandbreakfast_plan
                        new_instance.european_plan = old_instance.bedandbreakfast_plan
                        new_instance.hotel = Hotels.objects.get(id=hotel_id_from_request)
                        new_instance.inventory = HotelInventory.objects.get(id=matching_inventory_by_category.id)
                        new_instance.quantity = room_count
                        new_instance.cancellation_type = policy
                        new_instance.save()
                    else:
                        continue
        return {'date': start_date_from_request}


@csrf_exempt
def update_inventory_availability_by_id(request):
    """
    @param request: inputs from form named inventory price update
    @return: date
    @logic: updates the inventory_update table according to the provided data
    """
    if request.method == 'POST':
        start_date_from_request = request.POST.get('start_date')
        end_date_from_request = request.POST.get('end_date')
        hotel_id_from_request = request.POST.get('hotel')
        inventory_id_from_request = request.POST.get('inventory')
        policy_from_request = 'Non-refundable booking'
        is_available_from_request = request.POST.get('is_available')

        # find all the inventories that falls under the provided category
        # will return multiple (date-wise, policy-wise)
        matching_inventories_by_id = InventoryUpdate.objects.filter(hotel=hotel_id_from_request,
                                                                    inventory=inventory_id_from_request)

        # Convert string to date format, to iterate for loop using date range
        start_date_manipulation = datetime.strptime(start_date_from_request, "%Y-%m-%d").date()
        if end_date_from_request:
            end_date_manipulation = datetime.strptime(end_date_from_request, "%Y-%m-%d").date()
        else:
            end_date_manipulation = start_date_manipulation
        delta = end_date_manipulation - start_date_manipulation
        # for now : 2020-08-23 By:Acis
        room_count = 1
        # TODO: Need to handle cases for remaining policy, for now the front-end only sends Non-refundable booking as
        #  policy. If previous policy was refundable, then the algo fails because the param: policy_from_request has
        #  non-refundable value.
        for i in range(delta.days + 1):
            perfect_date = start_date_manipulation + timedelta(days=i)

            try:
                # filters one entry which matches the date and policy
                old_instance = matching_inventories_by_id.get(date=perfect_date, cancellation_type=policy_from_request)
                flag = check_for_booking_after(hotel_id_from_request, old_instance.inventory_id,
                                               perfect_date)

                if flag == "available":
                    old_instance.date = perfect_date
                    old_instance.is_available = is_available_from_request
                    old_instance.save()
                else:
                    continue
            except ObjectDoesNotExist:
                # filters one entry with date = null i.e. universal price and policy = same as previous
                old_instance = matching_inventories_by_id.get(date=None, cancellation_type=policy_from_request)
                flag = check_for_booking_after(hotel_id_from_request, old_instance.inventory_id,
                                               perfect_date)
                if flag == "available":
                    new_instance = InventoryUpdate()
                    new_instance.date = perfect_date
                    new_instance.status = None
                    new_instance.is_available = is_available_from_request
                    new_instance.bedandbreakfast_plan = old_instance.bedandbreakfast_plan
                    new_instance.european_plan = old_instance.european_plan
                    new_instance.hotel = Hotels.objects.get(id=hotel_id_from_request)
                    new_instance.inventory = HotelInventory.objects.get(id=inventory_id_from_request)
                    new_instance.quantity = room_count
                    new_instance.cancellation_type = policy_from_request
                    new_instance.save()
                else:
                    continue
        return {'date': start_date_from_request}
# for future use
    # def get_hotel_detail(request):
    #     main_dict = {}
    #     hotel_dict = {}
    #     hotel_list = []
    #     inventory_dict = {}
    #     hotels = ''
    #     if request.method == 'POST':
    #         start_date_from_request = request.POST.get('start_date')
    #         end_date_from_request = request.POST.get('end_date')
    #         hotel_id = request.POST.get('hotel_id')
    #         token = request.META.get('HTTP_AUTHORIZATION')
    #         if token:
    #             cleartoken = (token.split('Token '))
    #             user_id = Token.objects.get(key=cleartoken[1]).user_id
    #             user_instance = User.objects.get(id=user_id)
    #             types = user_instance.account_type.filter()
    #             request_user_id = user_id
    #         else:
    #             types = request.user.account_type.filter()
    #             request_user_id = request.user.id
    #
    #         # future
    #         # for typ in types:
    #         # 	if 'hotel_owner' in typ.type:
    #         # 		hotels = Hotels.objects.filter(owner_id=request_user_id, is_active=1)
    #         # 	elif 'hotel_staff' in typ.type:
    #         # 		id = request_user_id
    #         # 		company_id = StaffProfile.objects.values_list('company_id', flat=True).get(user=id)
    #         # 		hotels = Hotels.objects.filter(id=company_id)
    #
    #         hotels = Hotels.objects.filter(id=hotel_id)
    #         for hotel in hotels:
    #             hotel_dict.update({"id": hotel.id})
    #             hotel_dict.update({"name": hotel.prop_id.business_name})
    #             hotel_dict.update({"image": hotel.image.url})
    #             # inventories
    #             inventories = hotel.inventory.filter()
    #             inventory_list = []
    #             modal_id = 1
    #             for inventory in inventories:
    #                 count = InventoryUpdate.objects.filter(hotel=inventory.hotel_id, inventory=inventory.id,
    #                                                        date=start_date_from_request).count()
    #
    #                 if count == 0:
    #                     count_again = 0
    #                     count_again = InventoryUpdate.objects.filter(hotel=inventory.hotel_id, inventory=inventory.id,
    #                                                                  date=None).count()
    #
    #                     if count_again != 0:
    #                         array_inventory_update_new = InventoryUpdate.objects.filter(hotel=inventory.hotel_id,
    #                                                                                     inventory=inventory.id, date=None)
    #                         for new_inv_instance in array_inventory_update_new:
    #                             temp = send_policies()
    #                             all_items = json.loads(temp)
    #                             for item in all_items:
    #                                 if new_inv_instance.cancellation_type == item.get('name'):
    #                                     item['status'] = 'checked'
    #                                     break
    #                                 else:
    #                                     item['status'] = ''
    #                             inventory_dict.update({'policies': all_items})
    #                             inventory_dict.update({"modal_id": modal_id})
    #                             modal_id += 1
    #                             inventory_dict.update({"id": inventory.id})
    #                             inventory_dict.update({"hotel": inventory.hotel_id})
    #                             inventory_dict.update({"name": inventory.room_name})
    #                             booked_inventories = ModuleBooking.objects.filter(inventory_id=inventory.id,
    #                                                                               start_date=start_date_from_request)
    #                             booked_inventory = booked_inventories.aggregate(Sum('quantity'))
    #                             if booked_inventory['quantity__sum'] == None:
    #                                 a = 0
    #                                 inventory_dict.update({'booked': 0})
    #                             else:
    #                                 a = booked_inventory['quantity__sum']
    #
    #                             inventory_dict.update({"total_room": inventory.no_of_rooms - a})
    #                             inventory_dict.update({'current_room': inventory.no_of_rooms - a})
    #                             # inventory_dict.update({'unavailable': 0})
    #                             inventory_dict.update({'status': ''})
    #                             inventory_dict.update({'bedandbreakfast_plan': new_inv_instance.bedandbreakfast_plan})
    #                             inventory_dict.update({'european_plan': new_inv_instance.european_plan})
    #                             inventory_dict.update({'base_european_plan': inventory.european_plan})
    #                             inventory_dict.update({'base_bedandbreakfast_plan': inventory.bedandbreakfast_plan})
    #                             inventory_dict.update({'start_date_from_request': start_date_from_request})
    #                             inventory_dict.update({'cancellation': new_inv_instance.cancellation_type})
    #                             inventory_dict.update({'booked': a})
    #                             inventory_list.append(inventory_dict)
    #                             inventory_dict = {}
    #                 else:
    #                     array_inventory_update = InventoryUpdate.objects.filter(hotel=inventory.hotel_id,
    #                                                                             inventory=inventory.id, date=start_date_from_request)
    #
    #                     for new_instance in array_inventory_update:
    #                         temp = send_policies()
    #                         all_items = json.loads(temp)
    #                         for item in all_items:
    #                             if new_instance.cancellation_type == item.get('name'):
    #                                 item['status'] = 'checked'
    #                                 break
    #                             else:
    #                                 item['status'] = ''
    #
    #                         booked_inventories = ModuleBooking.objects.filter(inventory_id=inventory.id, start_date=start_date_from_request)
    #                         booked_inventory = booked_inventories.aggregate(Sum('quantity'))
    #                         if booked_inventory['quantity__sum'] == None:
    #                             a = 0
    #                             inventory_dict.update({'booked': 0})
    #                         else:
    #                             a = booked_inventory['quantity__sum']
    #                         inventory_dict.update({'policies': all_items})
    #                         inventory_dict.update({"modal_id": modal_id})
    #                         modal_id += 1
    #                         inventory_dict.update({"id": inventory.id})
    #                         inventory_dict.update({"hotel": inventory.hotel_id})
    #                         inventory_dict.update({"name": inventory.room_name})
    #                         inventory_dict.update({'current_room': 1})
    #                         # inventory_dict.update({'unavailable': new_instance.quantity})
    #                         inventory_dict.update({'status': new_instance.status})
    #                         inventory_dict.update({'cancellation': new_instance.cancellation_type})
    #                         inventory_dict.update({'bedandbreakfast_plan': new_instance.bedandbreakfast_plan})
    #                         inventory_dict.update({'european_plan': new_instance.european_plan})
    #                         inventory_dict.update({'base_european_plan': inventory.european_plan})
    #                         inventory_dict.update({'base_bedandbreakfast_plan': inventory.bedandbreakfast_plan})
    #                         inventory_dict.update({'start_date_from_request': start_date_from_request})
    #                         inventory_dict.update({"total_room": inventory.no_of_rooms - a})
    #                         inventory_dict.update({'booked': a})
    #                         inventory_list.append(inventory_dict)
    #                         inventory_dict = {}
    #             hotel_dict.update({"inventories": inventory_list})
    #             hotel_list.append(hotel_dict)
    #             hotel_dict = {}
    #         main_dict.update({"hotels": hotel_list})
    #         return main_dict
    #         # return JsonResponse(main_dict, safe=False)


