import requests
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.utils import json
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime

from account.Language.models import Language
from account.staff_profile.models import StaffProfile
from booking.booking_table.models import BookingTable
from booking.module_booking.models import ModuleBooking
from booking.utils import check_booking_available
from hotel.bankDetail.models import BankDetail
from hotel.groupRate.models import GroupRate
from hotel.hotel_facilities.models import HotelFacilities
from hotel.inventory.models import HotelInventory
from hotel.landmark.models import Landmark

from users.models import Users
from .models import Hotels, HotelFacilitiesMiddle, HotelLanguageMiddle
from .owner.models import HotelOwner
from .gallery.models import HotelGallery
from .address.models import HotelAddress
from .forms import HotelForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.db.models import Q
from account.owner_profile.models import OwnerProfile

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from hotel.decorators import hotel_update_decorator, acl_decorator
from hotel.decorators import hotel_create_decorator
from hotel.decorators import hotel_delete_decorator
from django.db import connection
from hotel.models import HotelsNew, HotelFacilitiesMiddleNew
from django.db.models import Avg, Count, Min, Sum, F
from hotel.propertyDetail.models import PropertyDetail


def toapprovehotel(request):
    hotels = Hotels.objects.filter(is_active=False)
    data = {
        'all_items': hotels
    }
    return render(request, 'hotel/approval.html', data)


def approvalpreview(request, item_id):
    object = Hotels.objects.get(pk=item_id)
    hotelAddress = HotelAddress.objects.get(hotel_id=item_id)
    galleries = HotelGallery.objects.filter(hotel_id=item_id)
    landmarks = hotelAddress.landmarks.filter()
    languages = object.languages.filter()
    hotel_obj = Hotels.objects.get(pk=item_id)
    facilities = hotel_obj.facilities.filter()
    bank = BankDetail.objects.filter(hotel=item_id)
    cancellations = hotel_obj.cancellation.filter()
    data = {
        'object': object,
        'galleries': galleries,
        'landmarks': landmarks,
        'address': hotelAddress,
        'facilities': facilities,
        'languages': languages,
        'bank': bank,
        'cancellations': cancellations,
    }
    return render(request, 'hotel/hotelpreview.html', data)


def approveddone(request, item_id):
    Hotels.objects.filter(id=item_id).update(is_active=True)
    return redirect("hotel:approvehotel")


def mass_approve(request):
    if request.method == 'POST':
        for i in request.POST.getlist('id[]'):
            Hotels.objects.filter(id=i).update(is_active=True)
        return JsonResponse({
            'success': True,
        })


def whichHotel(request, hotel_id):
    response = redirect('hotel:calendar', hotel_id)
    request.session['hotel_id'] = hotel_id
    # return after cookie is set
    response.set_cookie('current_hotel', hotel_id)
    return response


def hotelDashboardView(request):
    context = {
        'message': 'This is Dashboard for hotel Module'
    }
    return render(request, 'travel/hotel_base.html', context)


def cookiedelete(request):
    response = redirect('logout')
    response.set_cookie('current_hotel', 'empty')
    response.set_cookie('current_module', 'empty')
    response.set_cookie('current_company', 'empty')
    response.set_cookie('current_tourpackage', 'empty')
    response.set_cookie('hotel_inventory', 'empty')
    response.set_cookie('current_inventory', 'empty')
    response.set_cookie('current_rental', 'empty')
    return response


