
from hotel.amenities.models import HotelAmenities
from rest_framework import viewsets, status
from rest_framework.decorators import api_view,permission_classes

from hotel.inventory_bed_type.models import Inventory_Bed_Type
from hotel.inventory.models import HotelInventory
from hotel.roomfeature.models import HotelRoomFeature
from hotel.roomtype.models import HotelRoomType
from hotel.inventorygallery.models import InventoryGallery
from django.forms.models import model_to_dict

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

from points.credit_point.models import CreditPoint
from points.reward_point.models import RewardPoint
from points.virtual_point.models import VirtualPoint


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def defPointsAPIView(request):
	if request.method == "POST":
		user_id = request.POST.get('user_id')
		main = {}
		reward_count = RewardPoint.objects.filter(user = user_id).count()
		if reward_count >0:
			reward_instance = RewardPoint.objects.filter(user=user_id).latest('created_at')
			main['reward_points'] = reward_instance.net_total
		else:
			main['reward_points'] = None
			
		credit_count = CreditPoint.objects.filter(user=user_id).count()
		if credit_count > 0:
			credit_instance = CreditPoint.objects.filter(user=user_id).latest('created_at')
			main['credit_points'] = credit_instance.net_total
		else:
			main['credit_points'] = None
		
		virtual_count = VirtualPoint.objects.filter(user=user_id).count()
		if virtual_count > 0:
			virtual_instance = VirtualPoint.objects.filter(user=user_id).latest('created_at')
			main['virtual_points'] = virtual_instance.net_total
		else:
			main['virtual_points'] = None
			
		return JsonResponse(main, safe=False)
			
		
		
	# if request.method == "POST":
	# 	inventory_id = request.POST.get('inventory')
	# 	hotel_id = request.POST.get('hotel')
	# 	inventory = {}
	# 	custom_bed = []
	# 	parent_gallery = []
	# 	parent_inventory = []
	# 	parent_facilities = []
	# 	parent_room_facilities = []
	# 	parent_room_type = []
	# 	bed_type = []
	# 	inv_count = HotelInventory.objects.filter(id=inventory_id, hotel=hotel_id).count()
	# 	print('count')
	# 	print(inv_count)
	# 	if inv_count > 0:
	# 		inventory_basic = HotelInventory.objects.get(id=inventory_id, hotel=hotel_id)
	# 		inv_id = inventory_basic.id
	# 		dict_inventory = model_to_dict(inventory_basic)
	# 		del dict_inventory['priceforadult']
	# 		del dict_inventory['amenities']
	# 		del dict_inventory['roomfeatures']
	# 		del dict_inventory['hoteladdress']
	# 		del dict_inventory['roomtype']
	# 		del dict_inventory['created_at']
	# 		del dict_inventory['image']
	# 		dict_inventory.update({'priceforadult': json.loads(inventory_basic.priceforadult)})
	# 		dict_inventory.update({'main_image': inventory_basic.image.url})
	# 		# for gallery
	# 		galleries = InventoryGallery.objects.filter(hotel_inventory_id=inv_id)
	# 		if galleries:
	# 			for gallery in galleries:
	# 				url = gallery.image.url
	# 				dict_gallery = model_to_dict(gallery)
	# 				del dict_gallery['image']
	# 				del dict_gallery['hotel_inventory_id']
	# 				dict_gallery.update({'image': url})
	# 				parent_gallery.append(dict_gallery)
	#
	# 			dict_inventory.update({'gallery': parent_gallery})
	# 		else:
	# 			dict_inventory.update({'gallery': None})
	# 		# for gallery
	#
	# 		# for facilities
	# 		facilities = HotelAmenities.objects.filter(hotelinventory=inv_id)
	# 		if facilities:
	# 			for facility in facilities:
	# 				url = facility.image.url
	# 				dict_facility = model_to_dict(facility)
	# 				del dict_facility['image']
	# 				del dict_facility['created_at']
	# 				dict_facility.update({'image': url})
	# 				parent_facilities.append(dict_facility)
	# 			dict_inventory.update({'facilities': parent_facilities})
	# 		else:
	# 			dict_inventory.update({'facilities': None})
	#
	# 		# for facilities
	#
	# 		# for HotelRoomFeature
	# 		roomfeatures = HotelRoomFeature.objects.filter(hotelinventory=inv_id)
	# 		if roomfeatures:
	# 			for roomfeature in roomfeatures:
	# 				dict_room_facility = model_to_dict(roomfeature)
	# 				parent_room_facilities.append(dict_room_facility)
	# 			dict_inventory.update({'room features': parent_room_facilities})
	# 		else:
	# 			dict_inventory.update({'room features': None})
	#
	# 		# for HotelRoomFeature
	#
	# 		# for HotelRoomType
	# 		roomtypes = HotelRoomType.objects.filter(hotelinventory=inv_id)
	# 		if roomtypes:
	# 			for roomtype in roomtypes:
	# 				dict_room_type = model_to_dict(roomtype)
	# 				parent_room_type.append(dict_room_type)
	# 			dict_inventory.update({'room type': parent_room_type})
	# 		else:
	# 			dict_inventory.update({'room type': None})
	#
	# 		# for HotelRoomType
	#
	# 		# for Bed Type
	# 		bedtypes = Inventory_Bed_Type.objects.filter(inventory=inv_id)
	# 		if bedtypes:
	# 			for bedtype in bedtypes:
	# 				dict_bed_type = model_to_dict(bedtype)
	# 				del dict_bed_type['created_at']
	# 				del dict_bed_type['inventory']
	# 				del dict_bed_type['bed_type']
	# 				dict_bed_type.update({'bed_type': bedtype.bed_type.name})
	# 				bed_type.append(dict_bed_type)
	# 			dict_inventory.update({'bed type': bed_type})
	# 		else:
	# 			dict_inventory.update({'bed type': None})
	#
	# 		# for Bed Type
	# 		inventory['inventory'] = dict_inventory
	# 		return JsonResponse(inventory, safe=False)
	# 	else:
	# 		inventory['inventory'] = None
	# 		return JsonResponse(inventory, safe=False)


