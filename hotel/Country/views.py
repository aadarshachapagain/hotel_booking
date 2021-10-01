from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import Country
from .forms import CountryForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# @method_decorator([login_required], name='dispatch')
class CountryListView(ListView):
    model = Country
    template_name = 'country/index.html'
    context_object_name = 'all_items'


# @method_decorator([login_required], name='dispatch')
class CountryDelete(SuccessMessageMixin, DeleteView):
    model = Country
    success_url = reverse_lazy('hotel:country')
    pk_url_kwarg = 'country_id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


# @method_decorator([login_required], name='dispatch')
class CountryDetail(DetailView):
    model = Country
    template_name = 'country/show.html'
    queryset = Country.objects.all()


# @method_decorator([login_required], name='dispatch')
class CountryCreate(SuccessMessageMixin, CreateView):
    template_name = 'country/create.html'
    model = Country
    form_class = CountryForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('hotel:country')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(CountryCreate, self).get_context_data(**kwargs)
        return context


# @method_decorator([login_required], name='dispatch')
# @login_required
class CountryUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'country/create.html'
    model = Country
    form_class = CountryForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:country')
    queryset = Country.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(CountryUpdate, self).get_context_data(**kwargs)
        return context