# @method_decorator([login_required], name='dispatch')
class HotelListView(ListView):
    model = Hotels
    template_name = 'hotel/index.html'
    context_object_name = 'all_items'

    def get_context_data(self, object_list=None, **kwargs):
        user = self.request.user
        current_hotel = self.kwargs['hotel_id']
        context = super(HotelListView, self).get_context_data(**kwargs)
        hotel = Hotels.objects.get(id=current_hotel)
        galleries = HotelGallery.objects.filter(hotel_id=current_hotel)
        facilities = hotel.facilities.filter()
        languages = hotel.languages.filter()
        cancellation = hotel.cancellation.filter()
        bank_count = BankDetail.objects.filter(hotel=current_hotel).count()
        if bank_count > 0:
            context['bank'] = BankDetail.objects.filter(hotel=current_hotel)
        # landmarks = hotel.landmarks.filter()
        addrinstance = HotelAddress.objects.get(hotel_id=hotel.id)
        landmarks = addrinstance.landmarks.filter()
        grouprate = GroupRate.objects.filter(hotel=current_hotel)
        context['hotel'] = hotel
        context['all_items'] = hotel
        context['galleries'] = galleries
        context['facilities'] = facilities
        context['languages'] = languages
        context['landmarks'] = landmarks
        context['cancellations'] = cancellation
        context['grouprate'] = grouprate
        return context


@method_decorator([login_required], name='dispatch')
@method_decorator(hotel_delete_decorator, name='dispatch')
class HotelDelete(SuccessMessageMixin, DeleteView):
    model = Hotels
    success_url = reverse_lazy('hotel:hotelselect')

    def render_to_response(self, context, **response_kwargs):
        item_id = self.kwargs['pk']
        response = super(HotelDelete, self).render_to_response(context, **response_kwargs)
        response.set_cookie("current_hotel", 'empty')
        return response

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        success_url = self.get_success_url()
        response = redirect('hotel:hotelselect')
        response.set_cookie('current_hotel', 'empty')
        return response


@method_decorator([login_required], name='dispatch')
class HotelDetail(DetailView):
    model = Hotels
    template_name = 'hotel/show.html'
    queryset = Hotels.objects.all().values()

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['pk']
        context = super(HotelDetail, self).get_context_data(**kwargs)
        hotel = Hotels.objects.get(pk=item_id)
        addrinstance = HotelAddress.objects.get(hotel_id=hotel.id)
        landmarks = addrinstance.landmarks.filter()
        facilities = hotel.facilities.filter()
        languages = hotel.languages.filter()
        context['object'] = hotel
        context['facilities'] = facilities
        context['languages'] = languages
        context['landmarks'] = landmarks
        context['cancellations'] = hotel.cancellation.filter()
        context['bank'] = BankDetail.objects.filter(hotel=item_id)
        context['galleries'] = HotelGallery.objects.filter(hotel_id=item_id)
        return context


@method_decorator(acl_decorator(Hotels, 'add'), name='dispatch')
@method_decorator(hotel_create_decorator, name='dispatch')
class HotelCreate(SuccessMessageMixin, CreateView):
    template_name = 'hotel/create.html'
    model = Hotels
    form_class = HotelForm
    success_message = 'Information Added Successfully'
    errors2 = {}

    # def render_to_response(self, context, **response_kwargs):
    # 	item = self.object
    # 	response = super(HotelCreate, self).render_to_response(context, **response_kwargs)
    # 	response.set_cookie("current_hotel", item.id)
    # 	return response

    def get_success_url(self):
        item = self.object
        if self.form.data['register'] == 'Save and Exit':
            url = reverse_lazy('hotel:hotelindex', kwargs={'hotel_id': item.id})
        else:
            url = reverse_lazy('hotel:addressupdate', kwargs={'pk': item.id})
        return url

        # item = self.object
        # response = redirect('hotel:addressupdate', item.id)
        # # return after cookie is set
        # response.set_cookie('current_hotel', item.id)
        # return response

    # return reverse_lazy('hotel:addressupdate', kwargs={'pk': item.id})

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        for f in form.errors:
            self.errors2[f] = '.'.join(form.errors[f])
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        self.form = form
        hotel = form.save(commit=False)
        hotel.save()
        hoteladdress = HotelAddress.objects.create(hotel=hotel)
        facilities = form.data.getlist('facilities')
        languages = form.data.getlist('languages')

        for fac in facilities:
            facility = HotelFacilities.objects.get(id=fac)
            HotelFacilitiesMiddle.objects.create(hotels=hotel, hotelsfacilities=facility)

        for language in languages:
            languages = Language.objects.get(id=language)
            HotelLanguageMiddle.objects.create(hotels=hotel, language=languages)

        return super(HotelCreate, self).form_valid(form)
        # response = redirect('hotel:addressupdate', hotel.id)
        # # return after cookie is set
        # response.set_cookie('current_hotel', hotel.id)
        # return response

    # return super(HotelCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(HotelCreate, self).get_context_data(**kwargs)
        prop_detail = ''
        if 'prop_id' in self.kwargs:
            prop_id = self.kwargs['prop_id']
            prop_detail = PropertyDetail.objects.get(id=prop_id)

        context['owners'] = OwnerProfile.objects.all().order_by('id').reverse()
        usertmp = self.request.user.account_type.all()
        facilities = HotelFacilities.objects.all()
        languages = Language.objects.all()
        customerror = self.errors2

        context['facilities'] = facilities
        context['usertmp'] = usertmp
        context['languages'] = languages
        context['customerrors'] = customerror
        context['prop_detail'] = prop_detail

        # data = {
        #     'facilities': facilities,
        #     'usertmp': usertmp,
        #     'languages': languages,
        #     'customerrors': customerror,
        #     'prop_detail': prop_detail
        #
        # }
        return context


