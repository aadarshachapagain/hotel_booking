from points.point_setting.models import PointSetting
from points.point_setting.forms import PointSettingForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required], name='dispatch')
class PointSettingListView(ListView):
    model = PointSetting
    template_name = 'point_setting/index.html'
    context_object_name = 'all_items'


@method_decorator([login_required], name='dispatch')
class PointSettingDelete(SuccessMessageMixin, DeleteView):
    model = PointSetting
    success_url = reverse_lazy('points:point-setting-index')
    pk_url_kwarg = 'pointsetting_id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
# class CreditPointDetail(DetailView):
#     model = CreditPoint
#     template_name = 'credit_point/show.html'

    

@method_decorator([login_required], name='dispatch')
class PointSettingCreate(SuccessMessageMixin, CreateView):
    template_name = 'point_setting/create.html'
    model = PointSetting
    form_class = PointSettingForm
    success_message = 'Information Added Successfully'

    def get_success_url(self):
        return reverse_lazy('points:point-setting-index')

    def form_invalid(self, form):
        
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        credit = form.save(commit=False)
        credit.save()
        return super(PointSettingCreate, self).form_valid(form)


class PointSettingUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'point_setting/create.html'
    model = PointSetting
    form_class = PointSettingForm
    success_message = 'Information Updated Successfully'

    def form_valid(self, form):
        credit = form.save(commit=False)
        credit.is_active = False
        credit.save()
        return super(PointSettingUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(PointSettingUpdate, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('points:point-setting-index')
