from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib import messages
from hotel.bulkEdit.facilityforms import FacilityForm
from hotel.inventory.models import hotelinventory_amenities, HotelInventory
from hotel.amenities.models import HotelAmenities
import re
from hotel.addonservices.models import AddOnServices
from hotel.bulkEdit.featureforms import FeatureForm
from hotel.inventory.models import hotelinventory_roomfeatures
from hotel.roomfeature.models import HotelRoomFeature
from hotel.bulkEdit.models import PriceAlterLog
from hotel.bulkEdit.pricealterforms import PriceAlterForm
from hotel.roomtype.models import HotelRoomType
import json


class BulkEditList(generic.TemplateView):
    template_name = 'bulkEdit/index.html'

    def get_context_data(self, **kwargs):
        hotel_id = self.kwargs.get('hotel_id')
        context = {}
        context.update({'hotel_id': hotel_id})
        return context


class BulkEditCreate(SuccessMessageMixin, generic.CreateView):
    template_name = 'bulkEdit/create.html'

    def get_success_url(self):
        return reverse_lazy('hotel:bulkedit-list', kwargs={'hotel_id': self.kwargs.get('id')})

    def form_valid(self, form):
        form.save(commit=False)
        hotel_id = self.kwargs.get('id')
        # list_of_inv_tuples = HotelInventory.objects.filter(hotel_id=hotel_id).values_list('id')
        # list_of_inv_ids = []
        # for inv in list_of_inv_tuples:
        #     list_of_inv_ids.append(inv[0])
        #
        # services_to_be_deleted = AddOnServices.objects.filter(inventory_id__in=list_of_inv_ids).values_list('id')
        # services_array = []
        # for service in services_to_be_deleted:
        #     services_array.append(service[0])
        #     # instance = AddOnServices.objects.get(id=service[0]).delete()
        #
        #
        # for item in services_array:
        #     AddOnServices.objects.get(id=item).delete()
        #
        # bulkdata = form.data.getlist('inventory')
        # list_of_tuple = []
        # for sing_arr in bulkdata:
        #     mixedarray = re.findall(r'\d+', sing_arr)
        #     list_of_tuple.append(mixedarray)
        #
        # for tuple in list_of_tuple:
        #     if tuple[0] is not None and tuple[1] is not None:
        #         obj = AddOnServices()
        #         obj.price = 0
        #         obj.inventory = HotelInventory.objects.get(id=tuple[0])
        #         obj.amenities = HotelAmenities.objects.get(id=tuple[1])
        #         obj.status = True
        #         obj.save()

        return super(BulkEditCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)

        print('form.data')
        print(form.data)
        print('self.form_class')
        print(self.form_class)
        print(form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_form_kwargs(self):
        """This method is what injects forms with their keyword
           arguments."""
        # grab the current set of form #kwargs
        kwargs = super(BulkEditCreate, self).get_form_kwargs()
        # Update the kwargs with the hotel
        kwargs['hotel'] = self.kwargs.get('id')
        return kwargs

    def get_form_class(self):
        model = self.kwargs.get('model')
        operation = self.kwargs.get('operation')
        id = self.kwargs.get('id')
        a = Switcher()
        temp, model = a.choose_module(model, operation)
        self.form_class = temp
        self.model = model
        return self.form_class

    def get_context_data(self, **kwargs):
        context = super(BulkEditCreate, self).get_context_data(**kwargs)
        hotel_id = self.kwargs.get('id')
        inventories_of_this_hotel = HotelInventory.objects.filter(hotel_id=hotel_id)
        amenities_selected = []
        features_selected = []
        list_of_inv_ids = HotelInventory.objects.filter(hotel_id=hotel_id).values_list('id')
        context.update({'hotel_id': hotel_id})
        context['inventories'] = inventories_of_this_hotel
        last_altered = ''
        last_altered_name = ''

        if self.form_class is FacilityForm:
            all_hotel_amenties = HotelAmenities.objects.filter(chargeable=False)
            pivotdata = AddOnServices.objects.filter(inventory_id__in=list_of_inv_ids)
            for pd in pivotdata:
                derived_name = str(pd.inventory.id) + '_amenity' + str(pd.amenities.id)
                amenities_selected.append(derived_name)
            context['room_amenties'] = all_hotel_amenties
            context['room_features'] = []
            context['amenities_selected'] = json.dumps(amenities_selected)

        if self.form_class is FeatureForm:
            all_room_features = HotelRoomFeature.objects.all()
            pivotfeaturesdata = hotelinventory_roomfeatures.objects.filter(hotelinventory_id__in=list_of_inv_ids)
            for pfd in pivotfeaturesdata:
                derived_name = str(pfd.hotelinventory.id) + '_features' + str(pfd.hotelroomfeature.id)
                features_selected.append(derived_name)
            context['room_features'] = all_room_features
            context['room_amenties'] = []
            context['features_selected'] = json.dumps(features_selected)
        if self.form_class is PriceAlterForm:

            if PriceAlterLog.objects.filter(hotel=hotel_id).order_by('created_at').exists():
                last_altered = PriceAlterLog.objects.filter(hotel=hotel_id).order_by('created_at').last()
                # last_altered = PriceAlterLog.objects.get(id=last_altered_id)
                context['lastaltered'] = last_altered
                # context = {
                #     'lastaltered': last_altered
                # }

                last_altered_name = HotelRoomType.objects.get(id=last_altered.altered_group).name
                context['last_altered_rate'] = last_altered.altered_percent
                context['last_altered_name'] = last_altered_name
                context['last_altered_type'] = last_altered.altered_type

            all_room_type = HotelRoomType.objects.all()
            list_roomType = []
            for type in all_room_type:
                formatted_data = formatByRoomType(type, hotel_id)
                if formatted_data:
                    list_roomType.append(formatted_data)
            room_type_list = json.dumps(list_roomType)
            context['room_amenties'] = []
            context['room_features'] = []
            # context['room_type_list'] = json.dumps(room_type_list)
            context['room_type_list'] = room_type_list

        return context


class Switcher(object):

    def choose_module(self, model, operation):
        """Dispatch method"""
        method_name = str(model)

        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid Model")
        # Call the method as we return it
        return method(operation)

    def facilities(self, operation):
        facilityInstance = FacilitiesRoute()
        # dynamically call the method of hotelInstance
        method = getattr(facilityInstance, operation, lambda: "Invalid Operation")
        return method()

    def features(self, operation):
        featureInstance = FeaturesRoute()
        # dynamically call the method of hotelInstance
        method = getattr(featureInstance, operation, lambda: "Invalid Operation")
        return method()

    def price(self, operation):
        priceInstance = PriceRoute()
        method = getattr(priceInstance, operation, lambda: "Invalid Operation")
        return method()


class FacilitiesRoute(object):
    def create(self):
        form = FacilityForm
        model = hotelinventory_amenities
        return form, model

    def update(self):
        url = "hotel:hotelupdate"
        return url


class FeaturesRoute(object):
    def create(self):
        form = FeatureForm
        model = hotelinventory_roomfeatures
        return form, model


class PriceRoute(object):
    def create(self):
        form = PriceAlterForm
        model = PriceAlterLog
        return form, model


def formatByRoomType(type, hotel_id):
    dict_room_type = {}
    inventory_list = []
    inventories_of_type = HotelInventory.objects.filter(roomtype=type, hotel_id=hotel_id)
    for inventory in inventories_of_type:
        dict_inventory = {}
        dict_inventory['id'] = inventory.id
        dict_inventory['name'] = inventory.room_name
        dict_inventory['room_type_id'] = inventory.roomtype.first().id

        inventory_list.append(dict_inventory)
        dict_room_type[type.name] = inventory_list
    return dict_room_type
