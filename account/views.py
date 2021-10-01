import random
import string

from django.contrib.auth.models import Group, Permission
from django.core.validators import validate_email
from django.db import DatabaseError
from django.shortcuts import render
from django.shortcuts import redirect

from rest_framework.response import Response
from django.views.generic import CreateView
from rest_framework import status

from account.staff_profile.models import StaffProfile
from account.utils import generate_pdf
# from travel_tour.owner.models import Travel_TourOwner
# from travel_tour.staff.models import TravelStaff
# from travel_tour.tour_company.models import TravelCompany
# from rental.rental_company.models import RentalCompany
# from restaurant.restaurant_company.models import RestaurantCompany
from .forms import OwnerSignUpForm
from .forms import StaffSignUpForm
from .forms import NormalUSerSignUpForm
from django.http import HttpResponse, JsonResponse
from account.models import User
from users.models import Users
from hotel.owner.models import HotelOwner
from hotel.staff.models import HotelStaff
from hotel.models import Hotels
from django.db.models import Q
from account.models import Account_Type
from django.contrib import messages

from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from account.owner_profile.models import OwnerProfile
from hotel.staff.decorators import staff_create_decorator
from hotel.staff.decorators import hotel_ownercreate_decorator
from django.utils.html import strip_tags

from django.contrib.auth.backends import ModelBackend

# from pyexcel_xls import get_data as xls_get
# from pyexcel_xlsx import get_data as xlsx_get
# from pyexcel.plugins.parsers import excel
from django.utils.datastructures import MultiValueDictKeyError

# Fcm Testing
from fcm_django.models import FCMDevice


def tochoice(request):
    print('in tochoice')
    devices = FCMDevice.objects.all()
    print('devices')
    print(devices)
    devices.send_message(title="Title", body="Message")
    devices.send_message(title="Title", body="Message", data={"test": "test"})
    devices.send_message(data={"test": "test"})
    print('may be sucessful')
    return render(request, 'dashboard/choice.html')


# FCM Testing


