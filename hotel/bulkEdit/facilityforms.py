from django import forms
from django.forms import models, ModelChoiceField
from django.forms.fields import MultipleChoiceField

from hotel.addonservices.models import AddOnServices
from hotel.amenities.models import HotelAmenities
from hotel.inventory.models import hotelinventory_amenities, HotelInventory
import re

#
# class AdvancedModelChoiceIterator(models.ModelChoiceIterator):
#     def choice(self, obj):
#         return (self.field.prepare_value(obj), self.field.label_from_instance(obj), obj)
#
#
# class AdvancedModelChoiceField(models.ModelMultipleChoiceField):
#     def _get_choices(self):
#         if hasattr(self, '_choices'):
#             return self._choices
#         return AdvancedModelChoiceIterator(self)
#
#     choices = property(_get_choices, MultipleChoiceField._set_choices)


class FacilityForm(forms.ModelForm):

    def save(self, commit=True):
        m = super(FacilityForm, self).save(commit=False)
        hotel_id = self.data['hotel_id']
        list_of_inv_tuples = HotelInventory.objects.filter(hotel_id=hotel_id).values_list('id')
        list_of_inv_ids = []
        for inv in list_of_inv_tuples:
            list_of_inv_ids.append(inv[0])

        services_to_be_deleted = AddOnServices.objects.filter(inventory_id__in=list_of_inv_ids).values_list('id')
        services_array = []
        for service in services_to_be_deleted:
            services_array.append(service[0])
            # instance = AddOnServices.objects.get(id=service[0]).delete()

        for item in services_array:
            AddOnServices.objects.get(id=item).delete()

        bulkdata = self.data.getlist('inventory')
        list_of_tuple = []
        for sing_arr in bulkdata:
            mixedarray = re.findall(r'\d+', sing_arr)
            list_of_tuple.append(mixedarray)

        for tuple in list_of_tuple:
            if tuple[0] is not None and tuple[1] is not None:
                obj = AddOnServices()
                obj.price = 0
                obj.inventory = HotelInventory.objects.get(id=tuple[0])
                obj.amenities = HotelAmenities.objects.get(id=tuple[1])
                obj.status = True
                obj.save()

    class Meta:
        model = hotelinventory_amenities
        fields = [
            'hotelinventory', 'hotelamenities'
        ]

    class Media:
        js = ('js/my-multiselect.js',)

    def __init__(self, hotel, *args, **kwargs):
        super(FacilityForm, self).__init__(*args, **kwargs)
        self.fields['hotelinventory'].queryset = HotelInventory.objects.filter(hotel=hotel)
        self.fields['hotelamenities'].queryset = HotelAmenities.objects.all()
