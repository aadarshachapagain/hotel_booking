# from django.http import JsonResponse, HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
#
# from booking.utils import check_booking_available
# from rental.vehicleInventory.models import VehicleInventory
# from rental.vehicleInventory.utils import VehicleInventoryFormat
# from booking.module_booking.models import ModuleBooking
# from rental.vehicleCategory.models import VehicleCategory
# from rental.vehicleDetail.models import VehicleDetail
# from itertools import chain
#
#
# # @csrf_exempt
# # @api_view(['POST'])
# # @permission_classes((IsAuthenticated,))
# # def available_rental(request):
# #     if request.method == "POST":
# #
# #         req_city = int(request.POST.get('city'))
# #
# #         check_in = request.POST.get('start_date')
# #         check_out = request.POST.get('end_date')
# #         req_count = int(request.POST.get('req_count'))
# #
# #         mainlist = []
# #         maindict = {}
# #         vehiclesidfrombooking = []
# #         vehinvsid_ByCity = []
# #         notbookedinv = []
# #         vehinvs_ByCity = []
# #         arrayfilterbycat = []
# #         cat_id = int(request.POST.get('cat_id'))
# #
# #         # cat_id = 1
# #         # req_city = 1
# #         # check_in = '2019-07-01'
# #         # check_out = '2019-07-15'
# #         # req_count = 1
# #         # Vehicle_category=VehicleD
# #
# #         array = []
# #         Vehicle_category = VehicleCategory.objects.get(id=cat_id)
# #         Vehicle_detail_by_cat = VehicleDetail.objects.filter(vehicle_category_id=Vehicle_category.id)
# #
# #
# #         for det in Vehicle_detail_by_cat:
# #             detailed_invs = VehicleInventory.objects.filter(vehicle_detail_id=det.id)
# #
# #             for det_inv in detailed_invs:
# #                 array.append(det_inv)
# #
# #         for a in array:
# #             arrayfilterbycat.append(a.id)
# #         vehicleinvbycat = VehicleInventory.objects.filter(id__in=arrayfilterbycat)
# #
# #         if VehicleInventory.objects.filter(vehicle_location_id=req_city).exists():
# #             vehinvs_ByCity = vehicleinvbycat.filter(vehicle_location_id=req_city)
# #
# #         vehiclesfrom_mbooking = ModuleBooking.objects.filter(module_name='rental')
# #
# #         for inv in vehiclesfrom_mbooking:
# #             vehiclesidfrombooking.append(inv.inventory_id)
# #
# #         for inv in vehinvs_ByCity:
# #             vehinvsid_ByCity.append(inv.id)
# #
# #         notbookedinv = list(set(vehinvsid_ByCity) - set(vehiclesidfrombooking))
# #         bookedinv = list(set(vehinvsid_ByCity) & set(vehiclesidfrombooking))
# #         distinctinv = []
# #
# #         for unique in bookedinv:
# #             if unique not in distinctinv:
# #                 distinctinv.append(unique)
# #
# #         bookedinvlist = []
# #         arr = []
# #         dept = []
# #         room = []
# #         flag = []
# #
# #         for binv in distinctinv:
# #             vehiclesbooked = ModuleBooking.objects.get(inventory_id=binv, module_name='rental')
# #             bookedinvlist.append(vehiclesbooked)
# #
# #         for vehicle in bookedinvlist:
# #             singlevechinvlist = ModuleBooking.objects.filter(inventory_id=binv, module_name='rental')
# #             for singlevechinv in singlevechinvlist:
# #                 arr.append(vehicle.start_date.strftime('%Y-%m-%d'))
# #                 dept.append(vehicle.end_date.strftime('%Y-%m-%d'))
# #                 room.append(vehicle.quantity)
# #                 flag.append(1)
# #
# #             arr.append(check_in)
# #             dept.append(check_out)
# #             flag.append(0)
# #             room.append(req_count)
# #             n = len(arr)
# #             k = int(VehicleInventory.objects.get(id=vehicle.inventory_id).avail_number)
# #
# #             if check_booking_available(arr, dept, n, k, room, flag):
# #                 roomavailable = check_booking_available(arr, dept, n, k, room, flag)
# #                 formatted_vehicleinv = VehicleInventoryFormat(vehicle.inventory_id)
# #                 formatted_vehicleinv['vehicleforbooking'] = roomavailable
# #                 mainlist.append(formatted_vehicleinv)
# #             arr = []
# #             dept = []
# #             room = []
# #             flag = []
# #
# #         for inv in notbookedinv:
# #             formatted_Vehicle = VehicleInventoryFormat(inv)
# #             no_of_invs = VehicleInventory.objects.get(id=inv).avail_number
# #             formatted_Vehicle['vehicleforbooking'] = int(no_of_invs)
# #             mainlist.append(formatted_Vehicle)
# #
# #         sortedmainlist = sorted(mainlist, key=lambda x: x['vech_inventory_detail']['created_at'], reverse=True)
# #
# #         maindict['available Vehicle'] = sortedmainlist
# #         # maindict['available Vehicle'] = mainlist
# #
# #     return JsonResponse(maindict, safe=False)
# #
#
#
# @csrf_exempt
# @api_view(['POST'])
# @permission_classes((IsAuthenticated,))
# def available_rental(request):
#     if request.method == "POST":
#
#         req_city = int(request.POST.get('city'))
#         check_in = request.POST.get('start_date')
#         check_out = request.POST.get('end_date')
#         req_count = int(request.POST.get('req_count'))
#
#         mainlist = []
#         maindict = {}
#         vehiclesidfrombooking = []
#         vehinvsid_ByCity = []
#         notbookedinv = []
#         vehinvs_ByCity = []
#         arrayfilterbycat = []
#         cat_id = int(request.POST.get('cat_id'))
#
#         # cat_id = 1
#         # req_city = 1
#         # check_in = '2019-07-01'
#         # check_out = '2019-07-15'
#         # req_count = 1
#         # Vehicle_category=VehicleD
#
#         array = []
#         Vehicle_category = VehicleCategory.objects.get(id=cat_id)
#         Vehicle_detail_by_cat = VehicleDetail.objects.filter(vehicle_category_id=Vehicle_category.id)
#
#         for det in Vehicle_detail_by_cat:
#             detailed_invs = VehicleInventory.objects.filter(vehicle_detail_id=det.id)
#
#             for det_inv in detailed_invs:
#                 array.append(det_inv)
#
#         for a in array:
#             arrayfilterbycat.append(a.id)
#         vehicleinvbycat = VehicleInventory.objects.filter(id__in=arrayfilterbycat)
#
#         if VehicleInventory.objects.filter(vehicle_location_id=req_city).exists():
#             vehinvs_ByCity = vehicleinvbycat.filter(vehicle_location_id=req_city)
#
#         vehiclesfrom_mbooking = ModuleBooking.objects.filter(module_name='rental', start_date=check_in,
#                                                              end_date=check_out)
#
#         for inv in vehiclesfrom_mbooking:
#             vehiclesidfrombooking.append(inv.inventory_id)
#
#         for inv in vehinvs_ByCity:
#             vehinvsid_ByCity.append(inv.id)
#
#         notbookedinv = list(set(vehinvsid_ByCity) - set(vehiclesidfrombooking))
#
#         # bookedinv = list(set(vehinvsid_ByCity) & set(vehiclesidfrombooking))
#         # distinctinv = []
#         #
#         # for unique in bookedinv:
#         #     if unique not in distinctinv:
#         #         distinctinv.append(unique)
#         #
#         # bookedinvlist = []
#         # arr = []
#         # dept = []
#         # room = []
#         # flag = []
#         #
#         # for binv in distinctinv:
#         #     vehiclesbooked = ModuleBooking.objects.get(inventory_id=binv, module_name='rental')
#         #     bookedinvlist.append(vehiclesbooked)
#         #
#         # for vehicle in bookedinvlist:
#         #     singlevechinvlist = ModuleBooking.objects.filter(inventory_id=binv, module_name='rental')
#         #     for singlevechinv in singlevechinvlist:
#         #         arr.append(vehicle.start_date.strftime('%Y-%m-%d'))
#         #         dept.append(vehicle.end_date.strftime('%Y-%m-%d'))
#         #         room.append(vehicle.quantity)
#         #         flag.append(1)
#         #
#         #     arr.append(check_in)
#         #     dept.append(check_out)
#         #     flag.append(0)
#         #     room.append(req_count)
#         #     n = len(arr)
#         #     k = int(VehicleInventory.objects.get(id=vehicle.inventory_id).avail_number)
#         #
#         #     if check_booking_available(arr, dept, n, k, room, flag):
#         #         roomavailable = check_booking_available(arr, dept, n, k, room, flag)
#         #         formatted_vehicleinv = VehicleInventoryFormat(vehicle.inventory_id)
#         #         formatted_vehicleinv['vehicleforbooking'] = roomavailable
#         #         mainlist.append(formatted_vehicleinv)
#         #     arr = []
#         #     dept = []
#         #     room = []
#         #     flag = []
#
#         for inv in notbookedinv:
#             formatted_Vehicle = VehicleInventoryFormat(inv)
#             # no_of_invs = VehicleInventory.objects.get(id=inv).avail_number
#             # formatted_Vehicle['vehicleforbooking'] = int(no_of_invs)
#             mainlist.append(formatted_Vehicle)
#
#         sortedmainlist = sorted(mainlist, key=lambda x: x['vech_inventory_detail']['created_at'], reverse=True)
#
#         maindict['available Vehicle'] = sortedmainlist
#         # maindict['available Vehicle'] = mainlist
#
#     return JsonResponse(maindict, safe=False)
