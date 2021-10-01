
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, AccessMixin
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from account.faq.forms import FAQForm
from account.faq.models import FAQ
from hotel.models import Hotels
from django.contrib.auth.decorators import permission_required, login_required


@method_decorator([login_required], name='dispatch')
class FAQListView(PermissionRequiredMixin, AccessMixin ,ListView):
	model = FAQ
	template_name = 'faq/index.html'
	context_object_name = 'all_items'
	permission_required = ('account.view_faq')
	
	
	def get_context_data(self, **kwargs):
		context = super(FAQListView, self).get_context_data(**kwargs)
		return context


# @method_decorator([login_required], name='dispatch')
class FAQDelete(SuccessMessageMixin, DeleteView):
	model = FAQ
	success_url = reverse_lazy('faq')
	pk_url_kwarg = 'detail_id'
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)


# @method_decorator([login_required], name='dispatch')
class FAQDetail(DetailView):
	model = FAQ
	template_name = 'faq/show.html'
	queryset = FAQ.objects.all()


# @method_decorator([login_required], name='dispatch')
class FAQCreate(SuccessMessageMixin, CreateView):
	template_name = 'faq/create.html'
	model = FAQ
	form_class = FAQForm
	success_message = 'Information Added Successfully'
	
	def form_valid(self, form):
		form.save(commit=False)
		answers = form.data.getlist('answer')
		questions = form.data.getlist('question')
		device = form.data.get('device')
		for index, question in enumerate(questions):
			instance = FAQ()
			instance.question = question
			instance.answer = answers[index]
			instance.device = device
			instance.save()
		return HttpResponseRedirect(self.get_success_url())
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(FAQCreate, self).get_context_data(**kwargs)
		return context
	
	def get_success_url(self):
		return reverse_lazy('faq')


# @method_decorator([login_required], name='dispatch')
# @login_required
class FAQUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'faq/create.html'
	model = FAQ
	form_class = FAQForm
	success_message = 'Information Updated Successfully'
	queryset = FAQ.objects.all()
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(FAQUpdate, self).get_context_data(**kwargs)
		return context
	
	def get_success_url(self):
		return reverse_lazy('faq')
