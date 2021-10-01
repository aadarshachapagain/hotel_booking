from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from booking.booking_table.models import BookingTable
from booking.reward.models import Reward
from booking.reward.forms import RewardForm
from booking.customer.models import Customer


class RewardView(ListView):
	model = Reward
	template_name = 'reward/index.html'
	context_object_name = 'all_items'


# @method_decorator([login_required], name='dispatch')
class RewardDelete(SuccessMessageMixin, DeleteView):
	model = Reward
	
	def get_success_url(self):
		return reverse_lazy('booking:reward')
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)


# @method_decorator([login_required], name='dispatch')
class RewardDetail(DetailView):
	model = Reward
	template_name = 'reward/show.html'
	queryset = Reward.objects.all()
	
	def get_context_data(self, **kwargs):
		context = super(RewardDetail, self).get_context_data(**kwargs)
		return context


class RewardCreate(SuccessMessageMixin, CreateView):
	template_name = 'reward/create.html'
	model = Reward
	form_class = RewardForm
	success_message = 'Information Added Successfully'
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def form_valid(self, form):
		module = form.save(commit=False)
		module.save()
		return super(RewardCreate, self).form_valid(form)
	
	def get_context_data(self, **kwargs):
		context = super(RewardCreate, self).get_context_data(**kwargs)
		booking = BookingTable.objects.all()
		customer = Customer.objects.all()
		context['booking'] = booking
		context['customer'] = customer
		return context
	
	def get_success_url(self):
		return reverse_lazy('booking:reward')


@method_decorator([login_required], name='dispatch')
class RewardUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'reward/create.html'
	model = Reward
	form_class = RewardForm
	success_message = 'Information Updated Successfully'
	queryset = Reward.objects.all()
	
	def get_success_url(self):
		item = self.object
		return reverse_lazy('booking:reward')
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def form_valid(self, form):
		module = form.save(commit=False)
		module.save()
		return super(RewardUpdate, self).form_valid(form)
	
	def get_context_data(self, **kwargs):
		context = super(RewardUpdate, self).get_context_data(**kwargs)
		booking = BookingTable.objects.all()
		context['booking'] = booking
		return context
