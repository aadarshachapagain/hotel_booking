from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from booking.booking_table.models import BookingTable
from booking.hotel_booking_log.forms import HotelBookingLogForm
from booking.hotel_booking_log.models import HotelBookingLog
from booking.module_booking.models import ModuleBooking
from booking.module_booking.forms import ModuleBookingForm

from booking.customer.models import Customer
from hotel.inventory.models import HotelInventory
from hotel.models import Hotels


class HotelBookingLogView(ListView):
	model = HotelBookingLog
	template_name = 'hotel_booking_log/index.html'
	context_object_name = 'all_items'
	
	# def get_context_data(self, **kwargs):
	# 	item_id = self.kwargs['pk']
	# 	context = super(ModuleBookingView, self).get_context_data(**kwargs)
	# 	all_items = ModuleBooking.objects.filter(company_id=item_id)
	# 	company_name = None
	# 	for item in all_items:
	# 		if item.module_name == 'hotel':
	# 			company_name = Hotels.objects.get(id=item.company_id)
	# 			inventory_name = HotelInventory.objects.get(id = item.inventory_id)
	# 			item.company_name = company_name.name
	# 			item.inventory_name = inventory_name.room_name
	#
	# 	context['company']=company_name
	# 	context['all_items'] = all_items
	# 	return context


# @method_decorator([login_required], name='dispatch')
class HotelBookingLogDelete(SuccessMessageMixin, DeleteView):
	model = HotelBookingLog
	
	def get_success_url(self):
		return reverse_lazy('booking:hotel-booking-log')
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)


# @method_decorator([login_required], name='dispatch')
class HotelBookingLogDetail(DetailView):
	model = HotelBookingLog
	template_name = 'hotel_booking_log/show.html'
	queryset = HotelBookingLog.objects.all()
	
	# def get_context_data(self, **kwargs):
	# 	context = super(ModuleBookingDetail, self).get_context_data(**kwargs)
	# 	item_id = self.kwargs['pk']
	# 	item = ModuleBooking.objects.get(id=item_id)
	# 	company_name = None
	# 	if item.module_name == 'hotel':
	# 		company_name = Hotels.objects.get(id=item.company_id)
	# 		inventory_name = HotelInventory.objects.get(id=item.inventory_id)
	# 		item.company_name = company_name.name
	# 		item.inventory_name = inventory_name.room_name
	# 	context['all_items'] = item
	# 	return context


class HotelBookingLogCreate(SuccessMessageMixin, CreateView):
	template_name = 'hotel_booking_log/create.html'
	model = HotelBookingLog
	form_class = HotelBookingLogForm
	success_message = 'Information Added Successfully'
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def form_valid(self, form):
		module = form.save(commit=False)
		module.save()
		return super(HotelBookingLogCreate, self).form_valid(form)
	
	def get_context_data(self, **kwargs):
		context = super(HotelBookingLogCreate, self).get_context_data(**kwargs)
		booking = BookingTable.objects.all()
		customer = Customer.objects.all()
		context['booking'] = booking
		context['customer'] = customer
		return context
	
	def get_success_url(self):
		return reverse_lazy('booking:hotel-booking-log')


@method_decorator([login_required], name='dispatch')
class HotelBookingLogUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'hotel_booking_log/create.html'
	model = HotelBookingLog
	form_class = HotelBookingLogForm
	success_message = 'Information Updated Successfully'
	queryset = HotelBookingLog.objects.all()
	
	def get_success_url(self):
		item = self.object
		return reverse_lazy('booking:hotel-booking-log')
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def form_valid(self, form):
		module = form.save(commit=False)
		module.save()
		return super(HotelBookingLogUpdate, self).form_valid(form)
	
	def get_context_data(self, **kwargs):
		context = super(HotelBookingLogUpdate, self).get_context_data(**kwargs)
		return context
