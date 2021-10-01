from django.shortcuts import render, redirect
from ..amenities.models import HotelAmenities
from ..inventory.models import HotelInventory
from .models import HotelBooking
from ..models import Hotels
from users.models import Users
from .forms import HotelBookingForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import messages
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator([login_required],name='dispatch')
class BookingListView(ListView):
        model=HotelBooking    
        template_name='booking/index.html'
        context_object_name = 'hotelbooks'

@method_decorator([login_required],name='dispatch')
class BookingDetail(DetailView):
    model = HotelBooking
    template_name = 'booking/show.html'
    queryset = HotelBooking.objects.all()


@method_decorator([login_required],name='dispatch')
class BookingDelete(SuccessMessageMixin,DeleteView):
        model=HotelBooking         
        pk_url_kwarg='hotelbook_id'      
        success_url = reverse_lazy('hotelbookindex')
        
        def get(self,request,*args,**kwargs):                  
                messages.warning(self.request,"Successfully Deleted!!!")
                return self.post(request, *args, **kwargs)

@method_decorator([login_required],name='dispatch')
class BookingUpdate(SuccessMessageMixin, UpdateView):
    template_name='booking/edit.html'
    model=HotelBooking
    form_class=HotelBookingForm
    success_message='Information Updated Successfully'
    success_url=reverse_lazy('hotelbookindex')
    queryset = HotelBooking.objects.all()
        
    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))
                
        
    def get_context_data(self, **kwargs):
        context = super(BookingUpdate, self).get_context_data(**kwargs)
        context['hotelbooked'] = HotelBooking.objects.all().order_by('id').reverse()
        context['hotelinv'] = HotelInventory.objects.all().order_by('id').reverse()
        context['users'] = Users.objects.all().order_by('id').reverse()
        return context

    

def create(request):
    
    return HttpResponse('<h1>Sorry you are not allowed to create booking from here</h1>')


# def index(request):
#     hotelsinv = HotelInventory.objects.all
#     hotelbooks = HotelBooking.objects.all
#     users = Users.objects.all
#     contex = {
#         'hotelsinv': hotelsinv,
#         'users': users,
#         'hotelbooks': hotelbooks,
#     }
#     return render(request, 'booking/index.html', contex)
    # return HttpResponse('<h1>Hotel Booking home</h1>')


# def delete(request, hotelbook_id):
#     item = HotelBooking.objects.get(pk=hotelbook_id)
#     item.delete()
#     messages.success(request, ('Item has been deleted'))
#     return redirect('hotelBookindex')


# def showdetail(request, hotelbook_id):
#     hotelsbook = HotelBooking.objects.get(pk=hotelbook_id)
#     contex = {
#         'hotelsbook': hotelsbook,
#         # 'hotelamenities': hotelamenities
#     }
#     return render(request, 'booking/show.html', contex)
#     # return HttpResponse('<h1>Hotel Booking home</h1>')


# def edit(request, hotelbook_id):
#     hotelbooked = HotelBooking.objects.get(pk=hotelbook_id)
#     hotelinv = HotelInventory.objects.all
#     users = Users.objects.all
#     contex = {
#         'hotelinv': hotelinv,
#         'hotelbooked': hotelbooked,
#         'users': users
#     }
#     return render(request, 'booking/edit.html', contex)
    # return HttpResponse('<h1>Hotel Booking Edit</h1>')


# def update(request, hotelbook_id):
#     if request.method == 'POST':
#         item = HotelBooking.objects.get(pk=hotelbook_id)
#         form = HotelBookingForm(request.POST or None, instance=item)
#         print(form.data)
#         if form.is_valid():
#             form.save()
#             hotelbooked = HotelBooking.objects.all
#             messages.success(request, ('Information Updated Sucessful'))
#             return redirect('hotelBookindex')
#         else:
#             # print(form.errors)
#             messages.success(request, ('Infromation Couldont be updated'))
#             hotelbooked = HotelBooking.objects.get(pk=hotelbook_id)
#             context = {
#                 'error': form.errors,
#                 'hotelbooked': hotelbooked
#             }
#             return render(request, 'booking/edit.html', context)
#     else:
#         hotelbooked = HotelInventory.objects.get(pk=hotelinv_id)
#         return render(request, 'booking/edit.html', {'hotelbooked': hotelbooked})

    # return HttpResponse('<h1>Hotel Booking Edit</h1>')
