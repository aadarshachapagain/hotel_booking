from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from hotel.Country.models import Country
from .models import State
from .forms import StateForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# @method_decorator([login_required], name='dispatch')
class StateListView(ListView):
    model = State
    template_name = 'state/index.html'
    context_object_name = 'all_items'


# @method_decorator([login_required], name='dispatch')
class StateDelete(SuccessMessageMixin, DeleteView):
    model = State
    success_url = reverse_lazy('hotel:State')
    pk_url_kwarg = 'State_id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


# @method_decorator([login_required], name='dispatch')
class StateDetail(DetailView):
    model = State
    template_name = 'state/show.html'
    queryset = State.objects.all()


# @method_decorator([login_required], name='dispatch')
class StateCreate(SuccessMessageMixin, CreateView):
    template_name = 'state/create.html'
    model = State
    form_class = StateForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('hotel:State')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(StateCreate, self).get_context_data(**kwargs)
        context['country'] = Country.objects.all().order_by('id').reverse()
        return context
    
    def form_valid(self, form):
        form.save(commit=False)
        country = form.data.get('country')
        names = form.data.getlist('name')
        for index, name in enumerate(names):
            state = State()
            state.name = name
            state.country = Country.objects.get(id=country)
            state.save()
        return HttpResponseRedirect(self.success_url)

# @method_decorator([login_required], name='dispatch')
# @login_required
class StateUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'state/create.html'
    model = State
    form_class = StateForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:State')
    queryset = State.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(StateUpdate, self).get_context_data(**kwargs)
        context['country'] = Country.objects.all().order_by('id').reverse()

        return context
