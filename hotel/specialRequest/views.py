from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from hotel.models import Hotels
from hotel.specialRequest.forms import specialRequestForm
from hotel.specialRequest.models import specialRequest


class specialRequestListView(ListView):
	model = specialRequest
	template_name = 'specialRequest/index.html'
	context_object_name = 'all_items'
	
	def get_context_data(self, **kwargs):
		context = super(specialRequestListView, self).get_context_data(**kwargs)
		# nisham suggested that special request are assigned by admin not vendor 03/24/2020
		# hotel_id = self.kwargs.get('item_id')
		# all_items = self.model.objects.filter(hotel =hotel_id )
		# context.update({'hotel_id': hotel_id})
		all_items = self.model.objects.all()
		context.update({'all_items': all_items})
		return context


@method_decorator([login_required], name='dispatch')
class specialRequestCreate(SuccessMessageMixin, CreateView):
	template_name = 'specialRequest/create.html'
	model = specialRequest
	form_class = specialRequestForm
	success_message = 'Information Added Successfully'
	
	def form_valid(self, form):
		form.save(commit=False)
		items = form.data.getlist('item')
		# hotel = form.data.get('hotel')
		for item in items:
			instance = self.model()
			instance.item = item
			# instance.hotel = Hotels.objects.get(pk=hotel)
			instance.save()
		return HttpResponseRedirect(self.get_success_url())
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(specialRequestCreate, self).get_context_data(**kwargs)
		return context
	
	def get_success_url(self):
		# return reverse_lazy('hotel:specialRequest', kwargs={'item_id': self.kwargs.get('item_id')})
		return reverse_lazy('hotel:specialRequest')
	
	def get_form_kwargs(self):
		kwargs = super(specialRequestCreate, self).get_form_kwargs()
		hotel_id = self.kwargs.get('item_id')
		kwargs['action'] = 'create'
		# kwargs['hotel'] = hotel_id
		return kwargs


@method_decorator([login_required], name='dispatch')
class specialRequestUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'specialRequest/create.html'
	model = specialRequest
	form_class = specialRequestForm
	success_message = 'Information Updated Successfully'
	queryset = specialRequest.objects.all()
	
	def form_valid(self, form):
		# self.hotel = form.data.get('hotel')
		form.save()
		return HttpResponseRedirect(self.get_success_url())
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
		
	def get_context_data(self, **kwargs):
		context = super(specialRequestUpdate, self).get_context_data(**kwargs)
		return context
	
	def get_form_kwargs(self):
		kwargs = super(specialRequestUpdate, self).get_form_kwargs()
		pk = self.kwargs.get('pk')
		# hotel_id = specialRequest.objects.get(pk=pk).hotel_id
		# kwargs['hotel'] = hotel_id
		kwargs['action'] = 'edit'
		return kwargs
	
	def get_success_url(self):
		# hotel_id =self.hotel
		# return reverse_lazy('hotel:specialRequest', kwargs={'item_id':hotel_id})
		return reverse_lazy('hotel:specialRequest')


@method_decorator([login_required], name='dispatch')
class specialRequestDelete(SuccessMessageMixin, DeleteView):
	model = specialRequest
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted.")
		return self.post(request, *args, **kwargs)
	
	def get_success_url(self):
		# item_id = self.object.id
		# hotel_id = specialRequest.objects.get(id=item_id).hotel_id
		# return reverse_lazy('hotel:specialRequest', kwargs={'item_id': hotel_id})
		return reverse_lazy('hotel:specialRequest')
	
	def delete(self, *args, **kwargs):
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		return HttpResponseRedirect(success_url)
