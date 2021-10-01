
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from hotel.Country.models import Country
from hotel.b2b.forms import B2BForm
from hotel.b2b.models import B2B
from hotel.models import Hotels


class B2BListView(ListView):
	model = B2B
	template_name = 'b2b/index.html'
	context_object_name = 'all_items'
	
@method_decorator([login_required], name='dispatch')
class B2BDelete(SuccessMessageMixin, DeleteView):
	model = B2B
	pk_url_kwarg = 'detail_id'
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)
	
	def get_success_url(self):
		item = self.object
		return reverse_lazy('hotel:b2b')


# @method_decorator([login_required], name='dispatch')
# class B2BDetail(DetailView):
# 	model = B2B
# 	template_name = 'B2B/show.html'
# 	queryset = Language.objects.all()


@method_decorator([login_required], name='dispatch')
class B2BCreate(SuccessMessageMixin, CreateView):
	template_name = 'b2b/create.html'
	model = B2B
	form_class = B2BForm
	success_message = 'Information Added Successfully'
	
	def form_valid(self, form):
		return super(B2BCreate, self).form_valid(form)
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(B2BCreate, self).get_context_data(**kwargs)
		return context
	
	def get_success_url(self):
		return reverse_lazy('hotel:b2b')


@method_decorator([login_required], name='dispatch')
class B2BUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'b2b/create.html'
	model = B2B
	form_class = B2BForm
	success_message = 'Information Updated Successfully'
	queryset = B2B.objects.all()
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
		
	def get_context_data(self, **kwargs):
		context = super(B2BUpdate, self).get_context_data(**kwargs)
		return context
	
	def get_success_url(self):
		return reverse_lazy('hotel:b2b')
