from points.credit_point.models import CreditPoint
from points.credit_point.forms import CreditPointForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required], name='dispatch')
class CreditPointListView(ListView):
    model = CreditPoint
    template_name = 'credit_point/index.html'
    context_object_name = 'all_items'


@method_decorator([login_required], name='dispatch')
class CreditPointDelete(SuccessMessageMixin, DeleteView):
    model = CreditPoint
    success_url = reverse_lazy('points:credit-points-index')
    pk_url_kwarg = 'credit_id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
# class CreditPointDetail(DetailView):
#     model = CreditPoint
#     template_name = 'credit_point/show.html'

    

@method_decorator([login_required], name='dispatch')
class CreditPointCreate(SuccessMessageMixin, CreateView):
    template_name = 'credit_point/create.html'
    model = CreditPoint
    form_class = CreditPointForm
    success_message = 'Information Added Successfully'

    def get_success_url(self):
        return reverse_lazy('points:credit-points-index')

    def form_invalid(self, form):
        
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        credit = form.save(commit=False)
        credit.save()
        return super(CreditPointCreate, self).form_valid(form)


class CreditPointUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'credit_point/create.html'
    model = CreditPoint
    form_class = CreditPointForm
    success_message = 'Information Updated Successfully'

    def form_valid(self, form):
        credit = form.save(commit=False)
        credit.is_active = False
        credit.save()
        return super(CreditPointUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(CreditPointUpdate, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('points:credit-points-index')
