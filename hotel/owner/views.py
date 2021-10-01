from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from ..models import Hotels
from .models import HotelOwner
from .forms import HotelOwnerForm
from django.contrib import messages
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from hashutils import make_pw_hash, check_pw_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from account.models import User

@method_decorator([login_required],name='dispatch')
class OwnerListView(ListView):
        model=HotelOwner        
        template_name='owner/index.html'
        context_object_name='all_items'

@method_decorator([login_required],name='dispatch')
class OwnerDelete(SuccessMessageMixin,DeleteView):
        model=HotelOwner
        success_url=reverse_lazy('hotel:ownerindex')
        pk_url_kwarg='owner_id'  
        def get(self,request,*args,**kwargs):
                User.objects.filter(id=self.kwargs['owner_id']).update(is_active=0)
                messages.warning(self.request,"Successfully Deleted!!!")
                return self.post(request,*args,**kwargs)

     
@method_decorator([login_required],name='dispatch')
class OwnerDetail(DetailView):        
        model=HotelOwner        
        template_name='owner/show.html'
        queryset=HotelOwner.objects.all()
        
@method_decorator([login_required],name='dispatch')
class OwnerCreate(SuccessMessageMixin,CreateView):
    template_name = 'owner/create.html'
    model=HotelOwner
    form_class=HotelOwnerForm
    success_message='Information Added Successfully'
    success_url=reverse_lazy('ownerindex')

    def form_valid(self, form):
            post = form.save(commit=False)
            hash_password = make_pw_hash(form.cleaned_data.get('password'))
            post.password = hash_password
            post.save()
            messages.success(self.request, 'User added sucessfully.')
            return redirect('ownerindex')

    def form_invalid(self,form):
        messages.warning(self.request,form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))
    
    def get_context_data(self, **kwargs):
        context = super(OwnerCreate, self).get_context_data(**kwargs)
               
        return context


@method_decorator([login_required],name='dispatch')
# @login_required
class OwnerUpdate(SuccessMessageMixin,UpdateView):
        template_name='owner/create.html'
        model=HotelOwner
        form_class=HotelOwnerForm
        success_message='Information Updated Successfully'
        success_url=reverse_lazy('hotel:ownerindex')
        queryset=HotelOwner.objects.all()

        def form_invalid(self,form):
                messages.warning(self.request,form.errors)
                return self.render_to_response(self.get_context_data(object=form.data))
                        
        def get_context_data(self, **kwargs):
                context = super(OwnerUpdate, self).get_context_data(**kwargs)
                           
                return context


  