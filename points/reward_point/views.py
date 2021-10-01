from points.reward_point.models import RewardPoint
from points.reward_point.forms import RewardPointForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required], name='dispatch')
class RewardPointListView(ListView):
    model = RewardPoint
    template_name = 'reward_point/index.html'
    context_object_name = 'all_items'


@method_decorator([login_required], name='dispatch')
class RewardPointDelete(SuccessMessageMixin, DeleteView):
    model = RewardPoint
    success_url = reverse_lazy('points:reward-points-index')
    pk_url_kwarg = 'reward_id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
# class RewardPointDetail(DetailView):
#     model = RewardPoint
#     template_name = 'reward_point/show.html'



@method_decorator([login_required], name='dispatch')
class RewardPointCreate(SuccessMessageMixin, CreateView):
    template_name = 'reward_point/create.html'
    model = RewardPoint
    form_class = RewardPointForm
    success_message = 'Information Added Successfully'
    # success_url = reverse_lazy('travel_tour:tourcompanyaddresscreate', kwargs={'item_id': item.company_id})

    def get_success_url(self):
        item = self.object
        return reverse_lazy('points:reward-points-index')

    def form_invalid(self, form):
        
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        reward = form.save(commit=False)
        reward.save()
        return super(RewardPointCreate, self).form_valid(form)


class RewardPointUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'reward_point/create.html'
    model = RewardPoint
    form_class = RewardPointForm
    success_message = 'Information Updated Successfully'

    # success_url = reverse_lazy('travel_tour:tourcompanyindex')
    def form_valid(self, form):
        tour = form.save(commit=False)
        tour.is_active = False
        tour.save()
        return super(RewardPointUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(RewardPointUpdate, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        item = self.object
        # print(item)
        return reverse_lazy('points:reward-points-index')