@method_decorator(acl_decorator(Hotels, 'change'), name='dispatch')
@method_decorator(hotel_update_decorator, name='dispatch')
class HotelUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'hotel/create.html'
    model = Hotels
    form_class = HotelForm
    success_message = 'Information Updated Successfully'

    # def get_success_url(self):
    #     item = self.object
    #     return reverse_lazy('hotel:hotelindex', kwargs={'hotel_id': item.id})
    #
    def get_success_url(self):
        item = self.object
        if self.form.data['register'] == 'Save and Exit':
            url = reverse_lazy('hotel:hotelindex', kwargs={'hotel_id': item.id})
        else:
            url = reverse_lazy('hotel:addressupdate', kwargs={'pk': item.id})
        return url

    def form_valid(self, form):
        self.form = form
        hotel = form.save(commit=False)
        hotel.is_active = False
        facilities = form.data.getlist('facilities')
        languages = form.data.getlist('languages')
        citizen_radio = form.data['citizen_radio']
        if (citizen_radio == 'False'):
            hotel.rateforforeign = None
            hotel.ratefornepali = None
            hotel.rateforsaarc = None
        hotel.save()
        item = self.object
        item_id = item.id
        hotel.facilities.through.objects.filter(hotels_id=item_id).delete()
        for fac in facilities:
            facility = HotelFacilities.objects.get(id=fac)
            HotelFacilitiesMiddle.objects.create(hotels=hotel, hotelsfacilities=facility)

        hotel.languages.through.objects.filter(hotels_id=item_id).delete()
        for language in languages:
            languages = Language.objects.get(id=language)
            HotelLanguageMiddle.objects.create(hotels=hotel, language=languages)

        return super(HotelUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(HotelUpdate, self).get_context_data(**kwargs)
        context['owners'] = HotelOwner.objects.all().order_by('id').reverse()
        item_id = self.kwargs['pk']
        prop_detail_id = Hotels.objects.get(id=item_id).prop_id.id
        prop_detail = PropertyDetail.objects.get(id=prop_detail_id)

        facilities = HotelFacilities.objects.exclude(facilitiess=item_id)
        languages = Language.objects.exclude(languages=item_id)
        selectedlanguage = Language.objects.filter(languages=item_id)
        selectedfacilities = HotelFacilities.objects.filter(facilitiess=item_id)
        instance = Hotels.objects.get(id=item_id)
        selected_star = []
        selected_star.append(instance.star_rating)
        star = ['Tourist Standard', '1 Star', '2 Star', '3 Star', '4 Star', '5 Star', '6 Star', '7 Star', 'Apartment']
        remaining_star = set(star).difference(set(selected_star))
        context['remaining_star'] = remaining_star
        context['facilities'] = facilities
        context['languages'] = languages
        context['selectedlanguage'] = selectedlanguage
        context['selectedfacilities'] = selectedfacilities
        context['prop_detail'] = prop_detail
        return context


def editHotel(request, item_id):
    item_id = item_id
    object = Hotels.objects.get(id=item_id)
    facilities = HotelFacilities.objects.exclude(facilitiess=item_id)
    selectedfacilities = HotelFacilities.objects.filter(facilitiess=item_id)
    context = {}
    context['facilities'] = facilities
    context['selectedfacilities'] = selectedfacilities
    context['object'] = object

    # return redirect('hotel:hotelcreate', context)
    return render(request, 'hotel/create.html', context)


def updateHotel(request, item_id):
    if request.method == 'POST':
        item = Hotels.objects.get(pk=item_id)
        form = HotelForm(request.POST or None, request.FILES, instance=item)
        if form.is_valid():
            facilities = form.data.getlist('facilities')
            oldhotelid = item_id
            name = form.cleaned_data['name']
            # estd_date = form.cleaned_data['estd_date']
            owner_id = form.cleaned_data['owner_id']
            number_of_room = form.cleaned_data['number_of_room']
            number_of_staff = form.cleaned_data['number_of_staff']
            wordsbyowner = form.cleaned_data['wordsbyowner']
            description = form.cleaned_data['description']
            is_active = False
            image = form.cleaned_data['image']
            obj = HotelsNew(
                oldhotelid=oldhotelid,
                name=name,
                owner_id=owner_id,
                number_of_room=number_of_room,
                number_of_staff=number_of_staff,
                wordsbyowner=wordsbyowner,
                description=description,
                image=image,
            )
            obj.save()
        for fac in facilities:
            facility = HotelFacilities.objects.get(id=fac)
            HotelFacilitiesMiddleNew.objects.create(hotels=obj, hotelsfacilities=facility)
    return redirect('hotel:hotelindex', kwargs={'hotel_id': item_id})


def hotelyouown(request):
    types = request.user.account_type.filter()
    for typ in types:
        if 'hotel_owner' in typ.type:
            hotel = Hotels.objects.filter(owner_id=request.user.id)

            context = {
                'hotels': hotel,
                'message': 'This is Dashboard for hotel Module'
            }
        elif 'hotel_staff' in typ.type:
            id = request.user.id
            company_id = StaffProfile.objects.values_list('company_id', flat=True).get(user=id)
            hotel = Hotels.objects.filter(id=company_id)
            context = {
                'hotels': hotel,
                'message': 'This is Dashboard for hotel Module'
            }
    return render(request, 'hotel/hotel_choice.html', context)


def inventoryyouown(request):
    if 'current_hotel' in request.COOKIES:
        current_hotel = request.COOKIES['current_hotel']

    hotel = Hotels.objects.filter(owner_id=request.user.id)
    types = request.user.account_type.filter()
    for typ in types:
        if 'hotel_owner' in typ.type:
            hotel = Hotels.objects.filter(owner_id=request.user.id)

            context = {
                'hotels': hotel,
                'message': 'This is Dasboard for hotel Module'
            }
        elif 'hotel_staff' in typ.type:
            id = request.user.id
            company_id = StaffProfile.objects.values_list('company_id', flat=True).get(user=id)
            hotel = Hotels.objects.filter(id=company_id)
            context = {
                'hotels': hotel,
                'message': 'This is Dasboard for hotel Module'
            }
    return render(request, 'hotel/inventory_choice.html', context)


def calendar(request, hotel_id):
    hotel_name = Hotels.objects.get(id=hotel_id)
    room_names = HotelInventory.objects.filter(hotel_id = hotel_id).values('roomtype__name','roomtype__id').distinct()
    # room_categories = room_names.objects.values_list('roomtype', flat=True).distinct().order_by()
    room_cat_list =[]
    for room_name in room_names:
        room_cat_dict = {}
        room_cat_dict.update(
            {
                "id": room_name["roomtype__id"],
                "category": room_name["roomtype__name"],
             }
        )
        room_cat_list.append(room_cat_dict)
    context = {
        'hotel_id': hotel_id,
        'hotel_name': hotel_name,
        'hotel_room_categories': room_cat_list
    }
    return render(request, 'calendar/calendar.html', context)


def myjson(request, hotel_id):
    # modules = ModuleBooking.objects.filter(company_id=hotel_id)
    main_list = []
    with connection.cursor() as cursor:
        cursor.execute(
            'SELECT company_id,inventory_id,SUM(quantity) AS room, start_date, end_date  FROM booking_modulebooking where company_id=' + hotel_id + ' GROUP BY company_id, inventory_id, start_date, end_date')
        row = cursor.fetchall()
        for r in row:
            a = list(r)
            module_dict = {}
            company = Hotels.objects.get(id=a[0])
            inventory = HotelInventory.objects.get(id=a[1])
            module_dict.update({'start': a[3]})
            end_date = a[4] + datetime.timedelta(days=1)
            module_dict.update({'end': end_date})
            temp_name = inventory.room_name
            module_dict.update({'title': temp_name})
            if (inventory.no_of_rooms - a[2]) <= 0:
                status = 'Full'
                bgcolor = "red"
                module_dict.update({'backgroundColor': 'red'})
                module_dict.update({'borderColor': 'red'})
            else:
                status = 'Available'
                bgcolor = "green"
                module_dict.update({'backgroundColor': 'green'})
                module_dict.update({'borderColor': 'green'})
            module_dict.update({'description': {'bgcolor': bgcolor, 'Status': status, 'Total': inventory.no_of_rooms,
                                                'Booked': a[2], 'Remaining': (inventory.no_of_rooms - a[2])}})

            main_list.append(module_dict)
    return JsonResponse(main_list, safe=False)


def check_availability(request):
    if request.method == 'POST':
        # initilization
        total_inventory = []
        in_booking = []
        arr = []
        dept = []
        room = []
        flag = []
        status = {}
        final = []
        check_array = []
        myFlag = 0

        # data collection
        hotel_id = request.POST.get('hotel_id')
        check_in = request.POST.get('start_date')
        check_out = request.POST.get('end_date')
        quantity = request.POST.get('quantity')
        adult_max = request.POST.get('adult_max')
        child_max = request.POST.get('child_max')
        module_name = 'hotel'

        status.update({'start_date': check_in})
        status.update({'end_date': check_out})
        final.append(status)
        status = {}

        # check inventory count
        inventory_count = HotelInventory.objects.filter(hotel=hotel_id, adult_max__gte=adult_max,
                                                        child_max__gte=child_max, no_of_rooms__gte=quantity).count()
        if inventory_count > 0:
            inventory_instance = HotelInventory.objects.filter(hotel=hotel_id, adult_max__gte=adult_max,
                                                               child_max__gte=child_max, no_of_rooms__gte=quantity)
            for inventory in inventory_instance:
                if inventory.pk not in total_inventory:
                    total_inventory.append(inventory.pk)

                company_id = inventory.hotel.id
                inventory_id = inventory.pk
                booking_count = ModuleBooking.objects.filter(module_name=module_name,
                                                             company_id=company_id,
                                                             inventory_id=inventory_id).count()

                if booking_count > 0:
                    # for same inventory use booking algorithm
                    booking_instance = ModuleBooking.objects.filter(module_name=module_name,
                                                                    company_id=company_id,
                                                                    inventory_id=inventory_id)

                    for instance in booking_instance:
                        if inventory_id not in in_booking:
                            in_booking.append(instance.inventory_id)
                        arr.append(instance.start_date.strftime('%Y-%m-%d'))
                        dept.append(instance.end_date.strftime('%Y-%m-%d'))
                        room.append(instance.quantity)
                        flag.append(1)

                    arr.append(check_in)
                    dept.append(check_out)
                    flag.append(0)
                    room.append(int(quantity))
                    n = len(arr)
                    inventory_instance = HotelInventory.objects.get(hotel=company_id, id=inventory_id)
                    k = inventory_instance.no_of_rooms

                    room_left = check_booking_available(arr, dept, n, k, room, flag)
                    if room_left != 0:
                        arr = []
                        dept = []
                        room = []
                        if inventory_id not in check_array:
                            status.update({'name': inventory_instance.room_name})
                            status.update({'available': room_left})
                            status.update({'start_date': check_in})
                            status.update({'end_date': check_out})
                            final.append(status)
                            status = {}
                            check_array.append(inventory_id)
                    else:
                        arr = []
                        dept = []
                        room = []

        else:
            myFlag = myFlag + 1
        final_invs = list(set(total_inventory).symmetric_difference(set(in_booking)))

        for final_inv in final_invs:
            if final_inv not in check_array:
                status.update({'name': HotelInventory.objects.get(id=final_inv).room_name})
                status.update({'available': HotelInventory.objects.get(id=final_inv).no_of_rooms})
                status.update({'start_date': check_in})
                status.update({'end_date': check_out})
                final.append(status)
                status = {}
                check_array.append(final_inv)
        if myFlag == 0 or in_booking == None:
            return JsonResponse({
                'success': True,
                "message": 'success',
                'myData': final
            })
        else:
            return JsonResponse({
                'success': True,
                'message': "All rooms are packed for this time frame.",
                'myData': final
            })

    else:
        return JsonResponse({
            'success': False,
            'message': "All rooms are packed for this time frame."
        })


def hotelList(request):
    hotel = Hotels.objects.all()
    context = {
        'hotels': hotel,
    }
    return render(request, 'hotel/hotel_list.html', context)


def hotelStatus(request, id, status):
    if status == 'True':
        status = 0
        Hotels.objects.filter(id=id).update(is_active=status)
    elif status == 'False':
        status = 1
        Hotels.objects.filter(id=id).update(is_active=status)
    return redirect('hotel:hotel_list')


def mass_active(request):
    if request.method == 'POST':
        for i in request.POST.getlist('id[]'):
            instance = Hotels.objects.get(id=i)
            Hotels.objects.filter(id=i).update(is_active=Q(is_active=False))
        return JsonResponse({
            'success': True,
        })


def createorupdate(request, prop_id):
    if Hotels.objects.filter(prop_id_id=prop_id).exists():
        hotel_id = Hotels.objects.filter(prop_id_id=prop_id).first().id
        return reverse_lazy('hotel:hotelupdate', kwargs={'pk': hotel_id})
    else:
        return reverse_lazy('hotel:hotelcreate-withprop', kwargs={'prop_id': prop_id})


import os
from travel import settings
from travel.devsettings import BASE_DIR


def booking_calendar(request, hotel_id):
    hotel_name = Hotels.objects.get(id=hotel_id)
    context = {
        'hotel_id': hotel_id,
        'hotel_name': hotel_name
    }
    return render(request, 'calendar/booking_calendar.html', context)


""" Booking data from api 
    *booking data accourding to hotel id 

"""
def     get_booking_calendar(request, hotel_id):
    # file_path = os.path.join(BASE_DIR, 'static/' 'booking_events.json')
    #
    # with open(file_path) as f:
    #     data = json.load(f)
    # domain = request.META['HTTP_HOST']

    domain = request.META['HTTP_HOST']
    print('domain')
    print(domain)
    baseurl = 'http://128.199.22.231:8006/'
    endpoint = 'get_booking_calendar_by_hotelId/{hotel_id}'.format(hotel_id=hotel_id)
    requestApi = baseurl + endpoint
    response = requests.get(requestApi)
    data = response.json()

    for d in data:
        if 'booking_id' in d.keys():
            path = '/booking/booking_table/show/' + str(d['booking_id'])
            url = 'http://{domain}{path}'.format(domain=domain, path=path)
            d['url'] = url
            d['start'] = datetime.strptime(d['start'], "%m-%d-%Y").strftime("%Y-%m-%d")
            d['end'] = datetime.strptime(d['end'], "%m-%d-%Y").strftime("%Y-%m-%d")

    return JsonResponse(data, safe=False)
