import decimal
import json
from decimal import Decimal

from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from users.models import Users
from ..models import Hotels
from .models import HotelFacilities
from .forms import HotelFacilitiesForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


@method_decorator([login_required], name='dispatch')
class FacilitiesList(ListView):
    model = HotelFacilities
    template_name = 'facilities/index.html'
    context_object_name = 'hotelfacilities'


@method_decorator([login_required], name='dispatch')
class FacilitiesDetail(DetailView):
    model = HotelFacilities
    template_name = 'facilities/show.html'
    queryset = HotelFacilities.objects.all()


@method_decorator([login_required], name='dispatch')
class FacilitiesCreate(SuccessMessageMixin, CreateView):
    template_name = 'facilities/create.html'
    model = HotelFacilities
    form_class = HotelFacilitiesForm
    success_message = 'Information Added Successfully'
    success_url = reverse_lazy('hotel:hotelfacilities')

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(FacilitiesCreate, self).get_context_data(**kwargs)
        context['users'] = Users.objects.all().order_by('id').reverse()
        return context


# Create your views here.
# def index(request):   

#     hotelfacilities=Hotelfacilities.objects.all
#     data={

#             'hotelfacilities':hotelfacilities
#     }
#     return render(request,'facilities/index.html',data)


# def show(request,item_id):
#         item=Hotelfacilities.objects.get(pk=item_id)
#         return render(request,'facilities/show.html',{'item':item})

# def create(request):
#         item=Hotelfacilities()
#         user=Users.objects.all
#         data={
#                 'item':item,
#                 'users':user
#         }
#         return render(request,'facilities/create.html',data)

# def store(request):
#     if request.method=='POST':
#         form=HotelAmenityForm(request.POST or None)
#         if form.is_valid():
#             form.save()

#             messages.success(request,('Information Added Successfully'))
#             return redirect('hotelfacilities')
#         else:
#            messages.success(request,('Information Couldnot be added'))
#            item=Hotelfacilities()
#            return render(request,'facilities/create.html',{'item':item})


#     else:


#         messages.success(request,('Information Couldnot be added'))
#         item=Hotelfacilities()
#         return render(request,'facilities/create.html',{'item':item})

@method_decorator([login_required], name='dispatch')
class FacilitiesUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'facilities/create.html'
    model = HotelFacilities
    form_class = HotelFacilitiesForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:hotelfacilities')
    queryset = HotelFacilities.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(FacilitiesUpdate, self).get_context_data(**kwargs)
        context['users'] = Users.objects.all().order_by('id').reverse()
        return context


@method_decorator([login_required], name='dispatch')
class FacilitiesDelete(SuccessMessageMixin, DeleteView):
    model = HotelFacilities
    # pk_url_kwarg = 'facilities_id'
    success_url = reverse_lazy('hotel:hotelfacilities')

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


# def update(request,item_id):

#     if request.method=='POST':
#         item=Hotelfacilities.objects.get(pk=item_id)
#         form=HotelAmenityForm(request.POST or None, instance=item)
#         print(form.data)
#         if form.is_valid():           
#             form.save()           
#             messages.success(request,('Information Updated Successfull'))
#             return redirect('hotelfacilities')
#         else:
#            messages.success(request,('Information Couldnot be Updated'))
#            item=Hotelfacilities.objects.get(pk=item_id)
#            return render(request,'facilities/create.html',{'item':item})

#     else:
#         item=Hotelfacilities.objects.get(id=item_id)
#         return render(request,'facilities/create.html',{'item':item})

# def edit(request,item_id):
#         item=Hotelfacilities.objects.get(pk=item_id)
#         user=Users.objects.all
#         return render(request,'facilities/create.html',{'item':item,'users':user})

# def delete(request,item_id):
#     item=Hotelfacilities.objects.get(pk=item_id)
#     item.delete()   
#     messages.success(request,('Item Is Deleted'))
#     return redirect('hotelfacilities')

from hotel.models import HotelFacilitiesMiddle
from hotel.hotel_facilities.forms import HotelFeatureForm


