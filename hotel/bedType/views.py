from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from hotel.bedType.models import BedType
from .forms import BedTypeForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required], name='dispatch')
class BedTypeListView(ListView):
    model = BedType
    template_name = 'bedType/index.html'
    context_object_name = 'all_items'


@method_decorator([login_required], name='dispatch')
class BedTypeDelete(SuccessMessageMixin, DeleteView):
    model = BedType
    success_url = reverse_lazy('hotel:bed-type')
    pk_url_kwarg = 'bed_id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)

@method_decorator([login_required], name='dispatch')
class BedTypeDetail(DetailView):
    model = BedType
    template_name = 'bedType/show.html'
    queryset = BedType.objects.all()

@method_decorator([login_required], name='dispatch')
class BedTypeCreate(SuccessMessageMixin, CreateView):
    template_name = 'bedType/create.html'
    model = BedType
    form_class = BedTypeForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('hotel:bed-type')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(BedTypeCreate, self).get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        form.save(commit=False)
        names = form.data.getlist('name')
        descriptions = form.data.getlist('description')
        for index, name in enumerate(names):
            bed = BedType()
            bed.name = name
            bed.description = descriptions[index]
            bed.save()
        return HttpResponseRedirect(self.success_url)

@method_decorator([login_required], name='dispatch')
class BedTypeUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'bedType/create.html'
    model = BedType
    form_class = BedTypeForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:bed-type')
    queryset = BedType.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(BedTypeUpdate, self).get_context_data(**kwargs)
        return context
