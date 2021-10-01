import decimal
import json
import datetime

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib import messages

from hotel.cancellation_policy.forms import CancellationForm
from hotel.cancellation_policy.models import Cancellation_Policy
from hotel.child_supplement_policy.forms import ChildSupplementPolicyForm
from hotel.child_supplement_policy.models import ChildSupplementPolicy
from hotel.cribsPolicy.forms import cribsPolicyForm
from hotel.cribsPolicy.models import cribsPolicy
from hotel.extraBed.forms import ExtraBedPolicyForm
from hotel.extraBed.models import ExtraBedPolicy
from hotel.inventory.models import HotelInventory
from hotel.inventoryUpdate.models import InventoryUpdate
from hotel.models import Hotels
from django.db.models import Q

from travel.businessPolicies import send_policies


class InventoryPoliciesList(generic.TemplateView):
	template_name = 'inventoryPolicies/index.html'
	
	def get_context_data(self, **kwargs):
		inventory_id = self.kwargs.get('inventory_id')
		context = {}
		hotel_id = HotelInventory.objects.get(id=inventory_id).hotel_id
		context.update({'hotel_id': hotel_id})
		context.update({'inventory_id': inventory_id})
		context.update({'inv_obj': HotelInventory.objects.get(id=inventory_id)})
		return context


class InventoryPoliciesCreate(SuccessMessageMixin, generic.TemplateView):
	template_name = 'inventoryPolicies/list.html'
	
	def get_success_url(self):
		return reverse_lazy('hotel:inventoryPolicies-list', kwargs={'inventory_id': self.kwargs.get('id')})
	
	def get_context_data(self, **kwargs):
		context = super(InventoryPoliciesCreate, self).get_context_data(**kwargs)
		model = self.kwargs.get('model')
		operation = self.kwargs.get('operation')
		id = self.kwargs.get('id')
		inventory_id = self.kwargs.get('inv_id')
		a = Switcher()
		cancel, title, form, model = a.choose_module(model, operation, id, inventory_id)
		flag1 = 0
		flag2 = 0
		flag3 = 0
		if title != 'Cancellation':
			for c in cancel:
				c.hotelInventory_id = str(c.hotelInventory_id)
				if c.change_status == 'new' and flag1 == 0:
					c.title = 'General Policies'
					flag1 = 1
				elif c.change_status == 'assigned' and flag2 == 0:
					c.title = 'Assigned Policies'
					flag2 = 1
				elif c.change_status == 'copied' and flag3 == 0:
					c.title = 'Specific Policies'
					flag3 = 1
				else:
					c.title = ''
		
		context.update({'title': title})
		context.update({'inventory_id': inventory_id})
		context.update({'hotel_id': id})
		context.update({'all_items': cancel})
		context.update({'inv_object': HotelInventory.objects.get(id=inventory_id)})
		return context


class InventoryPoliciesSave(View):
	
	def post(self, request, *args, **kwargs):
		title = request.POST.get('title')
		title = title.lower()
		operation = request.POST.get('operation')
		id = request.POST.getlist('policy')
		available_checkboxes = request.POST.getlist('available_checkbox')
		inventory = request.POST.get('inventory')
		register = request.POST.get('register')
		a = AssignSwitcher()
		url, mykwargs = a.choose_module(title, operation, id, inventory, register, available_checkboxes, request)
		if 'model' in mykwargs:
			return redirect(url,mykwargs['model'],mykwargs['operation'],mykwargs['id'] ,mykwargs['inv_id'])
		else:
			return redirect(url, mykwargs['inv_id'])


class Switcher(object):
	
	def choose_module(self, model, operation, id, inventory_id):
		"""Dispatch method"""
		method_name = str(model)
		
		# Get the method from 'self'. Default to a lambda.
		method = getattr(self, method_name, lambda: "Invalid Model")
		# Call the method as we return it
		return method(operation, id, inventory_id)
	
	def cancellation(self, operation, id, inventory_id):
		cancellationInstance = CancellationRoute()
		method = getattr(cancellationInstance, operation, lambda: "Invalid Operation")
		return method(id, inventory_id)
	
	def childsupplement(self, operation, id, inventory_id):
		childSupplementInstance = ChildSupplementRoute()
		method = getattr(childSupplementInstance, operation, lambda: "Invalid Operation")
		return method(id, inventory_id)
	
	def extrabed(self, operation, id, inventory_id):
		extraBedInstance = ExtraBedRoute()
		method = getattr(extraBedInstance, operation, lambda: "Invalid Operation")
		return method(id, inventory_id)
	
	def crib(self, operation, id, inventory_id):
		cribInstance = CribRoute()
		method = getattr(cribInstance, operation, lambda: "Invalid Operation")
		return method(id, inventory_id)


