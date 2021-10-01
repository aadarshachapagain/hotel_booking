from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from hotel.state.models import State
from hotel.Country.models import Country
from .models import City
from .forms import CityForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.core import serializers


# @method_decorator([login_required], name='dispatch')
class CityListView(ListView):
    model = City
    template_name = 'city/index.html'
    context_object_name = 'all_items'


# @method_decorator([login_required], name='dispatch')
class CityDelete(SuccessMessageMixin, DeleteView):
    model = City
    success_url = reverse_lazy('hotel:city')
    pk_url_kwarg = 'city_id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


# @method_decorator([login_required], name='dispatch')
class CityDetail(DetailView):
    model = City
    template_name = 'city/show.html'
    queryset = City.objects.all()


# @method_decorator([login_required], name='dispatch')
class CityCreate(SuccessMessageMixin, CreateView):
    template_name = 'city/create.html'
    model = City
    form_class = CityForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('hotel:city')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(CityCreate, self).get_context_data(**kwargs)
        context['state'] = State.objects.all().order_by('id').reverse()
        context['countries'] = Country.objects.all()
        return context

    def form_valid(self, form):
        form.save(commit=False)
        country = form.data.get('country')
        print(country)
        state = form.data.get('state')
        names = form.data.getlist('name')
        img = self.request.FILES.getlist('image')
        for index, name in enumerate(names):
            city = City()
            city.name = name
            city.image = img[index]
            city.country = Country.objects.get(id=country)
            city.state = State.objects.get(id=state)
            city.save()
        return HttpResponseRedirect(self.success_url)

# @method_decorator([login_required], name='dispatch')
# @login_required
class CityUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'city/create.html'
    model = City
    form_class = CityForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:city')
    queryset = City.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(CityUpdate, self).get_context_data(**kwargs)
        state = City.objects.get(id=self.object.id).state
        context['state'] = state
        context['countries'] = Country.objects.all()
        return context

#
# def getstate(request):
#     print('in getstate: from city create:')
#     country_id = (request.GET['sendcountry'])
#     states = State.objects.filter(country_id=country_id)
#     state_serialized = serializers.serialize('json', states)
#     return JsonResponse(state_serialized, safe=False)
