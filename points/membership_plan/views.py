from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

# from booking.customer.forms import CustomerForm
from points.membership_plan.forms import Membership_planForm
from points.membership_plan.models import Membership_plan

# from booking.customer.models import Customer
from hotel.Country.models import Country


class Membership_planCreate(SuccessMessageMixin, CreateView):
    template_name = 'membership_plan/create.html'
    model = Membership_plan
    form_class = Membership_planForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('points:memplanindex')

    # def get_success_url(self):
    #     item = self.object
    #     return reverse_lazy('rental:rentalcompanyaddressupdate', kwargs={'pk': item.id})

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        plan = form.save(commit=False)
        plan.save()
        return super(Membership_planCreate, self).form_valid(form)



class Membership_planListView(ListView):
    model = Membership_plan
    template_name = 'membership_plan/index.html'
    context_object_name = 'all_memberships'


class Membership_planUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'membership_plan/create.html'
    model = Membership_plan
    form_class = Membership_planForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('points:memplanindex')
    queryset = Membership_plan.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))



class Membership_planDelete(SuccessMessageMixin, DeleteView):
    model = Membership_plan
    success_url = reverse_lazy('points:memplanindex')
    pk_url_kwarg = 'pk'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)
