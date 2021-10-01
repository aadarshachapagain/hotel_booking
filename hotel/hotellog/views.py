from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.models import Users
from ..models import Hotels
from .models import HotelLog
from .forms import HotelLogForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

@method_decorator([login_required],name='dispatch')
class HotelLogList(ListView):
        model=HotelLog        
        template_name='HotelLog/index.html'
        context_object_name='all_items'

@method_decorator([login_required],name='dispatch')
class HotelLogDetail(DetailView):        
        model=HotelLog        
        template_name='HotelLog/show.html'
        queryset=HotelLog.objects.all()
      
@method_decorator([login_required],name='dispatch')
class HotelLogCreate(SuccessMessageMixin,CreateView):
    template_name = 'HotelLog/create.html'
    model=HotelLog 
    form_class=HotelLogForm
    success_message='Information Added Successfully'
    success_url=reverse_lazy('HotelLog')

    def form_invalid(self,form):
            messages.warning(self.request,form.errors)
            return self.render_to_response(self.get_context_data(object=form.data))
    
    def get_context_data(self, **kwargs):
        context = super(HotelLogCreate, self).get_context_data(**kwargs)
        context['users'] = Users.objects.all().order_by('id').reverse()             
        context['hotels'] = Hotels.objects.all().order_by('id').reverse()             
        return context

@method_decorator([login_required],name='dispatch')
class HotelLogUpdate(SuccessMessageMixin,UpdateView):
        template_name='HotelLog/create.html'
        model=HotelLog
        form_class=HotelLogForm
        success_message='Information Updated Successfully'
        success_url=reverse_lazy('HotelLog')
        queryset=HotelLog.objects.all()

        def form_invalid(self,form):
                messages.warning(self.request,form.errors)
                return self.render_to_response(self.get_context_data(object=form.data))
                
        def get_context_data(self, **kwargs):
            context = super(HotelLogUpdate, self).get_context_data(**kwargs)
            context['users'] = Users.objects.all().order_by('id').reverse()             
            context['hotels'] = Hotels.objects.all().order_by('id').reverse()             
            return context

@method_decorator([login_required],name='dispatch')
class HotelLogDelete(SuccessMessageMixin,DeleteView):
        model=HotelLog
        pk_url_kwarg='HotelLog_id'      
        success_url=reverse_lazy('HotelLog')
        def get(self,request,*args,**kwargs):                  
                messages.warning(self.request,"Successfully Deleted!!!")
                return self.post(request,*args,**kwargs)
     