class CancellationRoute(object):
	
	def list(self, id, inventory_id):
		temp = send_policies()
		all_items = json.loads(temp)
		if Cancellation_Policy.objects.filter(hotel=id, hotelInventory=inventory_id).exists():
			previous_policies = Cancellation_Policy.objects.filter(hotel=id, hotelInventory=inventory_id)
			for item in all_items:
				for policy in previous_policies:
					if policy.cancellation_type == item.get('name'):
						item['status'] = 'checked'
						break
					else:
						item['status'] = ''
		
		title = 'Cancellation'
		form = CancellationForm
		model = Cancellation_Policy
		return all_items, title, form, model


class ChildSupplementRoute(object):
	
	def list(self, id, inventory_id):
		cancel = ChildSupplementPolicy.objects.filter(Q(hotel=id), Q(hotelInventory=None),
		                                              Q(change_status='new'))
		assigned = ChildSupplementPolicy.objects.filter(Q(hotel=id), Q(hotelInventory=inventory_id),
		                                                Q(change_status='assigned'))
		copied = ChildSupplementPolicy.objects.filter(Q(hotel=id), Q(hotelInventory=inventory_id),
		                                              Q(change_status='copied'))
		parent_id = []
		for assign in assigned:
			cancel = cancel.exclude(id=assign.parent_id)
			parent_id.append(assign.parent_id)
		all_items = cancel | assigned | copied
		all_items = all_items.order_by('change_status')
		title = 'ChildSupplement'
		form = ChildSupplementPolicyForm
		model = ChildSupplementPolicy
		return all_items, title, form, model


class ExtraBedRoute(object):
	
	def list(self, id, inventory_id):
		cancel = ExtraBedPolicy.objects.filter(hotel=id, hotelInventory=None)
		assigned = ExtraBedPolicy.objects.filter(Q(hotel=id), Q(hotelInventory=inventory_id),
		                                         Q(change_status='assigned'))
		copied = ExtraBedPolicy.objects.filter(Q(hotel=id), Q(hotelInventory=inventory_id),
		                                       Q(change_status='copied'))
		parent_id = []
		for assign in assigned:
			cancel = cancel.exclude(id=assign.parent_id)
			parent_id.append(assign.parent_id)
		all_items = cancel | assigned | copied
		all_items = all_items.order_by('change_status')
		title = 'ExtraBed'
		form = ExtraBedPolicyForm
		model = ExtraBedPolicy
		return all_items, title, form, model


class CribRoute(object):
	
	def list(self, id, inventory_id):
		cancel = cribsPolicy.objects.filter(hotel=id, hotelInventory=None)
		assigned = cribsPolicy.objects.filter(Q(hotel=id), Q(hotelInventory=inventory_id),
		                                         Q(change_status='assigned'))
		copied = cribsPolicy.objects.filter(Q(hotel=id), Q(hotelInventory=inventory_id),
		                                       Q(change_status='copied'))
		parent_id = []
		for assign in assigned:
			cancel = cancel.exclude(id=assign.parent_id)
			parent_id.append(assign.parent_id)
		all_items = cancel | assigned | copied
		all_items = all_items.order_by('change_status')
		title = 'Crib'
		form = cribsPolicyForm
		model = cribsPolicy
		return all_items, title, form, model


