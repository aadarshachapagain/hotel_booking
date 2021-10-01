from PIL import Image
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from travel.utils import deleteCroppedImagePreview
from .models import OwnerProfile
from .forms import OwnerProfileForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from hashutils import make_pw_hash, check_pw_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from account.models import User
from hotel.Country.models import Country
import shutil


@method_decorator([login_required], name='dispatch')
class OwnerListView(ListView):
    model = OwnerProfile
    template_name = 'ownerprofile/index.html'
    context_object_name = 'all_items'


@method_decorator([login_required], name='dispatch')
class OwnerDelete(SuccessMessageMixin, DeleteView):
    model = OwnerProfile
    success_url = reverse_lazy('ownerprofileindex')
    pk_url_kwarg = 'owner_id'

    def get(self, request, *args, **kwargs):
        User.objects.filter(id=self.kwargs['owner_id']).update(is_active=0)
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
class OwnerDetail(DetailView):
    model = OwnerProfile
    template_name = 'ownerprofile/show.html'
    queryset = OwnerProfile.objects.all()


@method_decorator([login_required], name='dispatch')
class OwnerCreate(SuccessMessageMixin, CreateView):
    template_name = 'ownerprofile/create.html'
    model = OwnerProfile
    form_class = OwnerProfileForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('ownerprofileindex')

    def form_valid(self, form):
        post = form.save(commit=False)
        hash_password = make_pw_hash(form.cleaned_data.get('password'))
        post.password = hash_password
        post.save()
        deleteCroppedImagePreview(self.request, 'user_profile')
        messages.success(self.request, 'User added successfully.')
        return super(OwnerCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        countries = Country.objects.all()
        context = super(OwnerCreate, self).get_context_data(**kwargs)
        context['countries'] = countries
        return context


@method_decorator([login_required], name='dispatch')
class OwnerUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'ownerprofile/create.html'
    model = OwnerProfile
    form_class = OwnerProfileForm
    success_message = 'Information Updated Successfully'
    queryset = OwnerProfile.objects.all()

    def get_success_url(self):
        item = self.object
        return reverse_lazy('ownerprofileshow', kwargs={'pk': item.user.id})

    def form_valid(self, form):
        item = self.object
        deleteCroppedImagePreview(self.request, 'user_profile')
        return super(OwnerUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        user_id = self.object.user.id
        return self.render_to_response(self.get_context_data(object=form.data, user_id=user_id))

    def get_context_data(self, **kwargs):
        countries = Country.objects.all()
        context = super(OwnerUpdate, self).get_context_data(**kwargs)
        context['countries'] = countries
        return context


import os
from django.conf import settings
from django.http import HttpResponse, Http404


# def download(request, path):
def downloadId(request):
    owner_directory = 'owner_doc' + str(request.user.id) + '/'
    directory_path = os.path.join(settings.MEDIA_ROOT, owner_directory)
    img_list = os.listdir(directory_path)
    file_name = img_list[0]
    final_path = owner_directory + file_name
    file_path = os.path.join(settings.MEDIA_ROOT, final_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/any")
            # response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response


# def pdf_view(request):
#     owner_directory = 'owner_doc' + str(request.user.id) + '/'
#     directory_path = os.path.join(settings.MEDIA_ROOT, owner_directory)
#     img_list = os.listdir(directory_path)
#     file_name = img_list[0]
#     final_path = owner_directory + file_name
#     file_path = os.path.join(settings.MEDIA_ROOT, final_path)
#     # with open('/app/../Test.pdf', 'r') as pdf:
#     with open(file_path, 'r') as pdf:
#         response = HttpResponse(pdf.read(), content_type='application/pdf')
#         response['Content-Disposition'] = 'filename=some_file.pdf'
#         return response
#     pdf.closed
