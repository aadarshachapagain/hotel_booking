import requests
from django.contrib import messages
from django.utils.datetime_safe import datetime
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from account.staff_profile.models import StaffProfile
from booking.booking_table.models import BookingTable
from booking.booking_table.forms import BookingTableForm

from booking.customer.models import Customer
from booking.hotel_booking_log.models import HotelBookingLog
from booking.module_booking.models import ModuleBooking
from hotel.inventory.models import HotelInventory
from hotel.models import Hotels
from django.shortcuts import render, redirect


class BookingTableView(ListView):
    model = BookingTable
    template_name = 'booking_table/index.html'
    context_object_name = 'all_items'

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['company_id']
        context = super(BookingTableView, self).get_context_data(**kwargs)
        all_items = BookingTable.objects.filter(booking__company_id=item_id)
        company_name = None
        for item in all_items:
            company_name = Hotels.objects.get(id=item_id)
            item.company_name = company_name.name

        context['company'] = company_name
        context['all_items'] = all_items
        context['company_id'] = item_id
        return context


# @method_decorator([login_required], name='dispatch')
class BookingTableDelete(SuccessMessageMixin, DeleteView):
    model = BookingTable

    def get_success_url(self):
        return reverse_lazy('booking:booking-table')

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


# @method_decorator([login_required], name='dispatch')
class BookingTableDetail(DetailView):
    model = BookingTable
    template_name = 'booking_table/show.html'
    queryset = BookingTable.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookingTableDetail, self).get_context_data(**kwargs)
        item_id = self.kwargs['pk']
        modules = ModuleBooking.objects.filter(booking=item_id)
        booking = BookingTable.objects.get(id=item_id)
        hotelBookingLogInstancecount = HotelBookingLog.objects.filter(booking=item_id).count()
        if hotelBookingLogInstancecount == 0:
            booking.checkStatus = 'new'
        else:
            hotelBookingLogInstance = HotelBookingLog.objects.get(booking=item_id)
            booking.checkStatus = hotelBookingLogInstance.status
            booking.checkin = hotelBookingLogInstance.checkin_date
            booking.checkout = hotelBookingLogInstance.checkout_date
        company_name = None
        for item in modules:
            if item.module_name == 'hotel':
                company_name = Hotels.objects.get(id=item.company_id)
                inventory_name = HotelInventory.objects.get(id=item.inventory_id)
                item.company_name = company_name.name
                item.inventory_name = inventory_name.room_name

        context['hotel_id'] = item.company_id
        context['modules'] = modules
        context['booking'] = booking
        return context


# @method_decorator([login_required], name='dispatch')
class BookingTableDetailAdmin(DetailView):
    model = BookingTable
    template_name = 'booking_table/adminShow.html'
    queryset = BookingTable.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookingTableDetailAdmin, self).get_context_data(**kwargs)
        item_id = self.kwargs['pk']
        modules = ModuleBooking.objects.filter(booking=item_id)
        booking = BookingTable.objects.get(id=item_id)
        hotelBookingLogInstancecount = HotelBookingLog.objects.filter(booking=item_id).count()
        if hotelBookingLogInstancecount == 0:
            booking.checkStatus = 'new'
        else:
            hotelBookingLogInstance = HotelBookingLog.objects.get(booking=item_id)
            booking.checkStatus = hotelBookingLogInstance.status
            booking.checkin = hotelBookingLogInstance.checkin_date
            booking.checkout = hotelBookingLogInstance.checkout_date
        company_name = None
        for item in modules:
            if item.module_name == 'hotel':
                company_name = Hotels.objects.get(id=item.company_id)
                inventory_name = HotelInventory.objects.get(id=item.inventory_id)
                item.company_name = company_name.name
                item.inventory_name = inventory_name.room_name
                context['hotel_name'] = company_name.name
                context['hotel_phone1'] = company_name.address.contact1
                context['hotel_phone2'] = company_name.address.contact2
        context['modules'] = modules
        context['booking'] = booking
        return context


class BookingTableCreate(SuccessMessageMixin, CreateView):
    template_name = 'booking_table/create.html'
    model = BookingTable
    form_class = BookingTableForm
    success_message = 'Information Added Successfully'

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        module = form.save(commit=False)
        module.save()
        return super(BookingTableCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BookingTableCreate, self).get_context_data(**kwargs)
        customer = Customer.objects.all()
        print('customer')
        print(customer)
        context['customer'] = customer
        return context

    def get_success_url(self):
        return reverse_lazy('booking:booking-table')


@method_decorator([login_required], name='dispatch')
class BookingTableUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'booking_table/create.html'
    model = BookingTable
    form_class = BookingTableForm
    success_message = 'Information Updated Successfully'
    queryset = BookingTable.objects.all()

    def get_success_url(self):
        item = self.object
        return reverse_lazy('booking:booking-table')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        module = form.save(commit=False)
        module.save()
        return super(BookingTableUpdate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BookingTableUpdate, self).get_context_data(**kwargs)

        return context


def BookingUpdateStatus(request, pk, status):
    if status == '0':
        # 	checkin
        hotelBookingLogInstance = HotelBookingLog.objects.create()
        hotelBookingLogInstance.checkin_date = datetime.today()
        hotelBookingLogInstance.checkout_date = None
        hotelBookingLogInstance.booking = BookingTable.objects.get(id=pk)
        hotelBookingLogInstance.staff = StaffProfile.objects.get(user_id=11)
        hotelBookingLogInstance.status = 0
        hotelBookingLogInstance.save()
    if status == '1':
        # 	checkout
        hotelBookingLogInstance = HotelBookingLog.objects.get(booking=pk)
        hotelBookingLogInstance.checkout_date = datetime.today()
        hotelBookingLogInstance.status = 1
        hotelBookingLogInstance.save()
    return redirect('booking:booking-table-show', pk=pk)


def BookingUpdateSeenStatus(request, pk, status):
    if status == '1':
        # 	seen
        bookingTableInstance = BookingTable.objects.get(id=pk)
        bookingTableInstance.seenStatus = True
        bookingTableInstance.save()
    return redirect('booking:booking-table-show', pk=pk)


def BookingDetail(request, booking_id):


    baseurl = 'http://128.199.22.231:8006/'
    endpoint = 'get_booking_confirmation/{booking_id}'.format(booking_id=booking_id)
    requestApi = baseurl + endpoint
    response = requests.get(requestApi)
    data = response.json()

    booking_detail = {
        "email": "abc@gmail.com",
        "country": "Nepal",
        "address": "Thamel-10, kathmandu",
        "customer": "Mr John Doe",
        "total_price": data["paymentDetails_Grand_total_cost"],
        "discount": 120,
        "tax": data["paymentDetails_VAT_13_percent"],
        "bookedPolicy": data["bookedPolicy"],
        "paymentMethod": data["paymentDetails_paymentMethod"],
        "paymentStatus": "Completed",
        "booking_id": "abcd1234",
        "checkin": data["checkIn"],
        "checkout": data["checkOut"],

    }

    context = {
        'hotel_id': data["hotelId"],
        'object': booking_detail
    }

    return render(request, 'booking_table/show.html', context)