class AssignSwitcher(object):
	
	def choose_module(self, model, operation, id, inventory, register, available_checkboxes, request):
		"""Dispatch method"""
		method_name = str(model)
		
		# Get the method from 'self'. Default to a lambda.
		method = getattr(self, method_name, lambda: "Invalid Model")
		# Call the method as we return it
		return method(operation, id, inventory, register, available_checkboxes, request)
	
	def cancellation(self, operation, id, inventory, register, available_checkboxes, request):
		cancellationInstance = AssignCancellationRoute()
		# dynamically call the method of hotelInstance
		method = getattr(cancellationInstance, operation, lambda: "Invalid Operation")
		return method(id, inventory, register, available_checkboxes, request)
	
	def childsupplement(self, operation, id, inventory, register, available_checkboxes, request):
		childInstance = AssignChildSupplementRoute()
		# dynamically call the method of hotelInstance
		method = getattr(childInstance, operation, lambda: "Invalid Operation")
		return method(id, inventory, register, available_checkboxes, request)
	
	def extrabed(self, operation, id, inventory, register, available_checkboxes, request):
		extraBedInstance = AssignExtraBedRoute()
		# dynamically call the method of hotelInstance
		method = getattr(extraBedInstance, operation, lambda: "Invalid Operation")
		return method(id, inventory, register, available_checkboxes, request)
	
	def crib(self, operation, id, inventory, register, available_checkboxes, request):
		cribInstance = AssignCribRoute()
		# dynamically call the method of hotelInstance
		method = getattr(cribInstance, operation, lambda: "Invalid Operation")
		return method(id, inventory, register, available_checkboxes, request)


class AssignCancellationRoute(object):
	
	def assign(self, id, inventory, register, available_checkboxes, request):
		date_checkboxes = request.POST.getlist('date_checkbox')
		start_date = request.POST.getlist('start_date')
		end_date = request.POST.getlist('end_date')
		if Cancellation_Policy.objects.filter(hotelInventory=inventory).exists():
			Cancellation_Policy.objects.filter(hotelInventory=inventory).delete()
		for index, available_checkbox in enumerate(available_checkboxes):
			if available_checkbox == 'Yes':
				cancel = Cancellation_Policy()
				cancel.cancellation_type = id[index]
				cancel.hotelInventory = HotelInventory.objects.get(id=inventory)
				cancel.hotel = Hotels.objects.get(id=HotelInventory.objects.get(id=inventory).hotel_id)
				cancel.save()
				# inventoryUpdate
				temp = send_policies()
				all_items = json.loads(temp)
				for item in all_items:
					if item['name'] == id[index]:
						rate = decimal.Decimal(item['room_rate_number'])
						operator = item['room_rate_operator']
						bb_rate = HotelInventory.objects.get(id=inventory).bedandbreakfast_plan
						ep_rate = HotelInventory.objects.get(id=inventory).european_plan
						
						if operator == 'sub':
							bb_update = bb_rate - ((rate * bb_rate) / 100)
							ep_update = ep_rate - ((rate * ep_rate) / 100)
						elif operator == 'add':
							bb_update = bb_rate + ((rate * bb_rate) / 100)
							ep_update = ep_rate + ((rate * ep_rate) / 100)
						else:
							bb_update = bb_rate
							ep_update = ep_rate
						break
				# required if they want date in initial selection
				# if date_checkboxes[index] == 'Yes':
				# 	for i in range((datetime.datetime.strptime(end_date[index], '%Y-%m-%d') + datetime.timedelta(
				# 		days=1) - datetime.datetime.strptime(start_date[index], '%Y-%m-%d')).days):
				# 		inventory_update_instance = InventoryUpdate()
				# 		inventory_update_instance.hotel = Hotels.objects.get(
				# 			id=HotelInventory.objects.get(id=inventory).hotel_id)
				# 		inventory_update_instance.inventory = HotelInventory.objects.get(id=inventory)
				# 		inventory_update_instance.cancellation_type = id[index]
				# 		inventory_update_instance.european_plan = ep_update
				# 		inventory_update_instance.bedandbreakfast_plan = bb_update
				# 		inventory_update_instance.date = datetime.datetime.strptime(start_date[index],
				# 		                                                            '%Y-%m-%d') + datetime.timedelta(
				# 			days=i)
				# 		inventory_update_instance.save()
				#
				# else:
				inventory_update_instance = InventoryUpdate()
				inventory_update_instance.hotel = Hotels.objects.get(
					id=HotelInventory.objects.get(id=inventory).hotel_id)
				inventory_update_instance.inventory = HotelInventory.objects.get(id=inventory)
				inventory_update_instance.cancellation_type = id[index]
				inventory_update_instance.european_plan = ep_update
				inventory_update_instance.bedandbreakfast_plan = bb_update
				inventory_update_instance.save()
				
				
		if register == 'Save and Continue':
			mykwargs = {
				"model": "childsupplement",
				"operation": "list",
				"id": HotelInventory.objects.get(id=inventory).hotel_id,
				"inv_id": inventory,
			}
			url = 'hotel:inventoryPolicies-create'
		else:
			mykwargs = {
				"inv_id": inventory,
			}
			url = 'hotel:showinvdetail'
		return url, mykwargs


