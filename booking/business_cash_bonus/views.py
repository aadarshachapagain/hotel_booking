
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from booking.business_cash_bonus.forms import BusinessCashBonusForm
from booking.business_cash_bonus.models import BusinessCashBonus


@method_decorator([login_required], name='dispatch')
class BusinessCashBonusListView(ListView):
	model = BusinessCashBonus
	template_name = 'business_cash_bonus/index.html'
	context_object_name = 'all_items'


@method_decorator([login_required], name='dispatch')
class BusinessCashBonusDelete(SuccessMessageMixin, DeleteView):
	model = BusinessCashBonus
	success_url = reverse_lazy('booking:business-cash-bonus-index')
	pk_url_kwarg = 'business_id'
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
# class BusinessCashBonusDetail(DetailView):
#     model = BusinessCashBonus
#     template_name = 'business_cash_bonus/show.html'

@method_decorator([login_required], name='dispatch')
class BusinessCashBonusCreate(SuccessMessageMixin, CreateView):
	template_name = 'business_cash_bonus/create.html'
	model = BusinessCashBonus
	form_class = BusinessCashBonusForm
	success_message = 'Cash Bonus Added Successfully'
	
	def get_success_url(self):
		return reverse_lazy('booking:business-cash-bonus-index')
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def form_valid(self, form):
		virtual = form.save(commit=False)
		virtual.save()
		return super(BusinessCashBonusCreate, self).form_valid(form)


class BusinessCashBonusUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'business_cash_bonus/create.html'
	model = BusinessCashBonus
	form_class = BusinessCashBonusForm
	success_message = 'Bonus Cash Updated Successfully'
	
	def form_valid(self, form):
		tour = form.save(commit=False)
		tour.is_active = False
		tour.save()
		return super(BusinessCashBonusUpdate, self).form_valid(form)
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(BusinessCashBonusUpdate, self).get_context_data(**kwargs)
		return context
	
	def get_success_url(self):
		return reverse_lazy('booking:business-cash-bonus-index')
