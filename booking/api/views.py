from decimal import Decimal
from decimal import Decimal

from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage, message
from django.http import HttpResponse, JsonResponse, FileResponse
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers, settings
from rest_framework.decorators import api_view, permission_classes
from django.forms import model_to_dict
from django.utils.datetime_safe import datetime
from django.views.decorators.csrf import csrf_exempt

from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.utils import json

from account.tokens import account_activation_token
from booking.api.filters import BookingTableFilter

from booking.api.serializers import CustomerProfileSerializer, GuestDetailSerializer, GuestDocDetailSerializer, \
    PaymentSerializer
from booking.api import utils

from booking.business_cash_bonus.models import BusinessCashBonus
from booking.customer.models import Customer

from account.api.serializers import UserCreateSerializer, generateOTP
from account.models import User
from booking.guestdetail.models import GuestDetail
from booking.guestdocdetail.models import GuestDocDetail
# from booking.pdf.views import write_pdf_view
from booking.module_booking.models import ModuleBooking
from booking.utils import check_booking_available
from booking.utils import HotelList

# for customer login credintials
from hotel.Country.models import Country
from hotel.address.models import HotelAddress
from hotel.city.models import City
from hotel.hotel_facilities.models import HotelFacilities
from hotel.inventory.models import HotelInventory

# for customer login credintials
from hotel.inventory.models import HotelInventory
from booking.module_booking.models import ModuleBooking
from booking.booking_table.models import BookingTable
from django.utils.dateparse import parse_date
from hotel.inventory.utils import formatInventory
from hotel.reviews.models import HotelReview
from hotel.state.models import State

from io import BytesIO
from django.conf import settings
from points.credit_point.models import CreditPoint
from points.reward_point.models import RewardPoint
from points.virtual_point.models import VirtualPoint
from booking.referee_and_referred.models import RefereeAndReferred
from points.membership_plan.models import Membership_plan
from booking.business_partners.models import BusinessPartners
import datetime
from hotel.models import Hotels

from hotel.models import Hotels, HotelFacilitiesMiddle
from datetime import timedelta

# from travel_tour.tour_package.models import TourPackage
#
# from travel_tour.tour_package.utils import TourPackageFromat

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from booking.api import utils
from rest_framework.authtoken.models import Token
from django.db.models import Avg, Max, Min


def paginate(clist, limit, page):
    datacount = len(clist)
    paginator = Paginator(clist, limit)
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # return HttpResponse('Sorry requested page is not available:')
        objects = paginator.page(1)
    except EmptyPage:
        return False
    # return HttpResponse('Sorry requested page is not available:')
    # objects = paginator.page(paginator.num_pages)
    data = {
        'previous_page': objects.has_previous() and objects.previous_page_number() or None,
        'next_page': objects.has_next() and objects.next_page_number() or None,
        'totaldatacount': datacount,
        'data': list(objects),
    }
    return data

class CustomerLoginAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


from django.db import connection


# for customer login credintials

# for customer profile update
class CustomerProfileAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerProfileSerializer


# for customer profile update

# for guest detail
class GuestDetailAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = GuestDetail.objects.all()
    serializer_class = GuestDetailSerializer


# for guest detail

# for guest document detail
class GuestDocDetailAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = GuestDocDetail.objects.all()
    serializer_class = GuestDocDetailSerializer


# for guest document detail

def booking_confirmed(request):
    current_site = get_current_site(request)
    mail_subject = 'Activate your blog account.'
    message = render_to_string('booking/booking_confirmed_email.html', {
    })
    to_email = 'aadarshachapagain@gmail.com'
    email = EmailMessage(
        mail_subject, message, 'flytrip@codeforcore.com', to=[to_email]
    )
    email.attach_file('booking/templates/booking/weathermap.PNG')
    email.send()
    return HttpResponse('Email is sent please check it.')


class PaymentAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = BookingTable.objects.all()
    serializer_class = PaymentSerializer


