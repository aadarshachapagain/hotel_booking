from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from account.models import User
from account.owner_profile.models import OwnerProfile
from booking.api.utils import paginate
from hotel.address.models import HotelAddress
from booking.module_booking.models import ModuleBooking
from booking.customer.models import Customer
from hotel.cancellation_policy.models import Cancellation_Policy
from hotel.child_supplement_policy.models import ChildSupplementPolicy
from hotel.cribsPolicy.models import cribsPolicy
from hotel.extraBed.models import ExtraBedPolicy
from listing.api.serializers import listedPropSerializer, CancellationPolicySerializer, OtherPolicySerializer
from listing.api.serializers import BookingDetailSerializer
from hotel.inventory.models import HotelInventory
from django.forms import model_to_dict
from hotel.models import Hotels
from rest_framework.response import Response


class listedProp:
	def __init__(self, id=0, moduleName='', propName='', address='', numberStaff=0, totalInvNum=0):
		self.id = id
		self.moduleName = moduleName
		self.propName = propName
		self.address = address
		self.numberStaff = numberStaff
		self.totalInvNum = totalInvNum


class BookingDetail:
	def __init__(self, id=0, moduleName='', propName='', type='', checkin='', checkout='', customer='', created_at='',
	             address='', booking_id=0):
		self.id = id
		self.moduleName = moduleName
		self.propName = propName
		self.type = type
		self.checkin = checkin
		self.checkout = checkout
		self.customer = customer
		self.created_at = created_at
		self.address = address
		self.booking_id = booking_id


