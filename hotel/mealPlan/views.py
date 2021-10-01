from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from hotel.mealPlan.models import MealPlan
from hotel.mealPlan.forms import MealPlanForm


class MealPlanListView(ListView):
    model = MealPlan
    template_name = 'mealplan/index.html'
    context_object_name = 'all_items'


@method_decorator([login_required], name='dispatch')
class MealPlanDelete(SuccessMessageMixin, DeleteView):
    model = MealPlan
    pk_url_kwarg = 'detail_id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        item = self.object
        return reverse_lazy('hotel:MealPlan')



@method_decorator([login_required], name='dispatch')
class MealPlanCreate(SuccessMessageMixin, CreateView):
    template_name = 'mealplan/create.html'
    model = MealPlan
    form_class = MealPlanForm
    success_message = 'Information Added Successfully'

    def form_valid(self, form):
        return super(MealPlanCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    # def get_context_data(self, **kwargs):
    #     context = super(ChargesCreate, self).get_context_data(**kwargs)
    #     return context

    def get_success_url(self):
        return reverse_lazy('hotel:MealPlan')


@method_decorator([login_required], name='dispatch')
class MealPlanUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'mealplan/create.html'
    model = MealPlan
    form_class = MealPlanForm
    success_message = 'Information Updated Successfully'
    queryset = MealPlan.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(MealPlanUpdate, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('hotel:MealPlan')
