from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from hotel.address.models import HotelAddress
from hotel.models import Hotels
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from hotel.CommissionPaymentPolicies.models import CommissionPaymentPolicies
from hotel.CommissionPaymentPolicies.forms import CommissionPaymentPoliciesForm
from hotel.propertyDetail.models import PropertyDetail

__author__ = "Aashish Paudel"


@method_decorator([login_required], name="dispatch")
class CommissionPaymentPoliciesListView(ListView):
	model = CommissionPaymentPolicies
	template_name = "CommissionPaymentPolicies/index.html"
	context_object_name = "all_items"
	
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(CommissionPaymentPoliciesListView, self).get_context_data(**kwargs)
		item_id = self.kwargs["item_id"]
		policy = CommissionPaymentPolicies.objects.filter(hotel=item_id)
		context["all_items"] = policy
		context["item_id"] = item_id
		return context


@method_decorator([login_required], name="dispatch")
class CommissionPaymentPoliciesCreate(SuccessMessageMixin, CreateView):
	template_name = "CommissionPaymentPolicies/create.html"
	model = CommissionPaymentPolicies
	form_class = CommissionPaymentPoliciesForm
	success_message = "Information Added Successfully"
	
	def get_success_url(self, **kwargs):
		hotel_id = self.kwargs.get("item_id")
		if self.form.data['register'] == 'Save and Exit':
			url = reverse_lazy('hotel:hotelindex', kwargs={'hotel_id': hotel_id})
		else:
			url = reverse_lazy('hotel:hotelinvcreate', kwargs={'hotel_id': hotel_id})
		return url
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		hotel_id = self.kwargs.get("item_id")
		return self.render_to_response(
			self.get_context_data(object=form.data, hotel_id=hotel_id)
		)
	
	def form_valid(self, form):
		form.save(commit=False)
		hotel = get_object_or_404(Hotels, pk=self.kwargs.get("item_id"))
		if CommissionPaymentPolicies.objects.filter(hotel=hotel.pk).exists():
			policy = CommissionPaymentPolicies.objects.get(hotel=hotel.pk)
		else:
			policy = CommissionPaymentPolicies()
		policy.hotel = hotel
		policy.commission_percentage = form.data.get('commission_percentage')
		policy.invoice_name = PropertyDetail.objects.get(id=form.data.get('invoice_name'))
		if form.data.get('address_radio') == 'No':
			policy.alternative_address = form.data.get('alternative_address')
			policy.primary_address = None
		else:
			policy.alternative_address = None
			policy.primary_address = HotelAddress.objects.get(hotel = self.kwargs.get("item_id"))
			
		policy.save()
		self.form = form
		return HttpResponseRedirect(self.get_success_url())
	
	def get_context_data(self, **kwargs):
		context = super(CommissionPaymentPoliciesCreate, self).get_context_data(**kwargs)
		package_id = self.kwargs["item_id"]
		user = self.request.user.id
		if CommissionPaymentPolicies.objects.filter(hotel=Hotels.objects.get(id=package_id).pk).exists():
			context["object"] = CommissionPaymentPolicies.objects.get(hotel=Hotels.objects.get(id=package_id).pk)
		context["property_names"]=PropertyDetail.objects.filter(user = user)
		context["hotel_id"] = Hotels.objects.get(id=package_id).pk
		context["form"] = self.form_class
		return context


@method_decorator([login_required], name="dispatch")
class CommissionPaymentPoliciesDelete(SuccessMessageMixin, DeleteView):
	model = CommissionPaymentPolicies
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)
	
	def get_success_url(self):
		item_id = self.object.id
		x = CommissionPaymentPolicies.objects.get(id=item_id)
		return reverse_lazy("hotel:commission-payment-policies-index", kwargs={"item_id": x.hotel.id})
	
	def delete(self, *args, **kwargs):
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		return HttpResponseRedirect(success_url)
