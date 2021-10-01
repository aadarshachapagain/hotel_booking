from django.shortcuts import redirect
from rest_framework.authtoken.models import Token
from django.contrib.auth import (
	REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
	logout as auth_logout, update_session_auth_hash,
)

def for_pulse(request, token, module, operation, id):
	try:
		temp = Token.objects.get(key=token)
		auth_login(request, temp.user)
		a = Switcher()
		temp = a.choose_module(module, operation, id)
		if operation == 'update':
			return redirect(temp, id)
		elif operation == 'create':
			return redirect(temp)
	
	# if we return id from related operation
	# new_id = re.findall('\d+', temp)
	# if new_id:
	# 	new_id = int(new_id[0])
	# 	url = ''.join([i for i in temp if not i.isdigit()])
	# 	return redirect(url, new_id)
	# else:
	# 	url=temp
	# 	return redirect(url)
	
	except Token.DoesNotExist:
		return redirect('login')


class Switcher(object):
	
	def choose_module(self, module, operation, id):
		"""Dispatch method"""
		method_name = str(module)
		# Get the method from 'self'. Default to a lambda.
		method = getattr(self, method_name, lambda: "Invalid Module")
		# Call the method as we return it
		return method(operation, id)
	
	def hotel(self, operation, id):
		hotelInstance = HotelRoute()
		# dynamically call the method of hotelInstance
		method = getattr(hotelInstance, operation, lambda: "Invalid Operation")
		return method(id)
	
	def rental(self, operation, id):
		rentalInstance = RentalRoute()
		# dynamically call the method of hotelInstance
		method = getattr(rentalInstance, operation, lambda: "Invalid Operation")
		return method(id)


class HotelRoute(object):
	def create(self, id):
		url = 'hotel:hotelcreate'
		return url
	
	def update(self, id):
		url = "hotel:hotelupdate"
		return url


class RentalRoute(object):
	def create(self, id):
		url = 'rental:rentalcompanycreate'
		return url
	
	def update(self, id):
		url = "rental:rentalcompanyupdate"
		return url
