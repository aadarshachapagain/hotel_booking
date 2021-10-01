from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from booking.business_partners.forms import BusinessPartnersForm
from booking.business_partners.models import BusinessPartners


@method_decorator([login_required], name='dispatch')
class BusinessPartnersListView(ListView):
    model = BusinessPartners
    template_name = 'businessPartners/index.html'
    context_object_name = 'all_items'


@method_decorator([login_required], name='dispatch')
class BusinessPartnersDelete(SuccessMessageMixin, DeleteView):
    model = BusinessPartners
    success_url = reverse_lazy('booking:business-partners-index')
    pk_url_kwarg = 'partner_id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Business Partner Type Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
class BusinessPartnersDetail(DetailView):
    model = BusinessPartners
    template_name = 'businessPartners/show.html'
    queryset = BusinessPartners.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(BusinessPartnersDetail, self).get_context_data(**kwargs)
        return context

    

@method_decorator([login_required], name='dispatch')
class BusinessPartnersCreate(SuccessMessageMixin, CreateView):
    template_name = 'businessPartners/create.html'
    model = BusinessPartners
    form_class = BusinessPartnersForm
    success_message = 'New Business partner type added Successfully'

    def get_success_url(self):
        return reverse_lazy('booking:business-partners-index')

    def form_invalid(self, form):
        
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        credit = form.save(commit=False)
        credit.save()
        return super(BusinessPartnersCreate, self).form_valid(form)


class BusinessPartnersUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'businessPartners/create.html'
    model = BusinessPartners
    form_class = BusinessPartnersForm
    success_message = 'Business partner type updated Successfully'

    def form_valid(self, form):
        credit = form.save(commit=False)
        credit.is_active = False
        credit.save()
        return super(BusinessPartnersUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(BusinessPartnersUpdate, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('booking:business-partners-index')
