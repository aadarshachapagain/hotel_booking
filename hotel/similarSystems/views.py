import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from hotel.similarSystems.models import SimilarSystems
from hotel.similarSystems.forms import SimilarSystemsForm


class SimilarSystemsListView(ListView):
    model = SimilarSystems
    template_name = 'similarsystems/index.html'
    context_object_name = 'all_items'


@method_decorator([login_required], name='dispatch')
class SimilarSystemsDelete(SuccessMessageMixin, DeleteView):
    model = SimilarSystems
    pk_url_kwarg = 'detail_id'

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        item = self.object
        return reverse_lazy('hotel:SimilarSystems')


@method_decorator([login_required], name='dispatch')
class SimilarSystemsCreate(SuccessMessageMixin, CreateView):
    template_name = 'similarsystems/create.html'
    model = SimilarSystems
    form_class = SimilarSystemsForm
    success_message = 'Information Added Successfully'

    def form_valid(self, form):
        return super(SimilarSystemsCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(SimilarSystemsCreate, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('hotel:SimilarSystems')


@method_decorator([login_required], name='dispatch')
class SimilarSystemsUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'similarsystems/create.html'
    model = SimilarSystems
    form_class = SimilarSystemsForm
    success_message = 'Information Updated Successfully'
    queryset = SimilarSystems.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(SimilarSystemsUpdate, self).get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('hotel:SimilarSystems')


def byvendor(request):
    if request.method == "POST":
        similarsys = request.POST['similarsys']
        if similarsys:
            obj = SimilarSystems()
            obj.name = similarsys
            obj.status = True
            obj.save()
            sys = SimilarSystems.objects.get(id=obj.id)
            dict = model_to_dict(sys)
            del dict['created_at']
            json_sys = json.dumps(dict)
            return JsonResponse({
                'success': True,
                'sys': json_sys,
            })