class AssignChildSupplementRoute(object):
	
	def assign(self, id, inventory, register, available_checkboxes, request):
		alreadyList = []
		already = ChildSupplementPolicy.objects.filter(change_status='assigned', hotelInventory=inventory)
		if already:
			for a in already:
				alreadyList.append(str(a.pk))
			if len(id) > len(alreadyList):
				refined = list(set(id) - set(alreadyList))
			else:
				refined = list(set(alreadyList) - set(id))
			for r in refined:
				ChildSupplementPolicy.objects.filter(pk=r, change_status='assigned').delete()
		for i in id:
			if not ChildSupplementPolicy.objects.filter(id=i, hotelInventory=inventory).exists():
				cancel = ChildSupplementPolicy.objects.get(id=i)
				instance = ChildSupplementPolicy()
				instance.hotelInventory = HotelInventory.objects.get(id=inventory)
				instance.hotel = Hotels.objects.get(id=HotelInventory.objects.get(id=inventory).hotel_id)
				instance.parent = cancel
				instance.change_status = 'assigned'
				instance.save()
		if register == 'Save and Continue':
			mykwargs = {
				"model": "crib",
				"operation": "list",
				"id": HotelInventory.objects.get(id=inventory).hotel_id,
				"inv_id": inventory,
			}
			url = 'hotel:inventoryPolicies-create'
		else:
			mykwargs = {
				"inv_id": inventory,
			}
			url = 'hotel:showinvdetail'
		return url, mykwargs


class AssignExtraBedRoute(object):
	
	def assign(self, id, inventory, register, available_checkboxes, request):
		alreadyList = []
		already = ExtraBedPolicy.objects.filter(change_status='assigned', hotelInventory=inventory)
		if already:
			for a in already:
				alreadyList.append(str(a.pk))
			if len(id) > len(alreadyList):
				refined = list(set(id) - set(alreadyList))
			else:
				refined = list(set(alreadyList) - set(id))
			for r in refined:
				ExtraBedPolicy.objects.filter(pk=r, change_status='assigned').delete()
		for i in id:
			if not ExtraBedPolicy.objects.filter(id=i, hotelInventory=inventory).exists():
				cancel = ExtraBedPolicy.objects.get(id=i)
				instance = ExtraBedPolicy()
				instance.hotelInventory = HotelInventory.objects.get(id=inventory)
				instance.hotel = Hotels.objects.get(id=HotelInventory.objects.get(id=inventory).hotel_id)
				instance.parent = cancel
				instance.change_status = 'assigned'
				instance.save()
		if register == 'Save and Continue':
			mykwargs = {
				"model": "cancellation",
				"operation": "list",
				"id": HotelInventory.objects.get(id=inventory).hotel_id,
				"inv_id": inventory,
			}
			url = 'hotel:inventoryPolicies-create'
		else:
			mykwargs = {
				"inv_id": inventory,
			}
			url = 'hotel:showinvdetail'
		return url, mykwargs
		

class AssignCribRoute(object):
	
	def assign(self, id, inventory, register, available_checkboxes, request):
		alreadyList = []
		already = cribsPolicy.objects.filter(change_status='assigned', hotelInventory=inventory)
		if already:
			for a in already:
				alreadyList.append(str(a.pk))
			if len(id) > len(alreadyList):
				refined = list(set(id) - set(alreadyList))
			else:
				refined = list(set(alreadyList) - set(id))
			for r in refined:
				cribsPolicy.objects.filter(pk=r, change_status='assigned').delete()
		for i in id:
			if not cribsPolicy.objects.filter(id=i, hotelInventory=inventory).exists():
				cancel = cribsPolicy.objects.get(id=i)
				instance = cribsPolicy()
				instance.hotelInventory = HotelInventory.objects.get(id=inventory)
				instance.hotel = Hotels.objects.get(id=HotelInventory.objects.get(id=inventory).hotel_id)
				instance.parent = cancel
				instance.change_status = 'assigned'
				instance.save()
		if register == 'Save and Exit':
			mykwargs = {
				"inv_id": inventory,
			}
			url = 'hotel:showinvdetail'
			return url, mykwargs
