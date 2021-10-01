from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from users.models import Users
from ..models import Hotels
from .models import HotelAmenities
from .forms import HotelAmenityForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


@method_decorator([login_required], name='dispatch')
class AmenitiesList(ListView):
    model = HotelAmenities
    template_name = 'amenities/index.html'
    context_object_name = 'hotelamenities'


@method_decorator([login_required], name='dispatch')
class AmenitiesDetail(DetailView):
    model = HotelAmenities
    template_name = 'amenities/show.html'
    queryset = HotelAmenities.objects.all()


@method_decorator([login_required], name='dispatch')
class AmenitiesCreate(SuccessMessageMixin, CreateView):
    template_name = 'amenities/create.html'
    model = HotelAmenities
    form_class = HotelAmenityForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('hotel:hotelamenities')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(AmenitiesCreate, self).get_context_data(**kwargs)
        context['users'] = Users.objects.all().order_by('id').reverse()
        return context
    
    def form_valid(self, form):
        form.save(commit=False)
        names = form.data.getlist('name')
        status = form.data.getlist('statusMy')
        if 'changed' in status:
            images = form.files.getlist('image')
        k = 0
        for index, name in enumerate(names):
            amenity_instance = HotelAmenities()
            amenity_instance.name = name
            amenity_instance.category = form.data.get('category')
            if status[index] == "unchanged":
                amenity_instance.image = None
            else:
                amenity_instance.image = images[k]
                k = k + 1

            amenity_instance.save()
        return HttpResponseRedirect(self.success_url)


@method_decorator([login_required], name='dispatch')
class AmenitiesUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'amenities/create.html'
    model = HotelAmenities
    form_class = HotelAmenityForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:hotelamenities')
    queryset = HotelAmenities.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(AmenitiesUpdate, self).get_context_data(**kwargs)
        context['users'] = Users.objects.all().order_by('id').reverse()
        return context
    
    def form_valid(self, form):
        amenity = form.save(commit=False)
        amenity.image = form.files.get('image')
        amenity.save()
        return HttpResponseRedirect(self.success_url)


@method_decorator([login_required], name='dispatch')
class AmenitiesDelete(SuccessMessageMixin, DeleteView):
    model = HotelAmenities
    pk_url_kwarg = 'amenities_id'
    success_url = reverse_lazy('hotel:hotelamenities')

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)

