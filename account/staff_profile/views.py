from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password, password_changed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# from ..owner.models import OwnerProfile
# from .models import StaffProfile
# from .forms import StaffProfileForm
from django.contrib import messages
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from account.models import User
from account.owner_profile.models import OwnerProfile
from account.staff_profile.forms import StaffProfileForm
from account.staff_profile.models import StaffProfile
from hashutils import make_pw_hash, check_pw_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from hotel.models import Hotels
from hotel.staff.decorators import staff_create_decorator, staff_view_decorator
from hotel.staff.decorators import staff_update_decorator
# from travel_tour.tour_company.models import TravelCompany
# from rental.rental_company.models import RentalCompany
# from restaurant.restaurant_company.models import RestaurantCompany


@method_decorator([login_required], name='dispatch')
@method_decorator(staff_view_decorator, name='dispatch')
class StaffListView(ListView):
    model = StaffProfile
    template_name = 'staffprofile/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        user = self.request.user

        if 'current_module' in self.request.COOKIES:
            current_module = self.request.COOKIES['current_module']

        if (current_module == 'hotel'):
            if 'current_hotel' in self.request.COOKIES:
                current_hotel = self.request.COOKIES['current_hotel']
                hotel_id = current_hotel
                hotelname = Hotels.objects.values_list('name', flat=True).get(id=hotel_id)

            staff = StaffProfile.objects.filter(company_id=hotel_id, module=current_module)
            context = super(StaffListView, self).get_context_data(**kwargs)
            if staff:
                context['all_items'] = staff
                context['module'] = current_module
                context['companyname'] = hotelname
                context['hotel_id'] = hotel_id
                return context
            else:
                context['staff_list'] = 'No any staff has been registered.'
                context['companyname'] = hotelname
                context['module'] = current_module
                context['hotel_id'] = hotel_id
                return context

        # if (current_module == 'travel_tour'):
        #     context = super(StaffListView, self).get_context_data(**kwargs)
        #     if 'current_company' in self.request.COOKIES:
        #         current_company = self.request.COOKIES['current_company']
        #         travel_id = current_company
        #         context['travel_id'] = travel_id
        #         hotelname = TravelCompany.objects.values_list('name', flat=True).get(id=travel_id)
        #     staff = StaffProfile.objects.filter(company_id=travel_id, module=current_module).count()
        #
        #     if staff > 0:
        #         context['all_items'] = StaffProfile.objects.filter(company_id=travel_id, module=current_module)
        #         context['companyname'] = hotelname
        #         context['module'] = current_module
        #         return context
        #     else:
        #         context['staff_list'] = 'No any staff has been registered.'
        #         context['companyname'] = hotelname
        #         context['module'] = current_module
        #         return context
        #
        # if (current_module == 'rental'):
        #     if 'current_company' in self.request.COOKIES:
        #         current_rental = self.request.COOKIES['current_company']
        #         rental_id = current_rental
        #         rentalname = RentalCompany.objects.values_list('name', flat=True).get(id=rental_id)
        #         context = super(StaffListView, self).get_context_data(**kwargs)
        #         context['rental_id'] = rental_id
        #
        #     staff = StaffProfile.objects.filter(company_id=rental_id, module=current_module)
        #     if staff:
        #         context['all_items'] = staff
        #         context['companyname'] = rentalname
        #         context['module'] = current_module
        #         return context
        #     else:
        #         context['staff_list'] = 'No any staff has been registered.'
        #         context['companyname'] = rentalname
        #         context['module'] = current_module
        #         return context
        #
        # if (current_module == 'restaurant'):
        #     if 'current_company' in self.request.COOKIES:
        #         current_restaurant = self.request.COOKIES['current_company']
        #         restaurant_id = current_restaurant
        #         restaurantname = RestaurantCompany.objects.values_list('name', flat=True).get(id=restaurant_id)
        #     staff = StaffProfile.objects.filter(company_id=restaurant_id, module=current_module)
        #     context = super(StaffListView, self).get_context_data(**kwargs)
        #     if staff:
        #         context['all_items'] = staff
        #         context['companyname'] = restaurantname
        #         context['module'] = current_module
        #         context['restaurant_id'] = restaurant_id
        #         return context
        #     else:
        #         context['staff_list'] = 'No any staff has been registered.'
        #         context['companyname'] = restaurantname
        #         context['module'] = current_module
        #         context['restaurant_id'] = restaurant_id
        #         return context


@method_decorator([login_required], name='dispatch')
@method_decorator(staff_update_decorator, name='dispatch')
class StaffDelete(SuccessMessageMixin, DeleteView):
    model = StaffProfile
    success_url = reverse_lazy('staffindex')

    # pk_url_kwarg='staff_id'
    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
# @method_decorator(staff_create_decorator,name='dispatch')
class StaffDetail(DetailView):
    model = StaffProfile
    template_name = 'staffprofile/show.html'
    queryset = StaffProfile.objects.all()

    # def get_context_data(self, **kwargs):
    #         context = super(StaffListView, self).get_context_data(**kwargs)


# @method_decorator([login_required], name='dispatch')
# @method_decorator(staff_create_decorator, name='dispatch')
class StaffCreate(SuccessMessageMixin, CreateView):
    template_name = 'staffprofile/create.html'
    model = StaffProfile
    form_class = StaffProfileForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('staffindex')

    def form_valid(self, form):
        post = form.save(commit=False)
        hash_password = make_pw_hash(form.cleaned_data.get('password'))
        post.password = hash_password
        post.save()
        messages.success(self.request, 'Staff added sucessfully.')
        return redirect('staffindex')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(StaffCreate, self).get_context_data(**kwargs)
        context['owners'] = OwnerProfile.objects.all().order_by('id').reverse()
        return context


# @method_decorator([login_required], name='dispatch')
# @method_decorator(staff_update_decorator, name='dispatch')
class StaffUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'staffprofile/create.html'
    model = StaffProfile
    form_class = StaffProfileForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('staffindex')
    queryset = StaffProfile.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        print('in get context data of staff Update:')
        context = super(StaffUpdate, self).get_context_data(**kwargs)
        context['owners'] = OwnerProfile.objects.all().order_by('id').reverse()
        return context


def staffResetPassword(request, id):
    user = User.objects.get(id=id)
    pwtoken = PasswordResetTokenGenerator().make_token(user)
    newuid = urlsafe_base64_encode(force_bytes(user.pk)).decode()
    return redirect('password_reset_confirm', uidb64=newuid, token=pwtoken)


def StaffActive(request, id, active):
    # print(active)
    # print('hello')
    if active == 'True':
        value = 0

    elif active == 'False':
        value = 1

    User.objects.filter(id=id).update(is_active=value)
    return redirect('staffindex')
