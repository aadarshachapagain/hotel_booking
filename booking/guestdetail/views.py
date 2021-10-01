from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# from booking.customer.forms import CustomerForm
# from booking.customer.models import Customer
from booking.customer.models import Customer
from booking.guestdetail.forms import GuestDetailForm
from booking.guestdetail.models import GuestDetail
from hotel.Country.models import Country


class GuestDetailCreate(SuccessMessageMixin, CreateView):
    template_name = 'guestdetail/create.html'
    model = GuestDetail
    form_class = GuestDetailForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('booking:guestdetailindex')

    # def get_success_url(self):
    #     item = self.object
    #     return reverse_lazy('rental:rentalcompanyaddressupdate', kwargs={'pk': item.id})

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.save()
        return super(GuestDetailCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(GuestDetailCreate, self).get_context_data(**kwargs)
        context['countries'] = Country.objects.all().order_by('id').reverse()
        context['customers'] = Customer.objects.all().order_by('id').reverse()
        # context['landmarks'] = Landmark.objects.all().order_by('id').reverse()
        return context


class GuestDetailListView(ListView):
    model = GuestDetail
    template_name = 'guestdetail/index.html'
    context_object_name = 'all_bookings'


class GuestDetailUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'guestdetail/create.html'
    model = GuestDetail
    form_class = GuestDetailForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('booking:guestdetailindex')
    queryset = GuestDetail.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))


    def get_context_data(self, **kwargs):
        context = super(GuestDetailUpdate, self).get_context_data(**kwargs)
        context['countries'] = Country.objects.all().order_by('id').reverse()
        context['customers'] = Customer.objects.all().order_by('id').reverse()
        return context

class GuestDetailDelete(SuccessMessageMixin, DeleteView):
    model = GuestDetail
    success_url = reverse_lazy('booking:guestdetailindex')
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