# for guest document detail


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def start_booking(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    cleartoken = (token.split('Token '))
    main_dict = {}
    new_dict = {}
    main_list = []
    user_id = Token.objects.get(key=cleartoken[1]).user_id

    if request.method == "POST":
        received_json_data = json.loads(request.body)
        modules = received_json_data.get('module')
        booking_instance = BookingTable()
        booking_instance.save()
        for module in modules:
            module_instance = ModuleBooking()
            module_instance.module_name = module.get('module_name')
            module_instance.quantity = module.get('quantity')
            module_instance.start_date = module.get('start_date')
            module_instance.end_date = module.get('end_date')
            module_instance.sub_total = module.get('sub_total')
            module_instance.discount = module.get('discount')
            module_instance.tax = module.get('tax')
            module_instance.company_id = module.get('company')
            module_instance.status = 'booked'
            module_instance.inventory_id = module.get('inventory')
            # customer_module_instance = Customer.objects.get(user_id=user_id)
            # module_instance.customer = customer_module_instance
            module_instance.booking = booking_instance
            module_instance.save()
            main_dict['id'] = module_instance.id
            main_list.append(main_dict)
            main_dict = {}
    new_dict.update({'id': main_list})
    return JsonResponse(new_dict, safe=False)


@csrf_exempt
@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def init_booking(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    if token:
        cleartoken = (token.split('Token '))
    main_dict = {}
    
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        modules = received_json_data.get('module')
        for module in modules:
            id = module.get('id')
            instance = ModuleBooking.objects.get(id=id)
            naive = instance.updated_at.replace(tzinfo=None)
            difference_time = (datetime.datetime.now() - naive)
            a = difference_time.days * 1440 + difference_time.seconds / 60
            if a < 10:
                instance.updated_at = datetime.datetime.now()
                instance.save()
                main_dict['booking_id'] = instance.booking.id
            else:
                main_dict['booking_id'] = None
    
    return JsonResponse(main_dict, safe=False)


@csrf_exempt
@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def guest_detail(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    main_dict = {}
    parent_list = []
    child_list = []
    instance = 0
    if request.method == "POST":
        received_json_data = json.loads(request.body)
        guests = received_json_data.get("guest")
        for guest in guests:
            if guest.get('parent_status') == 0:
                parent_list.append(guest)
            else:
                child_list.append(guest)
        for parent in parent_list:
            instance = save_guest(parent, token, instance)
            # doc_instance = GuestDocDetail()
            # document = parent.get('document')
            # doc_instance.document_type = document['document_type']
            # doc_instance.document_number = document['document_number']
            # doc_instance.document_file = document['doc_file']
            # doc_instance.visa_required = document['visa_required']
            # doc_instance.visa_expiry = document['visa_expiry']
            # doc_instance.issuing_country = document['issuing_country']
            # doc_instance.guest_detail = instance
            # doc_instance.save()
        for child in child_list:
            save_guest(child, token, instance)

    main_dict['msg'] = 'Ok'
    return JsonResponse(main_dict, safe=False)


def save_guest(data, token, parent_id):
    instance = GuestDetail()
    instance.name = data.get('name')
    instance.email = data.get('email')
    instance.contact = data.get('contact')
    instance.address = data.get('address')
    instance.gender = data.get('gender')
    instance.dob = data.get('dob')
    instance.city = data.get('city')
    instance.country = data.get('country')
    if parent_id:
        instance.parent_status = 1
        instance.parent = GuestDetail.objects.get(id=parent_id.pk)
    else:
        instance.parent_status = 0
    if token:
        cleartoken = (token.split('Token '))
        user_id = Token.objects.get(key=cleartoken[1]).user_id
        customer_instance = Customer.objects.get(user_id=user_id)
        instance.customer = customer_instance
    instance.save()
    return instance


@csrf_exempt
@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def paymentAPI(request):
    obj = 0
    instance = 0
    module_instance = 0
    customer_module_instance = 0
    token = request.META.get('HTTP_AUTHORIZATION')
    main_dict = {}
    new_dict = {}
    main_list = []
    user_id = ''

    if request.method == "POST":
        received_json_data = json.loads(request.body)
        obj = BookingTable.objects.get(id=received_json_data['payment']['booking_id'])
        obj.payment_method = received_json_data['payment']['payment_method']
        obj.payment_type = received_json_data['payment']['payment_type']
        obj.payment_status = received_json_data['payment']['payment_status']
        obj.total_price = received_json_data['payment']['total_price']
        obj.total_discount = received_json_data['payment']['total_discount']
        obj.total_tax = received_json_data['payment']['total_tax']
        obj.booked_date = received_json_data['payment']['booked_date']
        obj.guest = GuestDetail.objects.get(pk=received_json_data.get('guest_id'))
        obj.status = 'confirmed'
        if token:
            cleartoken = (token.split('Token '))
            user_id = Token.objects.get(key=cleartoken[1]).user_id
            customer = Customer.objects.get(user_id=user_id).name
            obj.customer = Customer.objects.get(user_id=user_id)
        else:
            customer = GuestDetail.objects.get(pk=received_json_data.get('guest_id')).name

        name_split = customer.split(" ")
        name_split = name_split[1]
        last_name = name_split[0:3]
        obj.confirmation_number = str(last_name).upper() + '-' + received_json_data['payment'][
            'booked_date'] + '-' + str(generateOTP(4))
        obj.save()

        if user_id:
            customer_module_instance = Customer.objects.get(user_id=user_id)
    
            # cash bonus added if the user has any kind of business partnership
            check_partner = Customer.objects.get(user=user_id).partnerplan
            if check_partner != None:
                cash_bonus = check_partner.flightexcludedCb
                cash = BusinessCashBonus()
                cash.cash_bonus_amount = (Decimal(cash_bonus) * Decimal(
                    received_json_data['payment']['total_price'])) / 100
                cash.remark = 'bonus got'
                # cash.booking = module_instance
                cash.transaction = obj
                cash.user = customer_module_instance
                cash.save()
    
            # commented for discussion with mr. dotel
            # point is created according to hotel not on the basis of inventory count
            # add_credit_point = CreditPoint()
            # add_credit_point.remark = 'Not Used'
            # add_credit_point.booking = module_instance
            # add_credit_point.transaction = obj
            # add_credit_point.user = customer_module_instance
            # add_credit_point.save()
    
            points = received_json_data.get('points')
            if points.get('reward') != 0:
                reward = RewardPoint()
                reward.transaction_amount = -1 * points.get('reward')
                reward.remark = 'used'
                # reward.booking = module_instance
                reward.transaction = obj
                reward.user = customer_module_instance
                reward.save()
    
            if points.get('virtual') != 0:
                virtual = VirtualPoint()
                virtual.transaction_amount = -1 * points.get('virtual')
                virtual.remark = 'used'
                # virtual.booking = module_instance
                virtual.transaction = obj
                virtual.user = customer_module_instance
                virtual.save()
    
            if points.get('credit') != 0:
                credit = CreditPoint()
                credit.transaction_amount = -1 * points.get('credit')
                credit.remark = 'used'
                # credit.booking = module_instance
                credit.transaction = obj
                credit.user = customer_module_instance
                credit.save()

    main_dict.update({'msg':'Payment Successful'})
    return JsonResponse(main_dict, safe=False)

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def first_hotel_list(request):
    if request.method == "POST":
        status = []
        final_hotel = []
        location = request.POST.get('location')
        check_in = request.POST.get('checkin')
        check_out = request.POST.get('checkout')
        quantity = request.POST.get('quantity')
        child_max = request.POST.get('no_child')
        adult_max = request.POST.get('no_adult')
        infant_max = request.POST.get('no_infant')
        
        if 'limit' not in request.POST:
            limit = 10
        else:
            limit = int(request.POST.get('limit'))

        if 'page' not in request.POST:
            page = 1
        else:
            page = int(request.POST.get('page'))

        # access address table to filter location
        final_invs, final_rooms = utils.getMatchingInventory(location, check_in, check_out,  child_max, adult_max, infant_max)
        
        for final_inv in final_invs:
            inv_temp = HotelInventory.objects.get(id=final_inv)
            if inv_temp.hotel_id not in final_hotel:
                a = HotelList(inv_temp.hotel_id)
                status.append(a)
                final_hotel.append(inv_temp.hotel_id)
        data = paginate(status, limit, page)
        return JsonResponse(data, safe=False)
        


class BookinData:
    arrivaldate = []
    departuredate = []
    count = []
    flag = []
    k = 0
    n = 0
    id = 0
    idlist = []

    def __eq__(self, other):
        return self.id == other.id


@csrf_exempt
@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def availableInv(request):
    flag = []
    invbookedlist = []
    invsent = []
    repeatedinvlist = []
    nonrepeatedid = []
    sentinventory = []
    dict_invbooked = []
    totalInvIdOfAHotel = []
    listOfInvIdBooked = []
    listOfInvIdNotBooked = []
    listOfPassBkdInvId = []
    # list of inv id that will satisfy the query and are present in module Booking.

    main = {}

    if request.method == "POST":
        hotel_id = request.POST.get('hotel_id')
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        # location = request.POST.get('location')
        norooms = request.POST.get('norooms')
        # if norooms is None:
        norooms = 0
        nochilds = request.POST.get('no_child')
        noadults = request.POST.get('no_adult')
        noinfants = request.POST.get('no_infant')

        if 'limit' not in request.POST:
            limit = 10
        else:
            limit = int(request.POST.get('limit'))

        if 'page' not in request.POST:
            page = 1
        else:
            page = int(request.POST.get('page'))

        # inventory whose is active is true
        hotelinvlist = HotelInventory.objects.filter(hotel=hotel_id, is_active=True)

        for hotelinv in hotelinvlist:
            totalInvIdOfAHotel.append(hotelinv.id)

        if ModuleBooking.objects.filter(company_id=hotel_id, module_name="hotel").exists():
            # inventories that are booked and recorded in module booking.
            invbookedlist = ModuleBooking.objects.filter(company_id=hotel_id, module_name="hotel")

        # for detail info of inventory that are in ModuleBooking
        for invbkd in invbookedlist:
            if invbkd.inventory_id not in listOfInvIdBooked:
                # should check if the selected inv will be enough for the query or not.
                requiredroom = shouldsendinv(queryadult=noadults, queryinfant=noinfants,
                                             querychild=nochilds,
                                             inv_id=invbkd.inventory_id)
                # All the inv from modulebooking are of not the same hotel so check if the inventory are from same hotel
                try:
                    singleInventoryInstance = hotelinvlist.get(id=invbkd.inventory_id)
                except HotelInventory.DoesNotExist:
                    singleInventoryInstance = None

                if singleInventoryInstance:
                    singleInventoryInstance = hotelinvlist.get(id=invbkd.inventory_id)
                    listOfInvIdBooked.append(invbkd.inventory_id)

                    if singleInventoryInstance.no_of_rooms >= requiredroom:
                        listOfPassBkdInvId.append(invbkd.inventory_id)

        listOfInvIdNotBooked = list(set(totalInvIdOfAHotel) - set(listOfInvIdBooked))
        # difference of total inv and inv that are booked

        temp_invnotbookedlist = []
        for id in listOfInvIdNotBooked:
            temp_invnotbookedlist.append(hotelinvlist.get(id=id))

        invnotbookedlist = temp_invnotbookedlist
        if (len(invnotbookedlist) != 0):
            for invnotbooked in invnotbookedlist:
                # check if the query matching results are present or not in inv that are not booked yet
                requiredroomofthistype = shouldsendinv(queryadult=noadults, queryinfant=noinfants,
                                                       querychild=nochilds,
                                                       inv_id=invnotbooked.id)
                if requiredroomofthistype <= invnotbooked.no_of_rooms:
                    dict_invnotbooked = formatInventory(invnotbooked.id, invnotbooked.no_of_rooms)
                    invsent.append(dict_invnotbooked)

        listThatPassedQuery = ModuleBooking.objects.filter(inventory_id__in=listOfPassBkdInvId)

        # invbookedlist must be fetched from moduleBooking table.
        for invbooked in listThatPassedQuery:
            distinctinv = listThatPassedQuery.filter(inventory_id=invbooked.inventory_id)
            arrivaldate = []
            departuredate = []
            count = []

            # same inventory can have multiple bookings for different time
            for d in distinctinv:
                inventory_id = d.inventory_id
                arrivaldate.append(d.start_date.strftime('%Y-%m-%d'))
                departuredate.append(d.end_date.strftime('%Y-%m-%d'))
                countinvbooked = d.quantity
                count.append(int(countinvbooked))
                flag.append(1)

            arrivaldate.append(checkin)
            departuredate.append(checkout)
            flag.append(0)
            count.append(int(norooms))
            n = len(arrivaldate)
            k = HotelInventory.objects.get(id=d.inventory_id).no_of_rooms

            # data structure to send data in booking algo
            obj = BookinData()
            obj.arrivaldate = arrivaldate
            obj.departuredate = departuredate
            obj.count = count
            obj.flag = flag
            obj.k = k
            obj.n = n
            obj.id = inventory_id
            repeatedinvlist.append(obj)

            if (obj.id not in nonrepeatedid):
                nonrepeatedid.append(obj.id)

            new_dict = {}
            for obj in repeatedinvlist:
                if obj.id not in new_dict and obj.id != "":
                    new_dict[obj.id] = obj

        for index in nonrepeatedid:
            roomavailable = check_booking_available(new_dict[index].arrivaldate, new_dict[index].departuredate,
                                                    new_dict[index].n, new_dict[index].k, new_dict[index].count,
                                                    new_dict[index].flag)

            if index not in sentinventory:
                sentinventory.append(index)
                if (roomavailable):
                    invpassed = HotelInventory.objects.get(id=index)
                    # decide whether this type of inventory should be sent or not

                    reqBkdRoomOfThisType = shouldsendinv(queryadult=noadults, queryinfant=noinfants,
                                                         querychild=nochilds,
                                                         inv_id=invpassed.id)
                    # roomavailable from booking may be different from result obtained from'shouldsendinv'
                    if reqBkdRoomOfThisType <= roomavailable:
                        dict_invbooked = formatInventory(invpassed.id, roomavailable)
        if len(dict_invbooked) == 0:
            print('dict is empty')
        else:
            invsent.append(dict_invbooked)
        data = utils.paginate(invsent, limit, page)
        max = HotelInventory.objects.all().aggregate(Max('price'))
        min = HotelInventory.objects.all().aggregate(Min('price'))
        data.update({'max_price': max['price__max']})
        data.update({'min_price': min['price__min']})

        if not data:
            return HttpResponse('Sorry requested page donot exist')

    return JsonResponse(data, safe=False)


def shouldsendinv(queryadult, queryinfant, querychild, inv_id):
    selectedInventory = HotelInventory.objects.get(id=inv_id)
    minimumRoom = 1
    a = True
    while a:
        # check if the adult, infant and child can be adjusted is the room of same type
        if (int(queryadult) <= int(selectedInventory.adult_max) * minimumRoom and int(querychild) <= int(
                selectedInventory.child_max) * minimumRoom and int(queryinfant) <= int(
            selectedInventory.infant_max) * minimumRoom):
            return minimumRoom
        else:
            minimumRoom += 1
            if minimumRoom > selectedInventory.no_of_rooms:
                a = False
    return minimumRoom


@csrf_exempt
@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def referperson(request):
    if request.method == "POST":
        selfuserid = request.POST.get('userid')
        email = request.POST.get('email')
        response_data = {}

        if email != '':
            user_tobe_referred = User.objects.get(email=email)
            device_id = user_tobe_referred.device_id

        if selfuserid != '':
            uniqtoken = Customer.objects.get(user=selfuserid).uniqtoken
        response_data['device_id'] = device_id
        response_data['uniqtoken'] = uniqtoken

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
@api_view(['POST'])
# @permission_classes((IsAuthenticated,))
def referrelation(request):
    if request.method == "POST":
        id_to_be_referred = request.POST.get('id')
        sponsortoken = request.POST.get('sponsortoken')
        getmembership = request.POST.get('membership')
        ## wannabetype can be either partner or member
        ## wannabeId id the Id of the particular subscription type
        ##such as goldmembership's ID or goldpartnership's ID

        getpartnership = request.POST.get('partnership')
    # this is the id of the user who is being referred by another user.

    # response_data = {}

    if sponsortoken != '':
        id_of_refeerer = Customer.objects.get(uniqtoken=sponsortoken)

        if id_to_be_referred != '':
            id_of_refeerer = Customer.objects.get(uniqtoken=sponsortoken)
            obj_id_to_be_referred = Customer.objects.get(user=id_to_be_referred)
            instance = RefereeAndReferred()
            instance.by = id_of_refeerer
            instance.to = obj_id_to_be_referred

            if getmembership != '':
                instance.membership = Membership_plan.objects.get(id=getmembership)

            elif getpartnership != '':
                instance.partnership = BusinessPartners.objects.get(id=getpartnership)

            else:
                return HttpResponse('Please specify which subscription you want to take')

            instance.status = 'pending'
            instance.save()

    return HttpResponse('Referred refree relation is saved in the table')


class Reapetedhotels:
    hotel = Hotels()
    count = 0


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def trendingDestinations(request):
    now = datetime.date.today()
    decr = datetime.timedelta(days=30)
    previous = now - decr
    hotelinrange = ModuleBooking.objects.filter(start_date__range=[previous, now])
    mostbookedhotel = []
    sortedmostbookedhotel = []
    trendingCities = {}
    trendinglist = []

    distinct_ids = []
    for hotel in hotelinrange:
        if hotel.company_id not in distinct_ids:
            distinct_ids.append(hotel.company_id)

    for id in distinct_ids:
        obj = Reapetedhotels()
        count = ModuleBooking.objects.filter(company_id=id).count()
        obj.hotel = Hotels.objects.get(id=id)
        obj.count = count
        mostbookedhotel.append(obj)

    sortedmostbookedhotel = sorted(mostbookedhotel, key=lambda x: x.count, reverse=True)

    finalbookedhotel = sortedmostbookedhotel[:10]
    for ft in finalbookedhotel:
        city = HotelAddress.objects.get(hotel=ft.hotel).city
        getcity = model_to_dict(City.objects.get(id=city.id))
        getcity.update({'image': city.image.url})

        if getcity not in trendinglist:
            trendinglist.append(getcity)

    trendingCities['cities'] = trendinglist
    return JsonResponse(trendingCities, safe=False)


def check_available_inv_again(request):
    arr = []
    dept = []
    room = []
    flag = []
    mainlist = []
    bookedinv = {}
    s = '{"requiredInv": [' \
        '{"inventory": 7, "count": 1}, {"inventory": 8, "count": 1}' \
        ']' \
        ',"checkin": "2019/06/15", "checkout": "2019/06/20"}'
    d = json.loads(s)

    # json = request.POST.get('json')
    # check_in = request.POST.get('check_in')
    # check_out = request.POST.get('check_out')

    # check_in = '2019-06-15'
    # check_out = '2019-06-20'
    # quantity = 2

    check_in = d['checkin']
    check_out = d['checkout']

    # i = 0

    module_name = 'Hotel'
    # inventory_ids = [7, 8, 9]
    # neededs = [2, 3, 4]

    # for inventory_id in inventory_ids:
    for inv in d['requiredInv']:
        booking_count = ModuleBooking.objects.filter(module_name=module_name,
                                                     inventory_id=inv['inventory']).count()

        if booking_count > 0:
            # for same inventory use booking algorithm
            booking_instance = ModuleBooking.objects.filter(module_name=module_name,
                                                            inventory_id=inv['inventory'])

            for instance in booking_instance:
                arr.append(instance.start_date.strftime('%Y-%m-%d'))
                dept.append(instance.end_date.strftime('%Y-%m-%d'))
                room.append(instance.quantity)
                flag.append(1)

            arr.append(check_in)
            dept.append(check_out)
            flag.append(0)
            room.append(int(inv['count']))
            n = len(arr)
            inventory_instance = HotelInventory.objects.get(id=inv['inventory'])

            k = inventory_instance.no_of_rooms

            availableroom = check_booking_available(arr, dept, n, k, room, flag)
            if availableroom:
                invavailable = {}
                invavailable['inventory'] = inv['inventory']
                if inv['count'] <= availableroom:
                    invavailable['available'] = 'available'
                else:
                    invavailable['available'] = ' Not available'

                if invavailable not in mainlist:
                    mainlist.append(invavailable)
            else:
                arr = []
                dept = []
                room = []
        # i = i + 1

    bookedinv['invs'] = mainlist
    return JsonResponse(bookedinv, safe=False)


# for travel and tour apis
# @csrf_exempt
# @api_view(['POST'])
# @permission_classes((IsAuthenticated,))
# def first_package_list(request):
#     if request.method == "POST":
#         main_list = []
#         main_dict = {}
#         location = request.POST.get('location')
#         time = request.POST.get('time')
#         module_name = 'travel_tour'
#
#         # access address table to filter location
#         if location == "":
#             return JsonResponse('Please enter location', safe=False)
#         try:
#             city_instance = City.objects.get(name=location)
#         except City.DoesNotExist:
#             return JsonResponse('Location not found', safe=False)
#
#         address_count = TourPackage.objects.filter(distination_city=city_instance.id, best_time__contains=time).count()
#         if address_count > 0:
#             matching_package = TourPackage.objects.filter(distination_city=city_instance.id, best_time__contains=time)
#             for package in matching_package:
#                 obj1 = TourPackageFromat(package.id)
#                 # a = json.dumps(obj1, default=convert_to_dict)
#                 # main_list.append(json.loads(a))
#                 main_list.append(obj1)
#             main_dict['package'] = main_list
#             return JsonResponse(main_dict, safe=False)
#         else:
#             return JsonResponse("Matching Package doesn't exists.", safe=False)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def trendingDestinations(request):
    now = datetime.date.today()
    decr = datetime.timedelta(days=100)
    previous = now - decr
    # hotelinrange = ModuleBooking.objects.filter(start_date__range=[previous, now], module_name='hotel')
    hotelinrange = ModuleBooking.objects.filter(start_date__range=[previous, now], module_name='hotel')
    mostbookedhotel = []
    sortedmostbookedhotel = []
    trendingCities = {}
    trendinglist = []

    distinct_ids = []
    for hotel in hotelinrange:
        if hotel.company_id not in distinct_ids:
            distinct_ids.append(hotel.company_id)

    for id in distinct_ids:
        obj = Reapetedhotels()
        count = ModuleBooking.objects.filter(company_id=id).count()
        obj.hotel = Hotels.objects.get(id=id)
        obj.count = count
        mostbookedhotel.append(obj)

    sortedmostbookedhotel = sorted(mostbookedhotel, key=lambda x: x.count, reverse=True)

    finalbookedhotel = sortedmostbookedhotel[:10]
    for ft in finalbookedhotel:
        city = HotelAddress.objects.get(hotel=ft.hotel).city
        getcity = model_to_dict(City.objects.get(id=city.id))
        getcity.update({'image': city.image.url})

        if getcity not in trendinglist:
            trendinglist.append(getcity)

    trendingCities['cities'] = trendinglist
    return JsonResponse(trendingCities, safe=False)


# @api_view(['POST'])
# @permission_classes((IsAuthenticated,))
# def trendingPackages(request):
#     now = datetime.date.today()
#     decr = datetime.timedelta(days=30)
#     previous = now - decr
#     packageinrange = ModuleBooking.objects.filter(start_date__range=[previous, now], module_name='travel_tour')
#     maindict = {}
#     mainlist = []
#
#     for package in packageinrange:
#         package = TourPackageFromat(package.inventory_id)
#         mainlist.append(package)
#
#     maindict['packages'] = mainlist
#     return JsonResponse(maindict, safe=False)


# @csrf_exempt
# @api_view(['POST'])
# @permission_classes((IsAuthenticated,))
# def package_search_by_theme(request):
#     if request.method == "POST":
#         main_list = []
#         main_dict = {}
#         theme = request.POST.get('theme')
#         module_name = 'travel_tour'
#
#         # access address table to filter location
#         if 'limit' not in request.POST:
#             limit = 10
#         else:
#             limit = int(request.POST.get('limit'))
#
#         if 'page' not in request.POST:
#             page = 1
#         else:
#             page = int(request.POST.get('page'))
#
#         if theme == "":
#             return JsonResponse('Please enter theme', safe=False)
#
#         theme_count = TourPackage.objects.filter(theme__title=theme).count()
#         if theme_count > 0:
#             matching_package = TourPackage.objects.filter(theme__title=theme)
#             for package in matching_package:
#                 obj1 = TourPackageFromat(package.id)
#                 # a = json.dumps(obj1, default=convert_to_dict)
#                 # main_list.append(json.loads(a))
#                 main_list.append(obj1)
#             data = utils.paginate(main_list, limit, page)
#
#             if not data:
#                 return HttpResponse('Sorry requested page donot exist')
#
#             # main_dict['package'] = main_list
#             return JsonResponse(data, safe=False)
#         else:
#             return JsonResponse("Matching Package doesn't exists.", safe=False)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def review(request):
    if request.method == "POST":
        main_list = []
        main_dict = {}
        module = request.POST.get('module')
        company_id = request.POST.get('company_id')
        inventory_id = request.POST.get('inventory_id')
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        user_id = request.POST.get('user_id')

        if module and company_id and inventory_id and rating and review and user_id:
            instance = HotelReview()
            instance.module = module
            instance.company_id = company_id
            instance.inventory_id = inventory_id
            instance.rating = rating
            instance.review = review
            instance.user_id = User.objects.get(id=user_id)
            instance.save()
            return JsonResponse("Your review is recorded.Thank You", safe=False)
        else:
            return JsonResponse("Please enter all the fields.", safe=False)

@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def my_booking(request):
    if request.method == "POST":
        # convert token into user id
        token = request.META.get('HTTP_AUTHORIZATION')
        cleartoken = (token.split('Token '))
        user_id = Token.objects.get(key=cleartoken[1]).user_id
        main_dict ={}
        main_list=[]
        booking_instances = BookingTable.objects.filter(customer=user_id)
        user_filter = BookingTableFilter(request.POST, queryset=booking_instances)
        for instance in user_filter.qs:
            tempVar = utils.MyBookingList(instance)
            a = json.dumps(tempVar, default=utils.convert_to_dict)
            main_list.append(json.loads(a))
        main_dict['booking'] = main_list
        return JsonResponse(main_dict, safe=False)
        