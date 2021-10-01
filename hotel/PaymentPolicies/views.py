from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from hotel.CreditCard.models import CreditCard
from hotel.models import Hotels
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from hotel.PaymentPolicies.models import PaymentPolicies
from hotel.PaymentPolicies.forms import PaymentPoliciesForm
from datetime import datetime

__author__ = "Aashish Paudel"


@method_decorator([login_required], name="dispatch")
class PaymentPoliciesListView(ListView):
	model = PaymentPolicies
	template_name = "PaymentPolicies/index.html"
	context_object_name = "all_items"
	
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(PaymentPoliciesListView, self).get_context_data(**kwargs)
		item_id = self.kwargs["item_id"]
		policy = PaymentPolicies.objects.filter(hotel=item_id)
		context["all_items"] = policy
		context["item_id"] = item_id
		return context


@method_decorator([login_required], name="dispatch")
class PaymentPoliciesCreate(SuccessMessageMixin, CreateView):
	template_name = "PaymentPolicies/create.html"
	model = PaymentPolicies
	form_class = PaymentPoliciesForm
	success_message = "Information Added Successfully"
	
	def get_success_url(self, **kwargs):
		hotel_id = self.kwargs.get("item_id")
		if self.form.data['register'] == 'Save and Exit':
			url = reverse_lazy('hotel:hotelindex', kwargs={'hotel_id': hotel_id})
		else:
			url = reverse_lazy('hotel:commission-payment-policies-create', kwargs={'item_id': hotel_id})
		return url
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		hotel_id = self.kwargs.get("item_id")
		return self.render_to_response(
			self.get_context_data(object=form.data, hotel_id=hotel_id)
		)
	
	def form_valid(self, form):
		form.save(commit=False)
		credit_cards = form.data.getlist('credit_card')
		hotel = get_object_or_404(Hotels, pk=self.kwargs.get("item_id"))
		available_radio = form.data.get('available_radio')
		PaymentPolicies.objects.filter(hotel=hotel.pk).delete()
		if available_radio == 'Yes':
			for card in credit_cards:
				policy = PaymentPolicies()
				policy.hotel = hotel
				policy.credit_card = CreditCard.objects.get(id=card)
				policy.save()
		self.form = form
		return HttpResponseRedirect(self.get_success_url())
	
	def get_context_data(self, **kwargs):
		context = super(PaymentPoliciesCreate, self).get_context_data(**kwargs)
		package_id = self.kwargs["item_id"]
		hotel_id = Hotels.objects.get(id=package_id).pk
		pre_payment_policies = PaymentPolicies.objects.filter(hotel=hotel_id)
		all_credit_cards = CreditCard.objects.all()
		for pre in pre_payment_policies:
			all_credit_cards=all_credit_cards.exclude(id=pre.credit_card_id)
		context["hotel_id"] = hotel_id
		context["credit_cards"] = all_credit_cards
		context["pre_credit_cards"] = pre_payment_policies
		return context


@method_decorator([login_required], name="dispatch")
class PaymentPoliciesDelete(SuccessMessageMixin, DeleteView):
	model = PaymentPolicies
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)
	
	def get_success_url(self):
		item_id = self.object.id
		x = PaymentPolicies.objects.get(id=item_id)
		return reverse_lazy("hotel:payment-policies-index", kwargs={"item_id": x.hotel.id})
	
	def delete(self, *args, **kwargs):
		self.object = self.get_object()
		success_url = self.get_success_url()
		self.object.delete()
		return HttpResponseRedirect(success_url)
