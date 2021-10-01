from points.virtual_point.models import VirtualPoint
from points.virtual_point.forms import VirtualPointForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required], name='dispatch')
class VirtualPointListView(ListView):
	model = VirtualPoint
	template_name = 'virtual_point/index.html'
	context_object_name = 'all_items'


@method_decorator([login_required], name='dispatch')
class VirtualPointDelete(SuccessMessageMixin, DeleteView):
	model = VirtualPoint
	success_url = reverse_lazy('points:virtual-points-index')
	pk_url_kwarg = 'virtual_id'
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
# class VirtualPointDetail(DetailView):
#     model = VirtualPoint
#     template_name = 'virtual_point/show.html'

@method_decorator([login_required], name='dispatch')
class VirtualPointCreate(SuccessMessageMixin, CreateView):
	template_name = 'virtual_point/create.html'
	model = VirtualPoint
	form_class = VirtualPointForm
	success_message = 'Information Added Successfully'
	
	def get_success_url(self):
		return reverse_lazy('points:virtual-points-index')
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def form_valid(self, form):
		virtual = form.save(commit=False)
		virtual.save()
		return super(VirtualPointCreate, self).form_valid(form)


class VirtualPointUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'virtual_point/create.html'
	model = VirtualPoint
	form_class = VirtualPointForm
	success_message = 'Information Updated Successfully'
	
	def form_valid(self, form):
		tour = form.save(commit=False)
		tour.is_active = False
		tour.save()
		return super(VirtualPointUpdate, self).form_valid(form)
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(VirtualPointUpdate, self).get_context_data(**kwargs)
		return context
	
	def get_success_url(self):
		return reverse_lazy('points:virtual-points-index')
