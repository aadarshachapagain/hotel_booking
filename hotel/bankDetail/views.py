from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from account.Language.models import Language
from account.Language.forms import LanguageForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from hotel.Country.models import Country
from hotel.bankDetail.forms import BankDetailForm
from hotel.bankDetail.models import BankDetail
from hotel.models import Hotels


class BankDetailListView(ListView):
    model = BankDetail
    template_name = 'bankDetail/index.html'
    context_object_name = 'all_items'

    def get_context_data(self, **kwargs):
        hotel_id = self.kwargs['hotel_id']
        context = super(BankDetailListView, self).get_context_data(**kwargs)
        all_items = self.model.objects.filter(hotel=hotel_id)
        context['all_items'] = all_items
        context['hotel_id'] = hotel_id
        return context


# @method_decorator([login_required], name='dispatch')
class BankDetailDelete(SuccessMessageMixin, DeleteView):
    model = BankDetail
    pk_url_kwarg = 'detail_id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        item = self.object
        return reverse_lazy('hotel:bank-detail', kwargs={'hotel_id': item.hotel.id})


# @method_decorator([login_required], name='dispatch')
# class BankDetailDetail(DetailView):
# 	model = BankDetail
# 	template_name = 'bankDetail/show.html'
# 	queryset = Language.objects.all()


# @method_decorator([login_required], name='dispatch')
class BankDetailCreate(SuccessMessageMixin, CreateView):
    template_name = 'bankDetail/create.html'
    model = BankDetail
    form_class = BankDetailForm
    success_message = 'Information Added Successfully'

    def form_valid(self, form):
        self.form = form
        bankDetail = form.save(commit=False)
        bankDetail.hotel = Hotels.objects.get(id=form.data.get('hotel'))
        bankDetail.save()
        return super(BankDetailCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        hotel_id = self.kwargs['hotel_id']
        form.hotel = hotel_id
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(BankDetailCreate, self).get_context_data(**kwargs)
        hotel_id = self.kwargs['hotel_id']
        context['hotel_id'] = hotel_id
        context['countries'] = Country.objects.all().reverse()
        return context

    def get_success_url(self):
        item = self.object
        if self.form.data['register'] == 'Save and Exit':
            url = reverse_lazy('hotel:hotelindex', kwargs={'hotel_id': item.hotel.id})
        else:
            url = reverse_lazy('hotel:hotelgallery-create', kwargs={'item_id': item.hotel.id})
        return url


# @method_decorator([login_required], name='dispatch')
# @login_required
class BankDetailUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'bankDetail/create.html'
    model = BankDetail
    form_class = BankDetailForm
    success_message = 'Information Updated Successfully'
    queryset = BankDetail.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(BankDetailUpdate, self).get_context_data(**kwargs)
        context['countries'] = Country.objects.all().reverse()
        return context

    def get_success_url(self):
        item = self.object
        return reverse_lazy('hotel:bank-detail', kwargs={'hotel_id': item.hotel.id})