@csrf_exempt
@api_view(['POST'])
def listedProperties(request):
	if request.method == "POST":
		dict_listedprop = {}
		listed_prop = []
		
		user_id = request.POST.get('user_id')
		if User.objects.filter(id=user_id).exists():
			if User.objects.filter(id=user_id, account_type__type='hotel_owner').exists():
				ownedhotels = Hotels.objects.filter(owner_id=user_id)
				for ownhtl in ownedhotels:
					obj = listedProp()
					obj.id = ownhtl.id
					obj.moduleName = 'hotel'
					obj.propName = ownhtl.name
					if HotelAddress.objects.filter(hotel_id=ownhtl.id).exists():
						obj.address = HotelAddress.objects.get(hotel_id=ownhtl.id).address
					else:
						obj.address = ''
					obj.numberStaff = ownhtl.number_of_staff
					obj.totalInvNum = ownhtl.number_of_room
					serializer = listedPropSerializer(obj)
					listed_prop.append(serializer.data)
		
		# if User.objects.filter(id=user_id, account_type__type='rental_owner').exists():
		#     ownedrentals = RentalCompany.objects.filter(owner_id=user_id)
		#     for ownrntl in ownedrentals:
		#         obj = listedProp()
		#         obj.id = ownrntl.id
		#         obj.moduleName = 'rental'
		#         obj.propName = ownrntl.name
		#         if RentalCompanyAddress.objects.filter(company_id=ownrntl.id).exists():
		#             obj.address = RentalCompanyAddress.objects.get(company_id=ownrntl.id).address
		#         else:
		#             obj.address = ''
		#         # obj.numberStaff = ownrntl.number_of_staff
		#         # obj.totalInvNum = ownrntl.number_of_room
		#         serializer = listedPropSerializer(obj)
		#         listed_prop.append(serializer.data)
		#
		# if User.objects.filter(id=user_id, account_type__type='restaurant_owner').exists():
		#     ownedrestaurant = RestaurantCompany.objects.filter(owner_id=user_id)
		#     for ownrest in ownedrestaurant:
		#         obj = listedProp()
		#         obj.id = ownrest.id
		#         obj.moduleName = 'restaurant'
		#         obj.propName = ownrest.name
		#         if RestaurantCompanyAddress.objects.filter(company_id=ownrest.id).exists():
		#             obj.address = RestaurantCompanyAddress.objects.get(company_id=ownrest.id).address
		#         else:
		#             obj.address = ''
		#         # obj.numberStaff = ownrest.number_of_staff
		#         # obj.totalInvNum = ownrest.number_of_room
		#         serializer = listedPropSerializer(obj)
		#         listed_prop.append(serializer.data)
		#
		# if User.objects.filter(id=user_id, account_type__type='travel_tour_owner').exists():
		#     ownedtravel = TravelCompany.objects.filter(owner_id=user_id)
		#     for owntrvl in ownedtravel:
		#         obj = listedProp()
		#         obj.id = owntrvl.id
		#         obj.moduleName = 'travel_tour'
		#         obj.propName = owntrvl.name
		#         if TourCompanyAddress.objects.filter(company_id=owntrvl.id).exists():
		#             obj.address = TourCompanyAddress.objects.get(company_id=owntrvl.id).address
		#         else:
		#             obj.address = ''
		#         serializer = listedPropSerializer(obj)
		#         listed_prop.append(serializer.data)
		else:
			return HttpResponse('Sorry user doesnot exist')
	dict_listedprop['listed_prop'] = listed_prop
	
	return JsonResponse(dict_listedprop, safe=False)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def bookingOnaDate(request):
	if request.method == "POST":
		checkin = request.POST.get('checkin')
		checkout = request.POST.get('checkout')
		owner_id = request.POST.get('owner_id')
		list_invs = []
		bookedinvids = []
		list_detail = []
		
		list_invs = inventoryowned(owner_id)
		
		if checkout == '':
			bookedinv = ModuleBooking.objects.filter(module_name='hotel', inventory_id__in=list_invs,
			                                         start_date=checkin,
			                                         booking__payment_status='OK')
		elif checkout != '':
			bookedinv = ModuleBooking.objects.filter(module_name='hotel', inventory_id__in=list_invs,
			                                         start_date=checkin, end_date__lte=checkout,
			                                         booking__payment_status='OK')
		
		for bi in bookedinv:
			obj = BookingDetail()
			obj.moduleName = 'Hotel'
			booking_instance = ModuleBooking.objects.get(id=bi.id, module_name='hotel')
			inv_instance = HotelInventory.objects.get(id=bi.inventory_id)
			hotel_name = inv_instance.hotel.name
			hotel_id = inv_instance.hotel.id
			inv_name = inv_instance.room_name
			start_date = booking_instance.start_date
			end_date = booking_instance.end_date
			obj.propName = hotel_name
			obj.id = hotel_id
			obj.booking_id = bi.booking_id
			obj.type = inv_name
			obj.checkin = start_date
			obj.checkout = end_date
			obj.created_at = booking_instance.created_at
			customer_name = Customer.objects.get(user_id=bi.customer_id)
			obj.customer = customer_name
			serializer = BookingDetailSerializer(obj)
			list_detail.append(serializer.data)
		
		return JsonResponse(list_detail, safe=False)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def paymentSummary(request):
	if request.method == "POST":
		list_invs = []
		list_detail = []
		owner_id = request.POST.get('owner_id')
		list_invs = inventoryowned(owner_id)
		
		bookedinv = ModuleBooking.objects.filter(module_name='hotel', inventory_id__in=list_invs,
		                                         booking__payment_status='OK')
		
		for bi in bookedinv:
			booking_instance = ModuleBooking.objects.get(id=bi.id, module_name='hotel')
			obj = BookingDetail()
			obj.moduleName = 'Hotel'
			booking_instance = ModuleBooking.objects.get(id=bi.id, module_name='hotel')
			inv_instance = HotelInventory.objects.get(id=bi.inventory_id)
			hotel_name = inv_instance.hotel.name
			hotel_id = inv_instance.hotel.id
			inv_name = inv_instance.room_name
			start_date = booking_instance.start_date
			end_date = booking_instance.end_date
			obj.propName = hotel_name
			obj.id = hotel_id
			obj.booking_id = bi.booking_id
			obj.type = inv_name
			obj.checkin = start_date
			obj.checkout = end_date
			obj.created_at = booking_instance.created_at
			obj.address = HotelAddress.objects.get(hotel_id=hotel_id).address
			customer_name = Customer.objects.get(user_id=bi.customer_id)
			obj.customer = customer_name
			serializer = BookingDetailSerializer(obj)
			list_detail.append(serializer.data)
	
	return JsonResponse(list_detail, safe=False)


