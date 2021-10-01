# from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
# from django.http import HttpResponse
#
# from account.Language.models import Language
# from account.Language.forms import LanguageForm
# from django.contrib import messages
# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.contrib.messages.views import SuccessMessageMixin
# from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
#
#
# # @method_decorator([login_required], name='dispatch')
# class LanguageListView(ListView):
#     model = Language
#     template_name = 'language/index.html'
#     context_object_name = 'all_items'
#
#
# # @method_decorator([login_required], name='dispatch')
# class LanguageDelete(SuccessMessageMixin, DeleteView):
#     model = Language
#     success_url = reverse_lazy('language')
#     pk_url_kwarg = 'country_id'
#
#     def get(self, request, *args, **kwargs):
#         messages.warning(self.request, "Successfully Deleted!!!")
#         return self.post(request, *args, **kwargs)
#
#
# # @method_decorator([login_required], name='dispatch')
# class LanguageDetail(DetailView):
#     model = Language
#     template_name = 'language/show.html'
#     queryset = Language.objects.all()
#
#
# # @method_decorator([login_required], name='dispatch')
# class LanguageCreate(SuccessMessageMixin, CreateView):
#     template_name = 'language/create.html'
#     model = Language
#     form_class = LanguageForm
#     success_message = 'Information Added Successfully'
#     success_url = reverse_lazy('language')
#
#     def form_invalid(self, form):
#         messages.warning(self.request, form.errors)
#         return self.render_to_response(self.get_context_data(object=form.data))
#
#     def get_context_data(self, **kwargs):
#         context = super(LanguageCreate, self).get_context_data(**kwargs)
#
#         return context
#
#
# # @method_decorator([login_required], name='dispatch')
# # @login_required
# class LanguageUpdate(SuccessMessageMixin, UpdateView):
#     template_name = 'language/create.html'
#     model = Language
#     form_class = LanguageForm
#     success_message = 'Information Updated Successfully'
#     success_url = reverse_lazy('language')
#     queryset = Language.objects.all()
#
#     def form_invalid(self, form):
#         messages.warning(self.request, form.errors)
#         return self.render_to_response(self.get_context_data(object=form.data))
#
#     def get_context_data(self, **kwargs):
#         context = super(LanguageUpdate, self).get_context_data(**kwargs)
#         return context
