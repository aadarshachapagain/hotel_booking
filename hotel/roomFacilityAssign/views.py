from django.db import transaction
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from hotel.inventory.models import HotelInventory, hotelinventory_roomfacility
from hotel.roomFacilityAssign.forms import RoomFacilityAssignForm
from hotel.room_facilities.models import RoomFacilities


@method_decorator([login_required], name='dispatch')
class RoomFacilityAssignListView(ListView):
	model = hotelinventory_roomfacility
	template_name = 'roomFacilityAssign/index.html'
	context_object_name = 'all_items'
	
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(RoomFacilityAssignListView, self).get_context_data(**kwargs)
		inventory_id = self.kwargs['item_id']
		facilities = self.model.objects.filter(hotelinventory=inventory_id, roomfacility__category='Advanced')
		context['all_items'] = facilities
		context['item_id'] = inventory_id
		context['hotel_id'] = HotelInventory.objects.get(id=inventory_id).hotel.id
		return context


@method_decorator([login_required], name='dispatch')
class RoomFacilityAssignDelete(SuccessMessageMixin, DeleteView):
	model = hotelinventory_roomfacility
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)
	
	def get_success_url(self):
		item_id = self.object.id
		x = hotelinventory_roomfacility.objects.get(id=item_id)
		return reverse_lazy('hotel:room-facility-assign-index', kwargs={'item_id': x.hotelinventory.id})
	
	def delete(self, *args, **kwargs):
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		return HttpResponseRedirect(success_url)


@method_decorator([login_required], name='dispatch')
class RoomFacilityAssignCreate(FormView):
	template_name = 'roomFacilityAssign/create.html'
	model = hotelinventory_roomfacility
	form_class = RoomFacilityAssignForm
	success_message = 'Information Added Successfully'
	
	def get_success_url(self):
		inventory_id = self.kwargs['item_id']
		if self.form.data['register'] == 'Save and Exit':
			return reverse_lazy('hotel:showinvdetail', kwargs={'pk': inventory_id})
		elif self.form.data['register'] == 'Save and Continue':
			return reverse_lazy('hotel:inventorygallery-create', kwargs={'item_id': inventory_id})
		else:
			return reverse_lazy('hotel:hotelinvcreate', kwargs={'hotel_id': HotelInventory.objects.get(id=inventory_id).hotel_id})
			
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	@transaction.atomic
	def form_valid(self, form):
		self.form = form
		inventory_id = self.kwargs['item_id']
		inventory_insatnce = HotelInventory.objects.get(id=inventory_id)
		facilities = form.data.getlist('roomfaclities')
		available_checkboxes = form.data.getlist('available_checkbox')
		price_checkboxes = form.data.getlist('price_checkbox')
		descriptions = form.data.getlist('description')
		for index, available_checkbox in enumerate(available_checkboxes):
			facility_instance = RoomFacilities.objects.get(id=facilities[index])
			if available_checkbox == 'Yes':
				if hotelinventory_roomfacility.objects.filter(hotelinventory=inventory_insatnce,
				                                              roomfacility=facility_instance).exists():
					hotelinventory_roomfacility.objects.filter(hotelinventory=inventory_insatnce,
					                                           roomfacility=facility_instance).delete()
				facility_instance = hotelinventory_roomfacility()
				facility_instance.hotelinventory = inventory_insatnce
				facility_instance.roomfacility = RoomFacilities.objects.get(id=facilities[index])
				facility_instance.description = descriptions[index]
				facility_instance.cost = price_checkboxes[index]
				facility_instance.save()
			else:
				if hotelinventory_roomfacility.objects.filter(hotelinventory=inventory_insatnce,
				                                              roomfacility=facility_instance).exists():
					hotelinventory_roomfacility.objects.filter(hotelinventory=inventory_insatnce,
					                                           roomfacility=facility_instance).delete()
		
		return super(RoomFacilityAssignCreate, self).form_valid(form)
	
	def get_context_data(self, **kwargs):
		context = super(RoomFacilityAssignCreate, self).get_context_data(**kwargs)
		inventory_id = self.kwargs['item_id']
		pre_selected_facilities = hotelinventory_roomfacility.objects.filter(hotelinventory=inventory_id,
		                                                                     roomfacility__category='Advanced')
		
		# facilities = RoomFacilities.objects.filter(category='Advanced')
		facilities = RoomFacilities.objects.filter(category='Advanced').exclude(hotelinventory=inventory_id)
		context['hotel_inventory'] = HotelInventory.objects.get(id=inventory_id)
		context['facilities'] = facilities
		context['pre_selected_facilities'] = pre_selected_facilities
		return context
