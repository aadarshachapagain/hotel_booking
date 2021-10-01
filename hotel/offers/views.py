from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from account.owner_profile.models import OwnerProfile
from hotel.offers.forms import OffersForm
from hotel.offers.models import Offers


@method_decorator([login_required], name='dispatch')
class OffersListView(ListView):
	model = Offers
	template_name = 'offers/index.html'
	
	def get_context_data(self, **kwargs):
		context = super(OffersListView, self).get_context_data(**kwargs)
		current_module=""
		if 'current_module' in self.request.COOKIES:
			current_module = self.request.COOKIES['current_module']
		current_hotel = ""
		if 'current_hotel' in self.request.COOKIES:
			current_hotel = self.request.COOKIES['current_hotel']
		data = Offers.objects.filter(creator=self.request.user.id, module=current_module)
		print(data)
		context['all_items']=data
		context['hotel_id']=current_hotel
		return context


@method_decorator([login_required], name='dispatch')
class OffersDelete(SuccessMessageMixin, DeleteView):
	model = Offers
	success_url = reverse_lazy('hotel:offers-index')
	pk_url_kwarg = 'offer_id'
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Offer Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
class OffersDetail(DetailView):
	model = Offers
	template_name = 'offers/show.html'


@method_decorator([login_required], name='dispatch')
class OffersCreate(SuccessMessageMixin, CreateView):
	template_name = 'offers/create.html'
	model = Offers
	form_class = OffersForm
	success_message = 'New Offer Added Successfully'
	
	
	def get_success_url(self):
		item = self.object
		status = self.form.data['save-status']
		print("hey")
		print(status)
		if status == 'save':
			return reverse_lazy('hotel:offers-index')
		elif status == 'save-assign':
			if 'current_hotel' in self.request.COOKIES:
				current_hotel = self.request.COOKIES['current_hotel']
				return reverse_lazy('hotel:inventory-offers-create', kwargs={'hotel_id': current_hotel})
			
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def form_valid(self, form):
		reward = form.save(commit=False)
		self.form = form
		reward.save()
		print("hey hey")
		return HttpResponseRedirect(self.get_success_url())
	
	def get_context_data(self, **kwargs):
		context = super(OffersCreate, self).get_context_data(**kwargs)
		user = self.request.user
		username = OwnerProfile.objects.get(user=user.id).name
		context['user'] = username
		context['user_id'] = user.id
		return context


class OffersUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'offers/create.html'
	model = Offers
	form_class = OffersForm
	success_message = 'Offer Updated Successfully'
	
	def form_valid(self, form):
		tour = form.save(commit=False)
		tour.is_active = False
		self.form=form
		tour.save()
		return super(OffersUpdate, self).form_valid(form)
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(OffersUpdate, self).get_context_data(**kwargs)
		id = self.kwargs['pk']
		offer = Offers.objects.get(id=id)
		username = OwnerProfile.objects.get(user=offer.creator).name
		context['user'] = username
		context['user_id'] = offer.creator.user.id
		return context
	
	def get_success_url(self):
		item = self.object
		status = self.form.data['save-status']
		print("hey")
		print(status)
		if status == 'save':
			return reverse_lazy('hotel:offers-index')
		elif status == 'save-assign':
			if 'current_hotel' in self.request.COOKIES:
				current_hotel = self.request.COOKIES['current_hotel']
				return reverse_lazy('hotel:inventory-offers-create', kwargs={'hotel_id': current_hotel})
	

	
def mass_delete(request):
	if request.method == 'POST':
		for i in request.POST.getlist('id[]'):
			Offers.objects.filter(id=i).delete()
		return JsonResponse({
			'success': True,
		})
