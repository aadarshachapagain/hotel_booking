from django.shortcuts import render, redirect
from django.http import HttpResponse

from hotel.inventory.models import HotelInventory
from users.models import Users
from ..models import Hotels
from .models import HotelReview
from .forms import HotelReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


@method_decorator([login_required], name='dispatch')
class HotelReviewList(ListView):
    model = HotelReview
    template_name = 'HotelReview/index.html'

    def get_context_data(self, **kwargs):
        context = super(HotelReviewList, self).get_context_data(**kwargs)
        all_items = HotelReview.objects.all()
        for item in all_items:
            item.company_name = Hotels.objects.get(id=item.company_id)
            item.inventory_name = HotelInventory.objects.get(id=item.inventory_id)
        context['all_items'] = all_items
        # context['hotels'] = Hotels.objects.get(id=self.object['company_id'])
        return context


@method_decorator([login_required], name='dispatch')
class HotelReviewDetail(DetailView):
    model = HotelReview
    template_name = 'HotelReview/show.html'
    queryset = HotelReview.objects.all()

    def get_context_data(self, **kwargs):
        company_id = self.kwargs['pk']
        temp = HotelReview.objects.get(id=company_id)
        context = super(HotelReviewDetail, self).get_context_data(**kwargs)
        context['hotels'] = Hotels.objects.get(id=temp.company_id)
        context['inventory'] = HotelInventory.objects.get(id=temp.inventory_id)
        return context


@method_decorator([login_required], name='dispatch')
class HotelReviewCreate(SuccessMessageMixin, CreateView):
    template_name = 'HotelReview/create.html'
    model = HotelReview
    form_class = HotelReviewForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('hotel:HotelReview')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(HotelReviewCreate, self).get_context_data(**kwargs)
        context['users'] = Users.objects.all().order_by('id').reverse()
        context['hotels'] = Hotels.objects.all().order_by('id').reverse()
        return context


@method_decorator([login_required], name='dispatch')
class HotelReviewUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'HotelReview/create.html'
    model = HotelReview
    form_class = HotelReviewForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:HotelReview')
    queryset = HotelReview.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(HotelReviewUpdate, self).get_context_data(**kwargs)
        context['users'] = Users.objects.all().order_by('id').reverse()
        context['hotels'] = Hotels.objects.all().order_by('id').reverse()
        return context


@method_decorator([login_required], name='dispatch')
class HotelReviewDelete(SuccessMessageMixin, DeleteView):
    model = HotelReview
    pk_url_kwarg = 'HotelReview_id'
    success_url = reverse_lazy('hotel:HotelReview')

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)
