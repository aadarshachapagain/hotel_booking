from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from ..owner.models import HotelOwner
from .models import HotelStaff
from .forms import HotelStaffForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from hashutils import make_pw_hash, check_pw_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from hotel.staff.decorators import staff_create_decorator
from hotel.staff.decorators import staff_update_decorator


@method_decorator([login_required], name='dispatch')
class StaffListView(ListView):
    model = HotelStaff
    template_name = 'staff/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        user = self.request.user
        # hotel_id = HotelOwner.objects.values_list('current_hotel', flat=True).get(user_id=user.id)
        if 'current_hotel' in self.request.COOKIES:
            current_hotel = self.request.COOKIES['current_hotel']
            hotel_id=current_hotel
        staff = HotelStaff.objects.filter(hotel=hotel_id)
        context = super(StaffListView, self).get_context_data(**kwargs)
        if staff:
            context['all_items'] = staff
            return context
        else:
            context['staff_list'] = 'No any staff has been registered.'
            return context


@method_decorator([login_required], name='dispatch')
@method_decorator(staff_update_decorator, name='dispatch')
class StaffDelete(SuccessMessageMixin, DeleteView):
    model = HotelStaff
    success_url = reverse_lazy('hotel:staffindex')

    # pk_url_kwarg='staff_id'
    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
# @method_decorator(staff_create_decorator,name='dispatch')
class StaffDetail(DetailView):
    model = HotelStaff
    template_name = 'staff/show.html'
    queryset = HotelStaff.objects.all()

    # def get_context_data(self, **kwargs):
    #         context = super(StaffListView, self).get_context_data(**kwargs)


@method_decorator([login_required], name='dispatch')
@method_decorator(staff_create_decorator, name='dispatch')
class StaffCreate(SuccessMessageMixin, CreateView):
    template_name = 'staff/create.html'
    model = HotelStaff
    form_class = HotelStaffForm
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
        context['owners'] = HotelOwner.objects.all().order_by('id').reverse()
        return context


@method_decorator([login_required], name='dispatch')
@method_decorator(staff_update_decorator, name='dispatch')
class StaffUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'staff/create.html'
    model = HotelStaff
    form_class = HotelStaffForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:staffindex')
    queryset = HotelStaff.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(StaffUpdate, self).get_context_data(**kwargs)
        context['owners'] = HotelOwner.objects.all().order_by('id').reverse()
        return context