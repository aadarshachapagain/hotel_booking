from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from booking.customer.forms import CustomerForm
from booking.customer.models import Customer
from hotel.Country.models import Country
from points.membership_plan.models import Membership_plan


class CustomerCreate(SuccessMessageMixin, CreateView):
    template_name = 'customer/create.html'
    model = Customer
    form_class = CustomerForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('booking:customerindex')

    # def get_success_url(self):
    #     item = self.object
    #     return reverse_lazy('rental:rentalcompanyaddressupdate', kwargs={'pk': item.id})

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.save()
        print('form data of customer:')
        print(form.data)
        return super(CustomerCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CustomerCreate, self).get_context_data(**kwargs)
        context['countries'] = Country.objects.all().order_by('id').reverse()
        context['memplans'] = Membership_plan.objects.all().order_by('id').reverse()

        # context['landmarks'] = Landmark.objects.all().order_by('id').reverse()
        return context


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/index.html'
    context_object_name = 'all_customers'


class CustomerUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'customer/create.html'
    model = Customer
    form_class = CustomerForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('booking:customerindex')
    queryset = Customer.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))


    def get_context_data(self, **kwargs):
        context = super(CustomerUpdate, self).get_context_data(**kwargs)
        context['countries'] = Country.objects.all().order_by('id').reverse()
        context['memplans'] = Membership_plan.objects.all().order_by('id').reverse()

        return context

class CustomerDelete(SuccessMessageMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('booking:customerindex')
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


