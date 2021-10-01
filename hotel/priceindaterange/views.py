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
from hotel.inventoryUpdate.models import InventoryUpdate
from hotel.inventoryUpdate.forms import InventoryUpdateForm


@method_decorator([login_required], name='dispatch')
class PriceinDateRangeCreate(SuccessMessageMixin, CreateView):
    template_name = 'priceindaterange/create.html'
    model = InventoryUpdate
    form_class = InventoryUpdateForm
    success_message = 'Information Added Successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inv_id = self.kwargs['inv_id']
        hotel_id = HotelInventory.objects.get(id=inv_id).hotel_id
        context['inv_id'] = inv_id
        context['hotel_id'] = hotel_id
        # hotel_id = HotelInventory.objects.get(id=inv_id).hotel_id
        hotel = Hotels.objects.get(id=hotel_id)
        inv = HotelInventory.objects.get(id=inv_id)
        context['hotel'] = hotel
        context['inv'] = inv
        return context



    def get_success_url(self):
        inv_id = self.kwargs['inv_id']
        return reverse_lazy('hotel:inventory-priceindaterange-list', kwargs={'inv_id': inv_id})
        # return reverse_lazy('hotel:showinvdetail', kwargs={'pk': inv_id})


@method_decorator([login_required], name='dispatch')
class PriceinDateRangeListView(SuccessMessageMixin, ListView):
    model = InventoryUpdate
    template_name = 'priceindaterange/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PriceinDateRangeListView, self).get_context_data(**kwargs)
        inv_id = self.kwargs['inv_id']
        hotel_id = HotelInventory.objects.get(id=inv_id).hotel_id
        all_items = InventoryUpdate.objects.filter(inventory_id=inv_id)
        context['all_items'] = all_items
        context['inv_id'] = inv_id
        context['hotel_id'] = hotel_id
        return context


@method_decorator([login_required], name='dispatch')
class PriceinDateRangeDelete(SuccessMessageMixin, DeleteView):
    model = InventoryUpdate
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        item_id = self.object.id
        inv_id = InventoryUpdate.objects.get(id=item_id).inventory.id
        return reverse_lazy('hotel:inventory-priceindaterange-list', kwargs={'inv_id': inv_id})

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


# @method_decorator([login_required], name='dispatch')
# class PriceinDateRangeUpdate(SuccessMessageMixin, UpdateView):
#     template_name = 'priceindaterange/create.html'
#     model = InventoryUpdate
#     form_class = InventoryUpdateForm
#     success_message = 'Information Updated Successfully'
#     queryset = InventoryUpdate.objects.all()
#
#     def form_valid(self, form):
#         print('form_data')
#         print(form.data)
#         # self.hotel = form.data.get('hotel')
#         form.save()
#         return HttpResponseRedirect(self.get_success_url())
#
#     def form_invalid(self, form):
#         print('form.data from form_invalid')
#         print(form.data)
#         messages.warning(self.request, form.errors)
#         return self.render_to_response(self.get_context_data(object=form.data))
#
#     def get_context_data(self, **kwargs):
#         context = super(PriceinDateRangeUpdate, self).get_context_data(**kwargs)
#         item_id = self.kwargs['pk']
#         inv_id = InventoryUpdate.objects.get(id=item_id).inventory.id
#         hotel_id = HotelInventory.objects.get(id=inv_id).hotel_id
#         inv = HotelInventory.objects.get(id=inv_id)
#         hotel = Hotels.objects.get(id=hotel_id)
#         context['inv'] = inv
#         context['hotel'] = hotel
#         # inv_id = InventoryUpdate.objects.get(id=item_id).inventory.id
#         # hotel_id = HotelInventory.objects.get(id=inv_id).hotel_id
#         # context['inv_id'] = inv_id
#         # context['hotel_id'] = hotel_id
#         return context
#
#     def get_success_url(self):
#         item_id = self.object.id
#         inv_id = InventoryUpdate.objects.get(id=item_id).inventory.id
#         return reverse_lazy('hotel:inventory-priceindaterange-list', kwargs={'inv_id': inv_id})


@method_decorator([login_required], name='dispatch')
class PriceinDateRangeUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'priceindaterange/create.html'
    model = InventoryUpdate
    form_class = InventoryUpdateForm
    success_message = 'Information Updated Successfully'
    queryset = InventoryUpdate.objects.all()

    def form_valid(self, form):
        print('from form_valid')
        print(form.data)
        # self.hotel = form.data.get('hotel')
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print('form.data from form_invalid')
        print(form.data)
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(PriceinDateRangeUpdate, self).get_context_data(**kwargs)
        item_id = self.kwargs['pk']
        print('item_id')
        print(item_id)
        inv_id = InventoryUpdate.objects.get(id=item_id).inventory.id
        hotel_id = HotelInventory.objects.get(id=inv_id).hotel_id
        hotel = Hotels.objects.get(id=hotel_id)
        context['inv_id'] = inv_id
        context['hotel_id'] = hotel_id
        context['hotel'] = hotel
        return context

    def get_success_url(self):
        item_id = self.object.id
        inv_id = InventoryUpdate.objects.get(id=item_id).inventory.id
        return reverse_lazy('hotel:inventory-priceindaterange-list', kwargs={'inv_id': inv_id})
