from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from hotel.city.models import City
from .models import Landmark
from .forms import LandmarkForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# @method_decorator([login_required], name='dispatch')
class LandmarkListView(ListView):
    model = Landmark
    template_name = 'Landmark/index.html'
    context_object_name = 'all_items'


# @method_decorator([login_required], name='dispatch')
class LandmarkDelete(SuccessMessageMixin, DeleteView):
    model = Landmark
    success_url = reverse_lazy('hotel:landmark')

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


# @method_decorator([login_required], name='dispatch')
class LandmarkDetail(DetailView):
    model = Landmark
    template_name = 'Landmark/show.html'
    queryset = Landmark.objects.all()


# @method_decorator([login_required], name='dispatch')
class LandmarkCreate(SuccessMessageMixin, CreateView):
    template_name = 'Landmark/create.html'
    model = Landmark
    form_class = LandmarkForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('hotel:landmark')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(LandmarkCreate, self).get_context_data(**kwargs)
        # context['city'] = City.objects.all().order_by('id').reverse()
        return context
    
    def form_valid(self, form):
        form.save(commit=False)
        names = form.data.getlist('name')
        for index, name in enumerate(names):
            landmark = Landmark()
            landmark.name = name
            landmark.save()
        return HttpResponseRedirect(self.success_url)


# @method_decorator([login_required], name='dispatch')
# @login_required
class LandmarkUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'Landmark/create.html'
    model = Landmark
    form_class = LandmarkForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:landmark')
    queryset = Landmark.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(LandmarkUpdate, self).get_context_data(**kwargs)
        # context['city'] = City.objects.all().order_by('id').reverse()
        return context