def inventoryowned(owner_id):
	list_invs = []
	ownedhotels = []
	
	# all hotels that requested owner owns
	if User.objects.filter(id=owner_id).exists():
		if OwnerProfile.objects.filter(user_id=owner_id).exists():
			if Hotels.objects.filter(owner_id_id=owner_id).exists():
				ownedhotels = Hotels.objects.filter(owner_id_id=owner_id)
	
	# all hotel inventory that requested owner owns
	for ownhtl in ownedhotels:
		hotelinvs = HotelInventory.objects.filter(hotel_id=ownhtl.id)
		for inv in hotelinvs:
			if inv.id not in list_invs:
				list_invs.append(inv.id)
	
	return list_invs


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def paymentDetail(request):
	book_list = []
	booking_id = request.POST.get('booking_id')
	bookings = ModuleBooking.objects.filter(booking_id=booking_id)
	# del dict_inventory['image']
	
	for book in bookings:
		book_dict = model_to_dict(book)
		hotel_name = Hotels.objects.get(id=book.company_id).name
		hotel_address = HotelAddress.objects.get(hotel_id=book.company_id).address
		inventor_name = HotelInventory.objects.get(id=book.inventory_id).room_name
		customer_name = Customer.objects.get(user_id=book.customer).name
		
		book_dict.update({'address': hotel_address})
		book_dict.update({'hotel': hotel_name})
		book_dict.update({'room': inventor_name})
		book_dict.update({'customer': customer_name})
		book_list.append(book_dict)
	
	return JsonResponse(book_list, safe=False)


# Aashish: API created at March 29, 2020

# cancellation policy
class CancellationPolicyObject:
	
	def __init__(self,cancelIdentity, hotel, inventory, type, hourBefore, deductedPrice, deductedNoShowPrice, applicableFrom,
	             applicableTo, applicableDays, cvvRequired, cardDetailRequired, chargeToModify, chargeToCancel):
		self.cancelIdentity = cancelIdentity
		self.hotel = hotel
		self.inventory = inventory
		self.type = type
		self.hourBefore = hourBefore
		self.deductedPrice = deductedPrice
		self.deductedNoShowPrice = deductedNoShowPrice
		self.applicableFrom = applicableFrom
		self.applicableTo = applicableTo
		self.applicableDays = applicableDays
		self.cvvRequired = cvvRequired
		self.cardDetailRequired = cardDetailRequired
		self.chargeToModify = chargeToModify
		self.chargeToCancel = chargeToCancel


class CancellationPolicyOperation(object):
	model = Cancellation_Policy
	
	def returnList(self, hotel_id, inventory_id):
		objectList =[]
		instancesOne = self.model.objects.filter(hotel_id=hotel_id, hotelInventory=inventory_id,
		                                         change_status='assigned')
		for instanceOne in instancesOne:
			status = "assigned"
			object = self.reformatPolicy(instanceOne, status)
			objectList.append(object)
		
		instancesTwo = self.model.objects.filter(hotel_id=hotel_id, hotelInventory=inventory_id,
		                                         change_status='copied')
		for instanceTwo in instancesTwo:
			status = "copied"
			object = self.reformatPolicy(instanceTwo, status)
			objectList.append(object)
		
		return objectList
	
	def reformatPolicy(self, instance, status):
		parentInstance = self.model.objects.get(pk=instance.parent_id) if status == 'assigned' else instance
		object = CancellationPolicyObject(
			cancelIdentity = instance.pk,
			hotel=instance.hotel_id,
			inventory=instance.hotelInventory_id,
			type=parentInstance.cancellation_type,
			hourBefore=parentInstance.hour,
			deductedPrice=parentInstance.price,
			deductedNoShowPrice=parentInstance.no_show,
			applicableFrom=parentInstance.season_start_date.date() if parentInstance.season_start_date else parentInstance.season_start_date,
			applicableTo=parentInstance.season_end_date.date() if parentInstance.season_end_date else parentInstance.season_end_date,
			applicableDays=parentInstance.day,
			cvvRequired=parentInstance.cvc_required,
			cardDetailRequired=parentInstance.card_detail_required,
			chargeToModify=parentInstance.charge_modification,
			chargeToCancel=parentInstance.charge_cancel
		)
		return object


