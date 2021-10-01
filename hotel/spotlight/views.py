
from hotel.state.models import State
from ..models import Hotels

from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from hotel.city.models import City
from django.http import JsonResponse
from django.core import serializers
from hotel.spotlight.models import Spotlight
from hotel.spotlight.forms import SpotlightForm


def getstate(request):
    print('in getstate:')
    country_id = (request.GET['sendcountry'])
    states = State.objects.filter(country_id=country_id)
    state_serialized = serializers.serialize('json', states)
    return JsonResponse(state_serialized, safe=False)


def getcity(request):
    obtstate = (request.GET['sendstate'])

    cities = City.objects.filter(state_id=obtstate)
    # for c in cities:
    #     print(c)
    city_serialized = serializers.serialize('json', cities)
    return JsonResponse(city_serialized, safe=False)


@method_decorator([login_required], name='dispatch')
class SpotLightListView(ListView):
    model = Spotlight
    template_name = 'spotlight/index.html'
    context_object_name = 'all_items'



@method_decorator([login_required], name='dispatch')
class SpotLightDelete(SuccessMessageMixin, DeleteView):
    model = Spotlight
    success_url = reverse_lazy('hotel:spotlightindex')
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
class SpotLightCreate(SuccessMessageMixin, CreateView):
    template_name = 'spotlight/create.html'
    model = Spotlight
    form_class = SpotlightForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('hotel:spotlightindex')


    def get_context_data(self, **kwargs):
        context = super(SpotLightCreate, self).get_context_data(**kwargs)
        allhotels = Hotels.objects.all()
        context['hotels'] = allhotels
        return context

#
@method_decorator([login_required], name='dispatch')
class SpotLightUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'spotlight/create.html'
    model = Spotlight
    form_class = SpotlightForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:spotlightindex')
    queryset = Spotlight.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SpotLightUpdate, self).get_context_data(**kwargs)
        allhotels = Hotels.objects.all()
        context['hotels'] = allhotels
        return context

