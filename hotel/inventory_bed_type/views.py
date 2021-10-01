from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from hotel.bedType.models import BedType
from hotel.inventory.models import HotelInventory
from hotel.inventorygallery.models import InventoryGallery
from hotel.priceOfRoom.models import PriceInDiffSys
from users.models import Users
# from travel_tour.tour_include.models import TravelInclude
# from travel_tour.tour_include.forms import TravelIncludeForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models import Q

from hotel.inventory_bed_type.models import Inventory_Bed_Type
from hotel.inventory_bed_type.forms import InventoryBedTypeForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from hotel.cancellation_policy.models import Cancellation_Policy
from hotel.cancellation_policy.forms import CancellationForm


@method_decorator([login_required], name='dispatch')
class Inventory_Bed_TypeListView(ListView):
	model = Inventory_Bed_Type
	template_name = 'inventory_bed_type/index.html'
	context_object_name = 'all_items'
	
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(Inventory_Bed_TypeListView, self).get_context_data(**kwargs)
		item_id = self.kwargs['item_id']
		cancel = Inventory_Bed_Type.objects.filter(inventory=item_id)
		context['all_items'] = cancel
		context['item_id'] = item_id
		context['hotel_id'] = HotelInventory.objects.get(id=item_id).hotel.id
		return context


@method_decorator([login_required], name='dispatch')
# @method_decorator(hotel_delete_decorator, name='dispatch')
class Inventory_Bed_TypeDelete(SuccessMessageMixin, DeleteView):
	model = Inventory_Bed_Type
	# success_url = reverse_lazy('hotel:showinvdetail')
	pk_url_kwarg = 'include_id'
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)
	
	def get_success_url(self):
		item_id = self.object.id
		x = Inventory_Bed_Type.objects.get(id=item_id)
		return reverse_lazy('hotel:inv-bed-type-index', kwargs={'item_id': x.inventory.id})
	
	def delete(self, *args, **kwargs):
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		return HttpResponseRedirect(success_url)


@method_decorator([login_required], name='dispatch')
class Inventory_Bed_TypeDetail(DetailView):
	model = Inventory_Bed_Type
	template_name = 'inventory_bed_type/show.html'
	queryset = Inventory_Bed_Type.objects.all().values()


@method_decorator([login_required], name='dispatch')
# @method_decorator(hotel_create_decorator, name='dispatch')
class Inventory_Bed_TypeCreate(SuccessMessageMixin, CreateView):
	template_name = 'inventory_bed_type/create.html'
	model = Inventory_Bed_Type
	form_class = InventoryBedTypeForm
	success_message = 'Information Added Successfully'
	
	def get_success_url(self, **kwargs):
		item = self.form.cleaned_data['inventory']
		price = PriceInDiffSys.objects.filter(inventory=item.id).count()
		if price <= 0:
			return reverse_lazy('hotel:inventory-price-create', kwargs={'inv_id': item.id})
		else:
			return reverse_lazy('hotel:inv-bed-type-index', kwargs={'item_id': item.id})
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def form_valid(self, form):
		form.save(commit=False)
		bed_type = form.data.getlist('bed_type')
		bed_count = form.data.getlist('bed_count')
		inventory = HotelInventory.objects.get(id=form.data.get('inventory'))
		for index, count in enumerate(bed_count):
			cancel = Inventory_Bed_Type()
			cancel.bed_count = count
			cancel.bed_type = BedType.objects.get(id=bed_type[index])
			cancel.inventory = inventory
			cancel.save()
			self.form = form
		return HttpResponseRedirect(self.get_success_url())
	
	def get_context_data(self, **kwargs):
		context = super(Inventory_Bed_TypeCreate, self).get_context_data(**kwargs)
		room_id = self.kwargs['item_id']
		x = HotelInventory.objects.get(id=room_id)
		bed_type = BedType.objects.all()
		context['bed_types'] = bed_type
		context['hotel_inventory'] = x
		return context


# @method_decorator(login_required, name='dispatch')
# @method_decorator(hotel_update_decorator, name='dispatch')
class Inventory_Bed_TypeUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'inventory_bed_type/create.html'
	model = Inventory_Bed_Type
	form_class = InventoryBedTypeForm
	success_message = 'Information Updated Successfully'
	
	
	def get_success_url(self):
		item = self.form.cleaned_data['inventory']
		return reverse_lazy('hotel:inv-bed-type-index', kwargs={'item_id': item.id})
	
	def form_valid(self, form):
		"""If the form is valid, redirect to the supplied URL."""
		self.form = form
		form.save()
		return HttpResponseRedirect(self.get_success_url())
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		pk = self.kwargs['pk']
		context = super(Inventory_Bed_TypeUpdate, self).get_context_data(**kwargs)
		x = self.model.objects.get(id=pk)
		bed_type = BedType.objects.all()
		context['bed_types'] = bed_type
		context['hotel_inventory'] = HotelInventory.objects.get(id=x.inventory_id)
		return context

