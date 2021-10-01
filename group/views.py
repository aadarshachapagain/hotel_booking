from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group, Permission
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from group.forms import GroupForm


@method_decorator([login_required], name='dispatch')
class GroupCreate(SuccessMessageMixin, CreateView):
	template_name = 'group/create.html'
	model = Group
	form_class = GroupForm
	success_message = 'Group Added'
	
	def form_valid(self, form):
		return super(GroupCreate, self).form_valid(form)
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		print(form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(GroupCreate, self).get_context_data(**kwargs)
		permission = Permission.objects.all()
		context['permissions'] = permission
		return context
	
	def get_success_url(self):
		return reverse_lazy('group:group-index')


@method_decorator([login_required], name='dispatch')
class GroupList(ListView):
	model = Group
	template_name = 'group/index.html'
	context_object_name = 'all_items'
	
	def get_context_data(self, **kwargs):
		context = super(GroupList, self).get_context_data(**kwargs)
		return context


class GroupDelete(SuccessMessageMixin, DeleteView):
	model = Group
	success_url = reverse_lazy('group:group-index')
	pk_url_kwarg = 'detail_id'
	
	def get(self, request, *args, **kwargs):
		messages.warning(self.request, "Successfully Deleted!!!")
		return self.post(request, *args, **kwargs)


class GroupUpdate(SuccessMessageMixin, UpdateView):
	template_name = 'group/create.html'
	model = Group
	form_class = GroupForm
	success_message = 'Information Updated Successfully'
	queryset = Group.objects.all()
	
	def form_invalid(self, form):
		messages.warning(self.request, form.errors)
		print(form.data)
		print(form.errors)
		return self.render_to_response(self.get_context_data(object=form.data))
	
	def get_context_data(self, **kwargs):
		context = super(GroupUpdate, self).get_context_data(**kwargs)
		group_id = self.kwargs['pk']
		permission = Permission.objects.exclude(group=group_id)
		group = Group.objects.get(id=group_id)
		context['selectedPermission'] = group.permissions.all()
		context['permissions'] = permission
		return context
	
	def form_valid(self, form):
		form.save(commit=False)
		group_id = self.kwargs['pk']
		group = Group.objects.get(id=group_id)
		group.name = form.data.get('name')
		group.save()
		permissionsForm = form.data.getlist('permissions')
		
		for permission in permissionsForm:
			per = Permission.objects.get(id=permission)
			group = Group.objects.get(id=group_id)
			group.permissions.add(per)
		return super(GroupUpdate, self).form_valid(form)
	
	def get_success_url(self):
		return reverse_lazy('group:group-index')



