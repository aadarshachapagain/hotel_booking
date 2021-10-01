import requests
from django.contrib import messages
from django.db.models import Count, Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from account.staff_profile.models import StaffProfile
from booking.booking_table.models import BookingTable
from booking.hotel_booking_log.forms import HotelBookingLogForm
from booking.hotel_booking_log.models import HotelBookingLog
from booking.module_booking.models import ModuleBooking
from booking.module_booking.forms import ModuleBookingForm

from booking.customer.models import Customer
from hotel.inventory.models import HotelInventory
from hotel.models import Hotels


# class ModuleBookingView(ListView):
#     model = ModuleBooking
#     template_name = 'module_booking/index.html'
#     context_object_name = 'all_items'
#
#     def get_context_data(self, **kwargs):
#         item_id = self.kwargs['pk']
#         context = super(ModuleBookingView, self).get_context_data(**kwargs)
#         modules = ModuleBooking.objects.filter(company_id=item_id)
#         unique = modules.values('booking').annotate(dcount=Count('booking'))
#         all_items = []
#         for item in unique:
#             new_item = {}
#             bookingid = item['booking']
#             customer_id = BookingTable.objects.get(id=bookingid)
#             new_item.update({'id': bookingid})
#             new_item.update({'customer_name': customer_id.customer.name})
#             new_item.update({'customer_phone': customer_id.customer.contact})
#             new_item.update({'booking_date': customer_id.booked_date})
#             temp1 = ModuleBooking.objects.filter(booking=bookingid).aggregate(Sum('quantity'))
#             new_item.update({'quantity': temp1['quantity__sum']})
#             new_item.update({'seenStatus': customer_id.seenStatus})
#             all_items.append(new_item)
#         context['hotel_id'] = item_id
#         context['all_items'] = all_items
#         return context


class AdminBookingList(ListView):
    model = ModuleBooking
    template_name = 'module_booking/admin_index.html'
    context_object_name = 'all_items'

    def get_context_data(self, **kwargs):
        context = super(AdminBookingList, self).get_context_data(**kwargs)
        modules = ModuleBooking.objects.all()
        unique = modules.values('booking').annotate(dcount=Count('booking'))
        all_items = []
        for item in unique:
            new_item = {}
            bookingid = item['booking']
            customer_id = BookingTable.objects.get(id=bookingid)
            new_item.update({'id': bookingid})
            new_item.update({'customer_name': customer_id.customer.name})
            new_item.update({'customer_phone': customer_id.customer.contact})
            new_item.update({'booking_date': customer_id.booked_date})
            temp1 = ModuleBooking.objects.filter(booking=bookingid)
            company_name = Hotels.objects.get(id=temp1[0].company_id)
            inventory_name = HotelInventory.objects.get(id=temp1[0].inventory_id)
            new_item.update({'company': company_name.name})
            new_item.update({'inventory': inventory_name.room_name})
            new_item.update({'seenStatus': customer_id.seenStatus})
            all_items.append(new_item)
        context['all_items'] = all_items
        return context


# @method_decorator([login_required], name='dispatch')
class ModuleBookingDelete(SuccessMessageMixin, DeleteView):
    model = ModuleBooking

    def get_success_url(self):
        return reverse_lazy('booking:module-booking')

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


# @method_decorator([login_required], name='dispatch')
class ModuleBookingDetail(DetailView):
    model = ModuleBooking
    template_name = 'module_booking/show.html'
    queryset = ModuleBooking.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ModuleBookingDetail, self).get_context_data(**kwargs)
        item_id = self.kwargs['pk']
        item = ModuleBooking.objects.get(id=item_id)
        company_name = None
        if item.module_name == 'hotel':
            company_name = Hotels.objects.get(id=item.company_id)
            inventory_name = HotelInventory.objects.get(id=item.inventory_id)
            hotelBookingLogInstancecount = HotelBookingLog.objects.filter(module_booking=item_id).count()
            if hotelBookingLogInstancecount == 0:
                item.checkStatus = 'new'
            else:
                hotelBookingLogInstance = HotelBookingLog.objects.get(module_booking=item_id)
                item.checkStatus = hotelBookingLogInstance.status
                item.checkin = hotelBookingLogInstance.checkin_date
                item.checkout = hotelBookingLogInstance.checkout_date

            item.company_name = company_name.name
            item.inventory_name = inventory_name.room_name

        context['all_items'] = item
        return context


class ModuleBookingCreate(SuccessMessageMixin, CreateView):
    template_name = 'module_booking/create.html'
    model = ModuleBooking
    form_class = ModuleBookingForm
    success_message = 'Information Added Successfully'

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        module = form.save(commit=False)
        module.save()
        return super(ModuleBookingCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ModuleBookingCreate, self).get_context_data(**kwargs)
        booking = BookingTable.objects.all()
        customer = Customer.objects.all()
        context['booking'] = booking
        context['customer'] = customer
        return context

    def get_success_url(self):
        return reverse_lazy('booking:module-booking')


@method_decorator([login_required], name='dispatch')
class ModuleBookingUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'module_booking/create.html'
    model = ModuleBooking
    form_class = ModuleBookingForm
    success_message = 'Information Updated Successfully'
    queryset = ModuleBooking.objects.all()

    def get_success_url(self):
        item = self.object
        return reverse_lazy('booking:module-booking')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        module = form.save(commit=False)
        module.save()
        return super(ModuleBookingUpdate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ModuleBookingUpdate, self).get_context_data(**kwargs)
        return context


import os
from travel import settings
import json
from travel.devsettings import BASE_DIR

""" Booking data by hotel id
*all rooms that are booked on all dates

"""

def list_booking(request, hotel_id):
    # file_path = os.path.join(BASE_DIR, 'static/' 'booking_events.json')
    # with open(file_path) as f:
    #     data = json.load(f)
    # context = {
    #     'all_items': data
    # }

    domain = request.META['HTTP_HOST']
    baseurl = 'http://128.199.22.231:8006/'
    endpoint = 'get_booking_calendar_by_hotelId/{hotel_id}'.format(hotel_id=hotel_id)
    requestApi = baseurl + endpoint
    response = requests.get(requestApi)
    data = response.json()
    context = {
        'all_items': data
    }
    return render(request, 'module_booking/index.html', context)
