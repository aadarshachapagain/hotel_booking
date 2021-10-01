from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from hotel.inventory.models import HotelInventory
from hotel.inventoryOffers.forms import InventoryOffersForm
from hotel.inventoryOffers.models import InventoryOffers
from hotel.offers.models import Offers


@method_decorator([login_required], name='dispatch')
class InventoryOffersListView(ListView):
	model = InventoryOffers
	template_name = 'inventoryOffers/index.html'
	
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(InventoryOffersListView, self).get_context_data(**kwargs)
		hotel_id = self.kwargs['hotel_id']
		context['hotel_id'] = hotel_id
		context['all_items'] = InventoryOffers.objects.filter(hotel_inventory__hotel=hotel_id)
		return context


@method_decorator([login_required], name='dispatch')
class InventoryOffersDelete(SuccessMessageMixin, DeleteView):
	model = InventoryOffers
	pk_url_kwarg = 'inventory_offer_id'
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Offer Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)
	
	def get_success_url(self):
		item_id = self.object.hotel_inventory
		x = HotelInventory.objects.get(id=item_id.id).hotel_id
		return reverse_lazy('hotel:showinvdetail', kwargs={'pk': item_id.id})
	
	def delete(self, *args, **kwargs):
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		return HttpResponseRedirect(success_url)


@method_decorator([login_required], name='dispatch')
class InventoryOffersDetail(DetailView):
	model = InventoryOffers
	template_name = 'inventoryOffers/show.html'


@method_decorator([login_required], name='dispatch')
class InventoryOffersCreate(SuccessMessageMixin, CreateView):
	template_name = 'inventoryOffers/create.html'
	model = InventoryOffers
	form_class = InventoryOffersForm
	success_message = 'New Offer Added Successfully'
	
	def get_context_data(self, **kwargs):
		context = super(InventoryOffersCreate, self).get_context_data(**kwargs)
		hotel_id = self.kwargs['hotel_id']
		related_inventory = HotelInventory.objects.filter(hotel_id=hotel_id)
		offers = Offers.objects.filter(module='Hotel', creator=self.request.user.id)
		context['hotel_id'] = hotel_id
		context['related_inventories'] = related_inventory
		context['offers'] = offers
		return context
	
	def get_success_url(self, **kwargs):
		item = self.form.cleaned_data['hotel_inventory']
		
		hotel_id = HotelInventory.objects.get(id=item.id).hotel_id
		return reverse_lazy('hotel:offers-index')
		# return reverse_lazy('hotel:hotelindex', kwargs={'hotel_id': hotel_id})
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def form_valid(self, form):
		form.save(commit=False)
		formData = form.data
		# print(formData.getlist('hotel_inventory'))
		for inv in formData.getlist('hotel_inventory'):
			instance = InventoryOffers()
			instance.offer = Offers.objects.get(id=formData['offer'])
			instance.hotel_inventory = HotelInventory.objects.get(id=inv)
			instance.status = formData['status']
			instance.save()
		self.form = form
		return HttpResponseRedirect(self.get_success_url())


class InventoryOffersUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'inventoryOffers/create.html'
	model = InventoryOffers
	form_class = InventoryOffersForm
	success_message = 'Offer Updated Successfully'
	
	def form_valid(self, form):
		tour = form.save(commit=False)
		tour.is_active = False
		self.form = form
		tour.save()
		return super(InventoryOffersUpdate, self).form_valid(form)
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(InventoryOffersUpdate, self).get_context_data(**kwargs)
		hotel_id = InventoryOffers.objects.get(id=self.kwargs['pk']).hotel_inventory
		context['hotel_id'] = hotel_id
		return context
	
	def get_success_url(self):
		item = self.form.cleaned_data['hotel_inventory']
		hotel_id = HotelInventory.objects.get(id=item.id).hotel_id
		return reverse_lazy('hotel:inventory-offers-index', kwargs={'hotel_id': hotel_id})
