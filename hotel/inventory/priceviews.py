from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from hotel.b2b.models import B2B
from hotel.child_supplement_policy.forms import ChildSupplementPolicyForm
from hotel.child_supplement_policy.models import ChildSupplementPolicy
from hotel.inventory.models import HotelInventory
from hotel.models import Hotels
from hotel.priceOfRoom.models import PriceInDiffSys
from hotel.priceOfRoom.forms import PriceInDiffSysForm


@method_decorator([login_required], name='dispatch')
class PriceOfDiffSystemCreate(SuccessMessageMixin, CreateView):
    template_name = 'pricefordiffsys/create.html'
    model = PriceInDiffSys
    form_class = PriceInDiffSysForm
    success_message = 'Information Added Successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inv_id = self.kwargs['inv_id']
        hotel_id = HotelInventory.objects.get(id=inv_id).hotel_id
        adult_max = HotelInventory.objects.get(id=inv_id).adult_max
        context['inv_id'] = inv_id
        context['hotel_id'] = hotel_id
        context['adult_max'] = adult_max
        return context

    def get_success_url(self):
        inv_id = self.kwargs['inv_id']
        return reverse_lazy('hotel:showinvdetail', kwargs={'pk': inv_id})


@method_decorator([login_required], name='dispatch')
class PriceOfDiffSystemListView(SuccessMessageMixin, ListView):
    model = PriceInDiffSys
    template_name = 'pricefordiffsys/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PriceOfDiffSystemListView, self).get_context_data(**kwargs)
        inv_id = self.kwargs['inv_id']
        hotel_id = HotelInventory.objects.get(id=inv_id).hotel_id
        all_items = PriceInDiffSys.objects.filter(inventory_id=inv_id)
        context['all_items'] = all_items
        context['inv_id'] = inv_id
        context['hotel_id'] = hotel_id
        return context


@method_decorator([login_required], name='dispatch')
class PriceOfDiffSystemDelete(SuccessMessageMixin, DeleteView):
    model = PriceInDiffSys
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        item_id = self.object.id
        inv_id = PriceInDiffSys.objects.get(id=item_id).inventory_id
        return reverse_lazy('hotel:inventory-price-list', kwargs={'inv_id': inv_id})

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


@method_decorator([login_required], name='dispatch')
class PriceOfDiffSystemUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'pricefordiffsys/edit.html'
    model = PriceInDiffSys
    form_class = PriceInDiffSysForm
    success_message = 'Information Updated Successfully'
    queryset = PriceInDiffSys.objects.all()

    def form_valid(self, form):
        # self.hotel = form.data.get('hotel')
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print('form.data from form_invalid')
        print(form.data)
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(PriceOfDiffSystemUpdate, self).get_context_data(**kwargs)
        item_id = self.kwargs['pk']
        inv_id = PriceInDiffSys.objects.get(id=item_id).inventory_id
        hotel_id = HotelInventory.objects.get(id=inv_id).hotel_id
        context['inv_id'] = inv_id
        context['hotel_id'] = hotel_id
        return context


    def get_success_url(self):
        item_id = self.object.id
        inv_id = PriceInDiffSys.objects.get(id=item_id).inventory_id
        return reverse_lazy('hotel:inventory-price-list', kwargs={'inv_id': inv_id})
