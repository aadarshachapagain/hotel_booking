from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from hotel.room_facilities.forms import RoomFacilitiesForm
from hotel.room_facilities.models import RoomFacilities
from users.models import Users

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


@method_decorator([login_required], name='dispatch')
class RoomFacilitiesList(ListView):
	model = RoomFacilities
	template_name = 'room_facilities/index.html'
	context_object_name = 'room_facilities'


@method_decorator([login_required], name='dispatch')
class RoomFacilitiesDetail(DetailView):
	model = RoomFacilities
	template_name = 'room_facilities/show.html'
	queryset = RoomFacilities.objects.all()


@method_decorator([login_required], name='dispatch')
class RoomFacilitiesCreate(SuccessMessageMixin, CreateView):
	template_name = 'room_facilities/create.html'
	model = RoomFacilities
	form_class = RoomFacilitiesForm
	success_message = 'Information Added Successfully'
	success_url = reverse_lazy('hotel:room-facilities')
	
	def get_success_url(self):
		if self.form.data['register'] == 'Save and Exit':
			return reverse_lazy('hotel:room-facilities')
		else:
			return reverse_lazy('hotel:room-facilities-create')
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(RoomFacilitiesCreate, self).get_context_data(**kwargs)
		context['users'] = Users.objects.all().order_by('id').reverse()
		return context
	
	def form_valid(self, form):
		self.form = form
		return super(RoomFacilitiesCreate, self).form_valid(form)

@method_decorator([login_required], name='dispatch')
class RoomFacilitiesUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'room_facilities/create.html'
	model = RoomFacilities
	form_class = RoomFacilitiesForm
	success_message = 'Information Updated Successfully'
	queryset = RoomFacilities.objects.all()
	
	def get_success_url(self):
		if self.form.data['register'] == 'Save and Exit':
			return reverse_lazy('hotel:room-facilities')
		else:
			return reverse_lazy('hotel:room-facilities-create')
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(RoomFacilitiesUpdate, self).get_context_data(**kwargs)
		context['users'] = Users.objects.all().order_by('id').reverse()
		return context
	
	def form_valid(self, form):
		self.form = form
		return super(RoomFacilitiesUpdate, self).form_valid(form)


@method_decorator([login_required], name='dispatch')
class RoomFacilitiesDelete(SuccessMessageMixin, DeleteView):
	model = RoomFacilities
	success_url = reverse_lazy('hotel:room-facilities')
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)
