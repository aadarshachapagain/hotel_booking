from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from booking.team_leader.forms import TeamLeaderForm
from booking.team_leader.models import TeamLeader


@method_decorator([login_required], name='dispatch')
class TeamLeaderListView(ListView):
	model = TeamLeader
	template_name = 'team_leader/index.html'
	context_object_name = 'all_items'


@method_decorator([login_required], name='dispatch')
class TeamLeaderDelete(SuccessMessageMixin, DeleteView):
	model = TeamLeader
	success_url = reverse_lazy('booking:team-leader-index')
	pk_url_kwarg = 'leader_id'
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
# class TeamLeaderDetail(DetailView):
#     model = TeamLeader
#     template_name = 'team_leader/show.html'

@method_decorator([login_required], name='dispatch')
class TeamLeaderCreate(SuccessMessageMixin, CreateView):
	template_name = 'team_leader/create.html'
	model = TeamLeader
	form_class = TeamLeaderForm
	success_message = 'Leader Type Added Successfully'
	
	def get_success_url(self):
		return reverse_lazy('booking:team-leader-index')
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def form_valid(self, form):
		credit = form.save(commit=False)
		credit.save()
		return super(TeamLeaderCreate, self).form_valid(form)


class TeamLeaderUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'team_leader/create.html'
	model = TeamLeader
	form_class = TeamLeaderForm
	success_message = 'Team Leader Updated Successfully'
	
	def form_valid(self, form):
		credit = form.save(commit=False)
		credit.is_active = False
		credit.save()
		return super(TeamLeaderUpdate, self).form_valid(form)
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(TeamLeaderUpdate, self).get_context_data(**kwargs)
		return context
	
	def get_success_url(self):
		return reverse_lazy('booking:team-leader-index')
