from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# from booking.customer.forms import CustomerForm
# from booking.customer.models import Customer
from booking.customer.models import Customer
from booking.guestdetail.forms import GuestDetailForm
from booking.guestdetail.models import GuestDetail
from booking.guestdocdetail.models import GuestDocDetail
from booking.guestdocdetail.forms import GuestDocDetailForm
from hotel.Country.models import Country


class GuestDocDetailCreate(SuccessMessageMixin, CreateView):
    template_name = 'guestdocdetail/create.html'
    model = GuestDocDetail
    form_class = GuestDocDetailForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('booking:guestdocdetailindex')

    # def get_success_url(self):
    #     item = self.object
    #     return reverse_lazy('rental:rentalcompanyaddressupdate', kwargs={'pk': item.id})

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.save()
        return super(GuestDocDetailCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(GuestDocDetailCreate, self).get_context_data(**kwargs)
        context['countries'] = Country.objects.all().order_by('id').reverse()
        context['customers'] = Customer.objects.all().order_by('id').reverse()
        context['guest_details'] = GuestDetail.objects.all().order_by('id').reverse()
        # context['landmarks'] = Landmark.objects.all().order_by('id').reverse()
        return context


class GuestDocDetailListView(ListView):
    model = GuestDocDetail
    template_name = 'guestdocdetail/index.html'
    context_object_name = 'all_docdetails'


class GuestDocDetailUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'guestdocdetail/create.html'
    model = GuestDocDetail
    form_class = GuestDocDetailForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('booking:guestdocdetailindex')
    queryset = GuestDocDetail.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))


    def get_context_data(self, **kwargs):
        context = super(GuestDocDetailUpdate, self).get_context_data(**kwargs)
        context['countries'] = Country.objects.all().order_by('id').reverse()
        context['guest_details'] = GuestDetail.objects.all().order_by('id').reverse()
        return context

class GuestDocDetailDelete(SuccessMessageMixin, DeleteView):
    model = GuestDocDetail
    success_url = reverse_lazy('booking:guestdocdetailindex')
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