def linktoverification(request):
    if request.method == 'POST':
        user = User.objects.filter(Q(email=request.POST['email']) & Q(is_verified=0)).distinct()
        if user.exists():
            user = User.objects.get(email=request.POST['email'])
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('account/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            email = request.POST['email']
            to_email = email
            email = EmailMultiAlternatives(
                mail_subject, message, 'BIG SAFAR <info@ktmvoyage.com>', to=[to_email]
            )
            email.content_subtype = 'html'
            status = email.send()
            data = {}
            if status == 1:
                data.update({'message': 'Please check your email for confirmation.'})
            else:
                data.update({'message': 'Please enter a valid email address.'})
            return render(request, 'registration/checkEmail.html', data)
        else:
            data = {
                'message': 'Please enter a valid email address.'
            }
            return render(request, 'registration/reverification.html', data)
    else:
        return render(request, 'registration/reverification.html')


# def custom_reset_password(request):
#     if request.method == 'POST':
#         user = User.objects.filter(Q(email=request.POST['email'])).distinct()
#         oldpassword = request.POST['oldpassword']
#         if user.exists():
#             data = {}
#             distinct_user = User.objects.get(Q(email=request.POST['email']))
#             stat = distinct_user.check_password(oldpassword)
#             if stat:
#                 user = User.objects.get(email=request.POST['email'])
#                 current_site = get_current_site(request)
#                 mail_subject = 'Reset Your  Password.'
#                 # 'registration/password_reset_email.html'
#                 # message = render_to_string('account/custom_password_reset_confirm.html', {
#                 #     'user': user,
#                 #     'domain': current_site.domain,
#                 #     'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
#                 #     'token': account_activation_token.make_token(user),
#                 # })
#                 message = render_to_string('registration/password_reset_email.html', {
#                     'protocol': 'http',
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
#                     'token': account_activation_token.make_token(user),
#                 })
#                 email = request.POST['email']
#                 to_email = email
#                 email = EmailMultiAlternatives(
#                     mail_subject, message, 'BIG SAFAR <info@ktmvoyage.com>', to=[to_email]
#                 )
#                 email.content_subtype = 'html'
#                 status = email.send()
#                 # data = {}
#                 if status == 1:
#                     data.update({'message': 'Please check your email for Password Reset link.'})
#                 else:
#                     data.update({'message': 'Please enter a valid email address.'})
#                 return render(request, 'registration/checkEmailNPassword.html', data)
#             else:
#                 data.update({'message': 'Old Password is incorrect.'})
#                 return render(request, 'registration/password_reset_custom_form.html', data)
#         else:
#             data = {
#                 'message': 'Email is incorrect.Please try again'
#             }
#             return render(request, 'registration/password_reset_custom_form.html', data)
#     else:
#         return render(request, 'registration/password_reset_custom_form.html')


def linktoverificationadmin(request):
    if request.method == 'POST':
        user = User.objects.filter(Q(id=request.POST['id']) & Q(is_verified=0)).distinct()
        if user.exists():
            user = User.objects.get(id=request.POST['id'])
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('account/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            email = user.email
            to_email = email
            email = EmailMultiAlternatives(
                mail_subject, message, 'KTM VOYAGE <info@ktmvoyage.com>', to=[to_email]
            )
            email.content_subtype = 'html'
            email.send()
            return JsonResponse({
                'success': True,
                'msg': 'We have send an activation link in your email.'
            })
        else:
            return JsonResponse({
                'success': True,
                'msg': 'Your account has already been verified.'
            })


# @login_required
# @hotel_ownercreate_decorator
def signup(request):
    if request.method == 'POST':
        form = OwnerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_verified = False
            user.is_active = False
            user.save()
            account_type = form.data.getlist('account_type')
            for type in account_type:
                user.account_type.add(type)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('account/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMultiAlternatives(
                mail_subject, message, 'KTM VOYAGE <info@ktmvoyage.com>', to=[to_email]
            )
            email.content_subtype = 'html'
            link = redirect('/dashboard')
            email.send()
            jsfile = 'js/redirectafter5sec.js'
            context = {
                'first_line_message': 'Please verify your email to confirm this registration</br>Click <a href=' + link.url + '>here</a> to login or wait you will be redirected you to the login page',
                'second_line_message': '',
                'jsfile': jsfile,
            }
            return render(request, 'travel/default_page.html', context)
            # return HttpResponse('Please confirm your email address to complete the registration')
        else:
            # if request.user.is_superuser:
            account_type = Account_Type.objects.filter(type__contains='_owner')

            context = {
                'account_types': account_type,
                'form': form
            }
            return render(request, 'account/signup_form.html', context)
    else:
        form = OwnerSignUpForm()
        # if request.user.is_superuser:
        account_type = Account_Type.objects.filter(type__contains='_owner')
        context = {
            'account_types': account_type,
            'form': form
        }
        return render(request, 'account/signup_form.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        token = account_activation_token.check_token(user, token)
        user.is_verified = True
        user.is_active = True
        user.save()

        id = user.id
        login(request, user)
        usertmp = request.user.account_type.all()
        temp = OwnerProfile.objects.filter(user=user).count()
        if temp == 0:
            OwnerProfile.objects.create(user=user)

        # for tmp in usertmp:
        #     if tmp.type == 'hotel_owner':
        #         OwnerProfile.objects.create(user=user)
        #     elif tmp.type == 'travel_tour_owner':
        #         OwnerProfile.objects.create(user=user)

        pwtoken = PasswordResetTokenGenerator().make_token(user)
        newuid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
        # return redirect('password_reset_confirm', uidb64=newuid, token=pwtoken)
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')


def reset_account_password(request):
    user = request.user
    pwtoken = PasswordResetTokenGenerator().make_token(user)
    newuid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
    return redirect('password_reset_confirm', uidb64=newuid, token=pwtoken)


# @method_decorator([login_required], name='dispatch')
# # To create staff of travel this decorator is commented
# @method_decorator(staff_create_decorator, name='dispatch')
# class StaffSignUpView(CreateView):
# 	model = User
# 	form_class = StaffSignUpForm
# 	template_name = 'account/signup_form.html'
#
# 	def get_context_data(self, **kwargs):
# 		message = None
# 		account_type = Account_Type.objects.filter()
#
# 		# if 'current_hotel' in self.request.COOKIES:
# 		#     current_hotel = self.request.COOKIES['current_hotel']
# 		#     if current_hotel != 'empty':
# 		#         hotels = Hotels.objects.filter(owner_id=self.request.user.id, is_active=True, id=current_hotel)
# 		hotels = Hotels.objects.filter(owner_id=self.request.user.id, is_active=True).order_by(
# 			'id').reverse()
# 		hotels = Hotels.objects.filter(owner_id=self.request.user.id).order_by(
# 			'id').reverse()
# 		travelcompany = TravelCompany.objects.filter(owner_id=self.request.user.id, status=1).order_by('id').reverse()
# 		rentalcompany = RentalCompany.objects.filter(owner_id=self.request.user.id).order_by(
# 			'id').reverse()
# 		restaurantcompany = RestaurantCompany.objects.filter(owner_id=self.request.user.id).order_by(
# 			'id').reverse()
# 		form = StaffSignUpForm(self.request.POST)
#
# 		usertmp = self.request.user.account_type.all()
# 		if 'current_module' in self.request.COOKIES:
# 			current_module = self.request.COOKIES['current_module']
# 		allaccounttypes = usertmp
# 		for user in usertmp:
# 			if (user.type == 'hotel_owner' and current_module == 'hotel'):
# 				if 'current_hotel' in self.request.COOKIES:
# 					current_hotel = self.request.COOKIES['current_hotel']
# 					if current_hotel != 'empty':
# 						hotels = Hotels.objects.filter(owner_id=self.request.user.id, id=current_hotel)
# 				if (hotels.count() <= 0):
# 					message = 'Sorry, You have no any verified Hotel to create Staffs.'
# 				account_type = Account_Type.objects.filter(type='hotel_staff')
# 			elif (user.type == 'travel_tour_owner' and current_module == 'travel_tour'):
# 				if (travelcompany.count() <= 0):
# 					message = 'Sorry, You have no any verified Travel Company to create Staffs.'
# 				account_type = Account_Type.objects.filter(type='travel_tour_staff')
# 			elif (user.type == 'rental_owner' and current_module == 'rental'):
# 				if 'current_company' in self.request.COOKIES:
# 					current_company = self.request.COOKIES['current_company']
# 					if current_company != 'empty':
# 						rentalcompany = RentalCompany.objects.filter(owner_id=self.request.user.id,
# 						                                             id=current_company)
# 				if (rentalcompany.count() <= 0):
# 					message = 'Sorry, You have no any verified Rental Company to create Staffs.'
# 				account_type = Account_Type.objects.filter(type='rental_staff')
# 			elif (user.type == 'restaurant_owner' and current_module == 'restaurant'):
# 				if 'current_company' in self.request.COOKIES:
# 					current_company = self.request.COOKIES['current_company']
# 					if current_company != 'empty':
# 						restaurantcompany = RestaurantCompany.objects.filter(owner_id=self.request.user.id,
# 						                                                     id=current_company)
# 				if (restaurantcompany.count() <= 0):
# 					message = 'Sorry, You have no any verified Restaurants Company to create Staffs.'
# 				account_type = Account_Type.objects.filter(type='restaurant_staff')
# 		context = {
# 			'message': message,
# 			'account_types': account_type,
# 			'allaccounttypes': allaccounttypes,
# 			'hotels': hotels,
# 			'travelcompanies': travelcompany,
# 			'rentalcompanies': rentalcompany,
# 			'current_module': current_module,
# 			'restaurantcompanies': restaurantcompany,
# 			'form': form
# 		}
# 		return context
#
# 	def form_valid(self, form):
# 		user = form.save(commit=False)
# 		user.is_verified = True
# 		user.is_active = True
# 		user.save()
# 		account_type = form.data.getlist('account_type')
# 		for type in account_type:
# 			user.account_type.add(type)
# 		hotel_id = form.data.get('hotel_id')
# 		owner_id = self.request.user.id
# 		userallaccounts = self.request.user.account_type.all()
# 		if 'current_module' in self.request.COOKIES:
# 			current_module = self.request.COOKIES['current_module']
# 		# name = form.data.get('first_name') + " " + form.data.get('last_name')
# 		for account in userallaccounts:
# 			if account.type == 'hotel_owner' and current_module == 'hotel':
# 				module = 'hotel'
# 				hotelstaff = StaffProfile.objects.create(user=user, owner_id=owner_id, company_id=hotel_id,
# 				                                         module=module)
# 			# account_type = Account_Type.objects.filter(type='hotel_staff')
# 			elif account.type == 'travel_tour_owner' and current_module == 'travel_tour':
# 				module = 'travel_tour'
# 				travelstaff = StaffProfile.objects.create(user=user, owner_id=owner_id, company_id=hotel_id,
# 				                                          module=module)
#
# 			elif account.type == 'rental_owner' and current_module == 'rental':
# 				module = 'rental'
# 				travelstaff = StaffProfile.objects.create(user=user, owner_id=owner_id, company_id=hotel_id,
# 				                                          module=module)
#
# 			elif account.type == 'restaurant_owner' and current_module == 'restaurant':
# 				module = 'restaurant'
# 				travelstaff = StaffProfile.objects.create(user=user, owner_id=owner_id, company_id=hotel_id,
# 				                                          module=module)
#
# 			# account_type = Account_Type.objects.filter(type='travel_tour_staff')
#
# 		# name = form.data.get('first_name') + " " + form.data.get('last_name')
# 		# staff = HotelStaff.objects.create(user=user, owner_id_id=owner_id, hotel_id=hotel_id, name=name)
# 		id = user.id
# 		return redirect('staffindex')
#
# 	# def form_invalid(self, form):
# 	#     account_type = Account_Type.objects.filter(type='hotel_staff')
# 	#     print('hello dai')
# 	#     usertmp = self.request.user.account_type.all()
# 	#     hotels = Hotels.objects.filter(owner_id=self.request.user.id, is_active=True).order_by(
# 	#         'id').reverse()
# 	#     travelcompany = TravelCompany.objects.filter(owner_id=self.request.user.id, status=1).order_by('id').reverse()
# 	#
# 	#     for user in usertmp:
# 	#         if user == 'hotel_owner':
# 	#             account_type = Account_Type.objects.filter(type='hotel_staff')
# 	#
# 	#         elif user == 'travel_tour_owner':
# 	#             account_type = Account_Type.objects.filter(type='travel_tour_staff')
# 	#
# 	#     context = {
# 	#         'account_types': account_type,
# 	#         'allaccounttypes': usertmp,
# 	#         'hotels': hotels,
# 	#         'form': form,
# 	#         'travelcompanies': travelcompany,
# 	#
# 	#     }
# 	#     return render(self.request, 'account/signup_form.html', context)
# 	def form_invalid(self, form):
# 		messages.warning(self.request, form.errors)
# 		return self.render_to_response(self.get_context_data(form=form, error=form.errors))
#
# super(StaffSignUpView, self)
#
# account_type = Account_Type.objects.filter(type='hotel_staff')
# print('hello dai')
# usertmp = self.request.user.account_type.all()
# hotels = Hotels.objects.filter(owner_id=self.request.user.id, is_active=True).order_by(
#     'id').reverse()
# travelcompany = TravelCompany.objects.filter(owner_id=self.request.user.id, status=1).order_by('id').reverse()
#
# for user in usertmp:
#     if user == 'hotel_owner':
#         account_type = Account_Type.objects.filter(type='hotel_staff')
#
#     elif user == 'travel_tour_owner':
#         account_type = Account_Type.objects.filter(type='travel_tour_staff')
#
# context = {
#     'account_types': account_type,
#     'allaccounttypes': usertmp,
#     'hotels': hotels,
#     'form': form,
#     'travelcompanies': travelcompany,
#
# }
# return render(self.request, 'account/signup_form.html', context)


def NormalUserSignUpView(request):
    if request.method == 'POST':
        form = NormalUSerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            html_content = render_to_string('account/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMultiAlternatives(
                mail_subject, html_content, 'KTM VOYAGE <info@ktmvoyage.com>', to=[to_email]
            )
            email.content_subtype = 'html'
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = NormalUSerSignUpForm()
    return render(request, 'account/signup_form.html', {'form': form})


def normalactivate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        owner = Users.objects.create(user=user)
        id = user.id
        return redirect('hotel:hotelindex')

    else:
        return HttpResponse('Activation link is invalid!')


def NormalUserLoginViewSet(request):
    return HttpResponse("hello")


def UserList(request):
    all_items = User.objects.filter(account_type__type__icontains='_owner').distinct()
    for item in all_items:
        cumullative = ''
        accountTypes = item.account_type.filter()
        for type in accountTypes:
            if cumullative == '':
                cumullative = type.display_name
            else:
                cumullative = cumullative + ' | ' + type.display_name
        item.accountType = cumullative
    accountType = Account_Type.objects.filter(type__icontains='_owner')
    typeFilters = {}
    typeFiltersList = []
    statusFilters = {}
    statusFiltersList = []
    for type in accountType:
        typeFilters.update({'value': type.display_name})
        typeFilters.update({'name': 5})
        typeFiltersList.append(typeFilters)
        typeFilters = {}

    totalStatus = all_items.values('is_active').distinct()
    for status in totalStatus:
        stat = 'Active' if status.get('is_active') == 1 else 'Inactive'
        statusFilters.update({'value': stat})
        statusFilters.update({'name': 4})
        statusFiltersList.append(statusFilters)
        statusFilters = {}

    context = {
        'all_items': all_items,
        'accountType': accountType,
        'statusFilters': statusFiltersList,
        'typeFilters': typeFiltersList
    }
    return render(request, 'user/index.html', context)


def UserActive(request, id, active):
    if active == 'True':
        value = 0

    elif active == 'False':
        value = 1

    User.objects.filter(id=id).update(is_active=value)
    return redirect('user_list')


def mass_active(request):
    if request.method == 'POST':
        for i in request.POST.getlist('id[]'):
            User.objects.filter(id=i).update(is_active=Q(is_active=False))
        return JsonResponse({
            'success': True,
        })


def UserUpdate(request, id):
    item = User.objects.get(pk=id)
    if request.method == 'POST':
        data = request.POST.copy()
        account_type = data.getlist('account_type')
        groups = data.getlist('groups')
        permissions = data.getlist('permissions')
        item.account_type.through.objects.filter(user_id=id).delete()
        item.groups.through.objects.filter(user_id=id).delete()
        item.user_permissions.through.objects.filter(user_id=id).delete()
        for type in account_type:
            item.account_type.add(type)
        for group in groups:
            group = Group.objects.get(id=group)
            group.user_set.add(item)
        for permission in permissions:
            permission = Permission.objects.get(id=permission)
            item.user_permissions.add(permission)
        return redirect('user_list')
    else:
        data = {
            'item': item,
            'permissions': Permission.objects.exclude(user=item.id),
            'selectedPermission': item.user_permissions.all(),
            'selectedGroup': item.groups.all(),
            'groups': Group.objects.exclude(user=item.id),
            'account_types': item.account_type.filter().distinct(),
            'all_types': Account_Type.objects.exclude(account_type=item.id),
        }
        return render(request, 'user/create.html', data)


def find_account_type(request, id):
    user_instance = User.objects.get(id=id)
    account_types = user_instance.account_type.filter()

    if len(account_types) == 0:
        return render(request, 'travel/404error.html')

    for account_type in account_types:
        type = account_type.type
        if 'owner' in type:
            return redirect('ownerprofileshow', id)
        elif 'staff' in type:
            return redirect('staffupdate', id)


def temp(request):
    current_site = get_current_site(request)

    data = {
        'domain': current_site.domain,
    }
    return render(request, 'account/acc_active_email.html', data)


class CustomBackend(ModelBackend):  # requires to define two functions authenticate and get_user
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # below line gives query set,you can change the queryset as per your requirement
            user = UserModel.objects.filter(
                Q(username__iexact=username) |
                Q(email__iexact=username)
            ).distinct()

        except UserModel.DoesNotExist:
            return None

        if user.exists():
            ''' get the user object from the underlying query set,
            there will only be one object since username and email
            should be unique fields in your models.'''
            user_obj = user.first()
            if user_obj.check_password(password):
                return user_obj
            return None
        else:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None


def bulkinvitation(request):
    account_types = Account_Type.objects.filter()
    data = {
        'account_types': account_types,
    }
    return render(request, 'account/bulkinvitation.html', data)


def string_num_generator(size):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


def uploadbulkemail(request):
    if request.method == "POST":
        print('request.P:')
        print(request.POST.get('account_type'))
        account_type = request.POST.get('account_type')
        repeatedemail = []
        emaillist = []
        uniqueemaillist = []
        filehandle = request.FILES['file']

        try:
            excel_file = request.FILES['file']
            if (str(excel_file).split('.')[-1] == "xlsx"):
                data = xlsx_get(excel_file, column_limit=4)
            else:
                return HttpResponse("Type misMatched")

        except MultiValueDictKeyError:
            return HttpResponse("you uploaded nothing")

        for i, (key, value) in enumerate(data.items()):
            emaillist = value

        print('len(emaillist)')
        print(len(emaillist))

        for i in range(1, len(emaillist) - 1):
            try:
                if emaillist[i][1]:
                    fieldvalue = emaillist[i][1]
                    if fieldvalue not in uniqueemaillist and emaillist[i][1] != '':
                        uniqueemaillist.append(emaillist[i][1])
            except IndexError:
                print("this doesn't exist")

        print('uniqueemaillist')
        print(uniqueemaillist)

        for email in uniqueemaillist:
            try:
                validate_email(email)
                valid_email = True
            except:
                valid_email = False

            if not valid_email:
                return HttpResponse('Email address from file are not valid. Please recheck email.')
            else:
                user = User()
                try:
                    user.is_verified = False
                    user.is_active = False
                    password = User.objects.make_random_password()
                    user.set_password(password)
                    user.email = email
                    user.save()
                    user.account_type.add(account_type)
                except DatabaseError:
                    repeatedemail.append(email)

                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('account/acc_active_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'token': account_activation_token.make_token(user),
                })
                to_email = email
                email = EmailMultiAlternatives(
                    mail_subject, message, 'flytrip@codeforcore.com', to=[to_email]
                )
                email.content_subtype = 'html'
                email.send()
                if len(repeatedemail) > 0:
                    data = {
                        'error': "Some emails already exists in System",
                        'repeated email': repeatedemail
                    }
        return HttpResponse('Please confirm your email address to complete the registration')

    # for i in range(1, len(emaillist) - 1):
    #     fieldvalue = emaillist[i][1]
    #     if fieldvalue not in uniqueemaillist:
    #         uniqueemaillist.append(emaillist[i][1])
    #         user = User()
    #         user.is_verified = False
    #         user.is_active = False
    #         password = User.objects.make_random_password()
    #         user.set_password(password)
    #         tempemail = emaillist[i][1]
    #         user.email = tempemail
    #         user.save()
    #         user.account_type.add(account_type)
    #
    #
    #         current_site = get_current_site(request)
    #         mail_subject = 'Activate your account.'
    #         message = render_to_string('account/acc_active_email.html', {
    #             'user': user,
    #             'domain': current_site.domain,
    #             'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
    #             'token': account_activation_token.make_token(user),
    #         })
    #         to_email = tempemail
    #         email = EmailMultiAlternatives(
    #             mail_subject, message, 'flytrip@codeforcore.com', to=[to_email]
    #         )
    #         email.content_subtype = 'html'
    #         email.send()
    return HttpResponse('Please confirm your email address to complete the registration')


def unsubscribe(request):
    return render(request, 'account/unsubscribe.html')


def agreement(request):
    pdf = generate_pdf(request, 'account/agreement.html')
    return HttpResponse(pdf, content_type='application/pdf')