class CancellationPolicyList(APIView):
	
	def get(self, request):
		pass
	
	def post(self, request):
		dataFromApi = request.data
		
		if 'limit' not in request.data:
			limit = 10
		else:
			limit = int(request.data.get('limit'))
		
		if 'page' not in request.data:
			page = 1
		else:
			page = int(request.data.get('page'))
		
		object = CancellationPolicyOperation()
		instances = object.returnList(dataFromApi.get('hotel_id'), dataFromApi.get('inventory_id'))
		serializer = CancellationPolicySerializer(instances, many=True)
		finalData = paginate(serializer.data, limit, page)
		return Response(finalData, status=status.HTTP_200_OK)


# other policy
# include crib, child supplement and extra bed policy
@csrf_exempt
@api_view(['POST'])
def childSupplementPolicy(request):
	customObject = OtherPolicyList()
	model = ChildSupplementPolicy
	finalData = customObject.post(request, model)
	return Response(finalData, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def extraBedPolicy(request):
	customObject = OtherPolicyList()
	model = ExtraBedPolicy
	finalData = customObject.post(request, model)
	return Response(finalData, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def cribPolicy(request):
	customObject = OtherPolicyList()
	model = cribsPolicy
	finalData = customObject.post(request, model)
	return Response(finalData, status=status.HTTP_200_OK)


class OtherPolicyObject:
	
	def __init__(self, policyIdentity, hotel, inventory, ageCategory, ageStart, ageEnd, costType, percentage,
	             unitOfCost, applicableFrom, applicableTo, applicableDays):
		self.policyIdentity = policyIdentity
		self.hotel = hotel
		self.inventory = inventory
		self.ageCategory = ageCategory
		self.ageStart = ageStart
		self.ageEnd = ageEnd
		self.costType = costType
		self.percentage = percentage
		self.unitOfCost = unitOfCost
		self.applicableFrom = applicableFrom
		self.applicableTo = applicableTo
		self.applicableDays = applicableDays


class OtherPolicyOperation(object):
	
	def returnList(self, hotel_id, inventory_id, model):
		objectList = []
		instancesOne = model.objects.filter(hotel_id=hotel_id, hotelInventory=inventory_id,
		                                    change_status='assigned')
		for instanceOne in instancesOne:
			status = "assigned"
			object = self.reformatPolicy(instanceOne, status, model)
			objectList.append(object)
		
		instancesTwo = model.objects.filter(hotel_id=hotel_id, hotelInventory=inventory_id,
		                                    change_status='copied')
		for instanceTwo in instancesTwo:
			status = "copied"
			object = self.reformatPolicy(instanceTwo, status, model)
			objectList.append(object)
		
		return objectList
	
	def reformatPolicy(self, instance, status, model):
		parentInstance = model.objects.get(pk=instance.parent_id) if status == 'assigned' else instance
		object = OtherPolicyObject(
			policyIdentity=instance.pk,
			hotel=instance.hotel_id,
			inventory=instance.hotelInventory_id,
			ageCategory=parentInstance.age_category,
			ageStart=parentInstance.age_start,
			ageEnd=parentInstance.age_end,
			costType=parentInstance.cost_status,
			percentage=parentInstance.cost,
			unitOfCost=parentInstance.unit,
			applicableFrom=parentInstance.season_start_date.date() if parentInstance.season_start_date else parentInstance.season_start_date,
			applicableTo=parentInstance.season_end_date.date() if parentInstance.season_end_date else parentInstance.season_end_date,
			applicableDays=parentInstance.day
		)
		return object


class OtherPolicyList(APIView):
	
	def get(self, request):
		pass
	
	def post(self, request, model):
		dataFromApi = request.data
		
		if 'limit' not in request.data:
			limit = 10
		else:
			limit = int(request.data.get('limit'))
		
		if 'page' not in request.data:
			page = 1
		else:
			page = int(request.data.get('page'))
		
		object = OtherPolicyOperation()
		instances = object.returnList(dataFromApi.get('hotel_id'), dataFromApi.get('inventory_id'), model)
		serializer = OtherPolicySerializer(instances, many=True)
		finalData = paginate(serializer.data, limit, page)
		return finalData
