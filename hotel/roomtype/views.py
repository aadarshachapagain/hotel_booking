from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from hotel.bedType.models import BedType
from hotel.roomfeature.forms import HotelRoomFeatureForm
from hotel.roomfeature.models import HotelRoomFeature
from hotel.roomtype.models import HotelRoomType
from hotel.roomtype.forms import HotelRoomTypeForm
from django.contrib import messages


@method_decorator([login_required], name='dispatch')
class HotelRoomTypeList(ListView):
    model = HotelRoomType
    template_name = 'hotelroomtype/index.html'
    context_object_name = 'hotelroomtypes'


@method_decorator([login_required], name='dispatch')
class HotelRoomTypeDetail(DetailView):
    model = HotelRoomType
    template_name = 'hotelroomtype/show.html'
    queryset = HotelRoomType.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(HotelRoomTypeDetail, self).get_context_data(**kwargs)
        context['beds'] = BedType.objects.filter(roomtype=self.kwargs['pk'])
        return context


@method_decorator([login_required], name='dispatch')
class HotelRoomTypeDelete(SuccessMessageMixin, DeleteView):
    model = HotelRoomType
    pk_url_kwarg = 'roomtype_id'
    success_url = reverse_lazy('hotel:hotelroomtype')

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)
    
    

@method_decorator([login_required], name='dispatch')
class HotelRoomTypeCreate(SuccessMessageMixin, CreateView):
    template_name = 'hotelroomtype/create.html'
    model = HotelRoomType
    form_class = HotelRoomTypeForm
    success_message = 'Information Added Successfully'
    my_form = ''

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_success_url(self):
        """
        This method return to appropriate pages according to the submit button.
        If "Save and Add New" data is saved and redirected to create page.
        Else If "Save and Exit" data is saved and redirected to index page.
        :return: Appropriate URL
        """
        register = self.my_form.replace(' ', '_')
        if register == 'Save_and_Add_New':
            return reverse_lazy('hotel:hotelroomtype-create')
        elif register == 'Save_and_Exit':
            return reverse_lazy('hotel:hotelroomtype')

    def get_context_data(self, **kwargs):
        context = super(HotelRoomTypeCreate, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        """
        This method saves type of room along with its associated bed types.
        Room type is related to model: HotelRoomType whereas Bed type is related
        to model : BedType.
        
        Room type is saved at first, after that Bed type is saved in separate table with
        with room type as foreign key.
        
        :param form: data from form
        :return: success url
        """
        self.my_form = form.data.get('register')
        form.save(commit=False)
        name = form.data.get('name')
        room_type = HotelRoomType()
        room_type.name = name
        room_type.save()
    
        bed_names = form.data.getlist('bed_name')
        bed_count = form.data.getlist('bed_count')
        descriptions = form.data.getlist('description')
        for index, name in enumerate(bed_names):
            bed = BedType()
            bed.name = name
            bed.roomtype = room_type
            bed.description = descriptions[index]
            bed.count = bed_count[index]
            bed.save()
        return HttpResponseRedirect(self.get_success_url())

@method_decorator([login_required], name='dispatch')
class HotelRoomTypeUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'hotelroomtype/create.html'
    model = HotelRoomType
    form_class = HotelRoomTypeForm
    success_message = 'Information Updated Successfully'
    success_url = reverse_lazy('hotel:hotelroomtype')
    queryset = HotelRoomType.objects.all()

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(HotelRoomTypeUpdate, self).get_context_data(**kwargs)
        context['beds'] = BedType.objects.filter(roomtype=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        This method saves type of room along with its associated bed types.
        Room type is related to model: HotelRoomType whereas Bed type is related
        to model : BedType.

        Room type is saved at first, after that Bed type is saved in separate table with
        with room type as foreign key.

        :param form: data from form
        :return: success url
        """
        self.my_form = form.data.get('register')
        form.save(commit=False)
        name = form.data.get('name')
        room_type = HotelRoomType.objects.get(id=self.kwargs['pk'])
        room_type.name = name
        room_type.save()
    
        bed_names = form.data.getlist('bed_name')
        bed_count = form.data.getlist('bed_count')
        descriptions = form.data.getlist('description')
        BedType.objects.filter(roomtype=self.kwargs['pk']).delete()
        for index, name in enumerate(bed_names):
            bed = BedType()
            bed.name = name
            bed.roomtype = room_type
            bed.description = descriptions[index]
            bed.count = bed_count[index]
            bed.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        """
        This method return to appropriate pages according to the submit button.
        If "Save and Add New" data is saved and redirected to create page.
        Else If "Save and Exit" data is saved and redirected to index page.
        :return: Appropriate URL
        """
        register = self.my_form.replace(' ', '_')
        if register == 'Save_and_Add_New':
            return reverse_lazy('hotel:hotelroomtype-create')
        elif register == 'Save_and_Exit':
            return reverse_lazy('hotel:hotelroomtype')
