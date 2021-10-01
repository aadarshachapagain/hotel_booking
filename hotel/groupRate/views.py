from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from hotel.models import Hotels
from hotel.groupRate.models import GroupRate
from hotel.groupRate.forms import GroupRateForm


@method_decorator([login_required], name='dispatch')
class GroupRateCreate(SuccessMessageMixin, CreateView):
    template_name = 'GroupRate/edit.html'
    model = GroupRate
    form_class = GroupRateForm
    success_message = 'Information Added Successfully'

    def form_valid(self, form):
        form.save(commit=False)
        hotel = form.data.get('hotel')
        range_start = form.data.getlist('range_start')
        range_end = form.data.getlist('range_end')
        map_cost = form.data.getlist('map_cost')
        ap_cost = form.data.getlist('ap_cost')
        for index, age_cat in enumerate(range_start):
            instance = GroupRate()
            instance.hotel = Hotels.objects.get(pk=hotel)
            instance.range_start = range_start[index]
            instance.range_end = range_end[index]
            instance.map_cost = map_cost[index] or 0.0
            instance.ap_cost = ap_cost[index] or 0.0
            instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        print(form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        hotel_id = self.kwargs.get('hotel_id')
        context = super(GroupRateCreate, self).get_context_data(**kwargs)
        context['hotel_id'] = hotel_id
        return context

    def get_success_url(self):
        return reverse_lazy('hotel:GroupRate', kwargs={'item_id': self.kwargs.get('hotel_id')})

    # def get_form_kwargs(self):
    #     kwargs = super(GroupRateCreate, self).get_form_kwargs()
    #     hotel_id = self.kwargs.get('item_id')
    #     kwargs['hotel'] = hotel_id
    #     return kwargs


class GroupRateListView(ListView):
    model = GroupRate
    template_name = 'GroupRate/index.html'
    context_object_name = 'all_items'

    def get_context_data(self, **kwargs):
        context = super(GroupRateListView, self).get_context_data(**kwargs)
        hotel_id = self.kwargs.get('item_id')
        all_items = GroupRate.objects.filter(hotel=hotel_id)
        context.update({'hotel_id': hotel_id})
        context.update({'all_items': all_items})
        return context


@method_decorator([login_required], name='dispatch')
class GroupRateUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'GroupRate/edit.html'
    model = GroupRate
    form_class = GroupRateForm
    success_message = 'Information Updated Successfully'
    queryset = GroupRate.objects.all()

    def form_valid(self, form):
        self.hotel = form.data.get('hotel')
        form.save(commit=False)
        data = form.cleaned_data
        hotel = data.get('hotel')
        instance = GroupRate.objects.get(pk=self.kwargs['pk'])
        instance.hotel = Hotels.objects.get(pk=hotel.id)
        instance.range_start = data.get('range_start')
        instance.range_end = data.get('range_end')
        instance.map_cost = data.get('map_cost') or 0.0
        instance.ap_cost = data.get('ap_cost') or 0.0
        instance.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        hotel_id = GroupRate.objects.get(id=pk).hotel.id
        context = super(GroupRateUpdate, self).get_context_data(**kwargs)
        context['hotel_id'] = hotel_id
        return context

    def get_success_url(self):
        hotel_id = self.hotel
        return reverse_lazy('hotel:GroupRate', kwargs={'item_id': hotel_id})


@method_decorator([login_required], name='dispatch')
class GroupRateDelete(SuccessMessageMixin, DeleteView):
    model = GroupRate

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted.")
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        item_id = self.object.id
        hotel_id = GroupRate.objects.get(id=item_id).hotel_id
        return reverse_lazy('hotel:GroupRate', kwargs={'item_id': hotel_id})

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
