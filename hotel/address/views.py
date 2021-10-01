from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from hotel.Country.models import Country
from hotel.gallery.models import HotelGallery
from hotel.state.models import State
from ..models import Hotels
from .models import HotelAddress
from .forms import HotelAddressForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from hotel.landmark.models import Landmark
from hotel.city.models import City
import geopy.distance
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers


def getstate(request):
    country_id = (request.GET['sendcountry'])
    states = State.objects.filter(country_id=country_id)
    state_serialized = serializers.serialize('json', states)
    return JsonResponse(state_serialized, safe=False)


def getcity(request):
    obtstate = (request.GET['sendstate'])
    cities = City.objects.filter(state_id=obtstate)
    city_serialized = serializers.serialize('json', cities)
    return JsonResponse(city_serialized, safe=False)


def getCountryPhone(request):
    country_id = (request.GET['sendcountry'])
    code = Country.objects.filter(id=country_id)
    code_serialized = serializers.serialize('json', code)
    print("serializer")
    print(code_serialized)
    return JsonResponse(code_serialized, safe=False)


# def getDistance(request):
#     objs = HotelAddress.objects.all()
#     # for obj in objs:
#     print(objs[0].city)
#     # For test purpose
#     city = objs[0].city
#     query_lat = objs.values_list('latitude', flat=True).get(city=city)
#     query_long = objs.values_list('longitude', flat=True).get(city=city)
#     query_xy = (query_lat, query_long)
#     print('query xy')
#     print(query_xy)
#     print(query_lat)
#     print(query_long)
#     for obj in objs:
#         print(obj.latitude)
#         obj_xy = (obj.latitude, obj.longitude)
#         print(obj_xy)
#         distance12 = geopy.distance.vincenty(query_xy, obj_xy).km
#         print('distance:')
#         print(distance12)
#
#     # print(city+':'+lat)
#     # p1 = (28.704060,77.102493)
#     # p2 = (27.717245,85.323959)
#     # distance = p1.distance(p2)
#     # distance_in_km = distance * 100
#     # distance = geopy.distance.vincenty(p1, p2).km
#     return HttpResponse(distance12)


@method_decorator([login_required], name='dispatch')
class AddressListView(ListView):
    model = HotelAddress
    template_name = 'address/index.html'
    context_object_name = 'all_items'


@method_decorator([login_required], name='dispatch')
class AddressDelete(SuccessMessageMixin, DeleteView):
    model = HotelAddress
    success_url = reverse_lazy('hotel:addressindex')
    pk_url_kwarg = 'address_id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
class AddressDetail(DetailView):
    model = HotelAddress
    template_name = 'address/show.html'
    queryset = HotelAddress.objects.all()


@method_decorator([login_required], name='dispatch')
class AddressCreate(SuccessMessageMixin, CreateView):
    template_name = 'address/create.html'
    model = HotelAddress
    form_class = HotelAddressForm
    success_message = 'Information Added Successfully'

    # success_url = reverse_lazy('hotel:hotelgallery-create')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        inv = form.save(commit=False)
        inv.save()
        landmarks = form.data.getlist('landmarks')

        for landmark in landmarks:
            inv.landmarks.add(landmark)
        return super(AddressCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddressCreate, self).get_context_data(**kwargs)
        item_id = self.kwargs['item_id']
        # context['hotels'] = Hotels.objects.all().order_by('id').reverse()
        context['hotels'] = item_id
        context['cities'] = City.objects.all().order_by('id').reverse()
        context['landmarks'] = Landmark.objects.all().order_by('id').reverse()
        return context

    def get_success_url(self):
        item = self.object
        print(item.hotel_id)
        # return HttpResponse('itemgaako xa')
        return reverse_lazy('hotel:hotelgallery-create', kwargs={'item_id': item.hotel_id})


@method_decorator([login_required], name='dispatch')
class AddressUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'address/create.html'
    model = HotelAddress
    form_class = HotelAddressForm
    success_message = 'Information Updated Successfully'
    # success_url = reverse_lazy('hotel:addressindex')
    queryset = HotelAddress.objects.all()

    def get_success_url(self):
        item = self.object
        if self.form.data['register'] == 'Save and Exit':
            url = reverse_lazy('hotel:hotelindex', kwargs={'hotel_id': item.hotel_id})
        else:
            url = reverse_lazy('hotel:hotelfacilities-newcreate', kwargs={'hotel_id': item.hotel_id})
        return url

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        self.form = form
        inv = form.save(commit=False)
        inv.save()
        landmarks = form.data.getlist('landmarks')
        item = self.object
        item_id = item.hotel_id
        inv.landmarks.through.objects.filter(hoteladdress_id=item_id).delete()
        for landmark in landmarks:
            inv.landmarks.add(landmark)
        return super(AddressUpdate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddressUpdate, self).get_context_data(**kwargs)
        item_id = self.kwargs['pk']
        gallery = HotelGallery.objects.filter(hotel_id=item_id).count()
        if gallery <= 0:
            status_value = 'go'
        else:
            status_value = 'no'
        context['status'] = status_value
        context['hotels'] = item_id
        context['cities'] = City.objects.all().order_by('id').reverse()
        landmark_list = Landmark.objects.exclude(hotellandmarks=item_id)
        selectedlist = Landmark.objects.filter(hotellandmarks=item_id)
        context['countries'] = Country.objects.all().reverse()
        context['selectedcountries'] = HotelAddress.objects.get(hotel_id=item_id).country
        context['states'] = State.objects.all().reverse()
        context['landmarks'] = landmark_list
        context['selectedlist'] = selectedlist
        return context


def addlandmark(request, address_id):
    if request.method == 'POST':
        landmarks = dict(request.POST)["landmarklist[]"]
        address_instance = HotelAddress.objects.get(hotel_id=address_id)
        new_landmark_instance = Landmark()
        new_landmark_instance.name = request.POST['landmarkname']
        new_landmark_instance.latitude = request.POST['lat_landmark']
        new_landmark_instance.longitude = request.POST['lng_landmark']
        new_landmark_instance.save()
        address_instance.landmarks.add(new_landmark_instance)
        landmarklist = []

        # for landmark in landmarks:
        #     l = Landmark()
        #     l.name = landmark
        #     l.save()
        #     address_instance.landmarks.add(l)

        addedlandmarks = HotelAddress.objects.get(hotel_id=address_id).landmarks.filter()

        for adl in addedlandmarks:
            dict_landmark = model_to_dict(adl)
            landmarklist.append(dict_landmark)
        return JsonResponse(landmarklist, safe=False)
    # return HttpResponse("I am ready for ajax call")


def map(request):
    return render(request, 'address/map.html')
