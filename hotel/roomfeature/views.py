from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from hotel.roomfeature.forms import HotelRoomFeatureForm
from hotel.roomfeature.models import HotelRoomFeature
from django.contrib import messages


@method_decorator([login_required], name='dispatch')
class RoomFeatureList(ListView):
    model = HotelRoomFeature
    template_name = 'hotelroomfeature/index.html'
    context_object_name = 'hotelroomfeatures'


@method_decorator([login_required], name='dispatch')
class RoomFeatureDetail(DetailView):
    model = HotelRoomFeature
    template_name = 'hotelroomfeature/show.html'
    queryset = HotelRoomFeature.objects.all()


@method_decorator([login_required], name='dispatch')
class HotelRoomFeaturesDelete(SuccessMessageMixin, DeleteView):
    model = HotelRoomFeature
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('hotel:hotelroomfeatures')

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
class FeaturesCreate(SuccessMessageMixin, CreateView):
    template_name = 'hotelroomfeature/create.html'
    model = HotelRoomFeature
    form_class = HotelRoomFeatureForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('hotel:hotelroomfeatures')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(FeaturesCreate, self).get_context_data(**kwargs)
        # context['users'] = Users.objects.all().order_by('id').reverse()
        return context

    def form_valid(self, form):
        form.save(commit=False)
        names = form.data.getlist('name')
        for name in names:
            facility = HotelRoomFeature()
            facility.name = name
            facility.save()
        return HttpResponseRedirect(self.success_url)

@method_decorator([login_required], name='dispatch')
class HotelRoomFeatureUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'hotelroomfeature/create.html'
    model = HotelRoomFeature
    form_class = HotelRoomFeatureForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:hotelroomfeatures')
    queryset = HotelRoomFeature.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(HotelRoomFeatureUpdate, self).get_context_data(**kwargs)
        # context['users'] = Users.objects.all().order_by('id').reverse()
        return context



