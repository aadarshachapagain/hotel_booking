from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import CreditCard
from .forms import CreditCardForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# @method_decorator([login_required], name='dispatch')
class CreditCardListView(ListView):
    model = CreditCard
    template_name = 'CreditCard/index.html'
    context_object_name = 'all_items'


# @method_decorator([login_required], name='dispatch')
class CreditCardDelete(SuccessMessageMixin, DeleteView):
    model = CreditCard
    success_url = reverse_lazy('hotel:credit-card')

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


# @method_decorator([login_required], name='dispatch')
class CreditCardDetail(DetailView):
    model = CreditCard
    template_name = 'CreditCard/show.html'
    queryset = CreditCard.objects.all()


# @method_decorator([login_required], name='dispatch')
class CreditCardCreate(SuccessMessageMixin, CreateView):
    template_name = 'CreditCard/create.html'
    model = CreditCard
    form_class = CreditCardForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('hotel:credit-card')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(CreditCardCreate, self).get_context_data(**kwargs)
        return context
    
    def form_valid(self, form):
        form.save(commit=False)
        names = form.data.getlist('name')
        for name in names:
            card_instance = CreditCard()
            card_instance.name = name
            card_instance.save()
        return HttpResponseRedirect(self.success_url)


# @method_decorator([login_required], name='dispatch')
# @login_required
class CreditCardUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'CreditCard/create.html'
    model = CreditCard
    form_class = CreditCardForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:credit-card')
    queryset = CreditCard.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(CreditCardUpdate, self).get_context_data(**kwargs)
        return context