class HotelFeatureCreate(FormView):
    template_name = 'facilities/hotel_feature.html'
    model = None
    form_class = HotelFeatureForm
    success_message = 'Information Added Successfully'
    errors2 = {}

    # def render_to_response(self, context, **response_kwargs):
    # 	item = self.object
    # 	response = super(HotelCreate, self).render_to_response(context, **response_kwargs)
    # 	response.set_cookie("current_hotel", item.id)
    # 	return response

    def get_success_url(self):
        hotel_id = self.kwargs['hotel_id']
        if self.form.data['register'] == 'Save and Exit':
            url = reverse_lazy('hotel:hotelindex', kwargs={'hotel_id':hotel_id})
        else:
            url = reverse_lazy('hotel:bank-detail-create', kwargs={'hotel_id':hotel_id})
        return url

        # item = self.object
        # hotel_id = self.kwargs['hotel_id']
        # # reverse('hotel:bank-detail-create', kwargs={'hotel_id': hotel})
        # response = redirect('hotel:bank-detail-create', hotel_id)
        # # return after cookie is set
        # # response.set_cookie('current_hotel', item.id)
        # return response

    # return reverse_lazy('hotel:addressupdate', kwargs={'pk': item.id})

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        for f in form.errors:
            self.errors2[f] = '.'.join(form.errors[f])
        return self.render_to_response(self.get_context_data(object=form.data))

    def form_valid(self, form):
        self.form = form
        features = form.data.getlist('featureexists')
        hotel_id = form.data.get('hotels')
        hotelsfacilities = form.data.getlist('hotelsfacilities')
        # freeorpaid = form.data.getlist('freeorpaid')
        # price = form.data.getlist('price')
        description = form.data.getlist('description')
        isrecomended = form.data.getlist('isrecomended')
        for index, feat in enumerate(features):
            feature_id = int(hotelsfacilities[index])
            if feat == 'yes':
                if HotelFacilitiesMiddle.objects.filter(hotelsfacilities_id=feature_id, hotels_id=hotel_id).exists():
                    HotelFacilitiesMiddle.objects.filter(hotelsfacilities_id=feature_id, hotels_id=hotel_id).delete()
                new_feature = HotelFacilitiesMiddle()
                new_feature.hotelsfacilities = HotelFacilities.objects.get(id=hotelsfacilities[index])
                new_feature.hotels = Hotels.objects.get(id=hotel_id)
                # new_feature.freeorpaid = freeorpaid[index]
                # new_feature.price = Decimal(price[index]) if price[index] != '' else 0.00
                new_feature.description = description[index]
                new_feature.isrecomended = isrecomended[index]
                new_feature.save()
            elif feat == 'no':
                if HotelFacilitiesMiddle.objects.filter(hotels_id=hotel_id, hotelsfacilities_id=feature_id).exists():
                    HotelFacilitiesMiddle.objects.filter(hotels_id=hotel_id, hotelsfacilities_id=feature_id).delete()
        return super(HotelFeatureCreate, self).form_valid(form)
        # response = redirect('hotel:bank-detail-create', hotel_id)
        # return response

    def get_context_data(self, **kwargs):
        # context = {}
        hotel_id = self.kwargs['hotel_id']
        context = super(HotelFeatureCreate, self).get_context_data(**kwargs)
        basic_physical_features = HotelFacilities.objects.filter(category='Basic')
        luxury_features = HotelFacilities.objects.filter(category='Luxury')
        additional_features = HotelFacilities.objects.filter(category='Additional')
        existingfeature = HotelFacilitiesMiddle.objects.filter(hotels_id=hotel_id)
        ef_list = []
        for ef in existingfeature:
            dict = model_to_dict(ef)
            price = str(dict['price'])
            del dict['price']
            dict.update({'price': price})
            ef_list.append(dict)

        context['basic_physical_features'] = basic_physical_features
        context['luxury_features'] = luxury_features
        context['additional_features'] = additional_features
        context['hotel_id'] = hotel_id
        context['existingfeature'] = json.dumps(ef_list)

        return context
