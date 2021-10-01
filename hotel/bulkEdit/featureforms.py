from django import forms
from hotel.inventory.models import hotelinventory_roomfeatures
from hotel.inventory.models import HotelInventory
from hotel.roomfeature.models import HotelRoomFeature
import re


class FeatureForm(forms.ModelForm):

    def save(self, commit=True):
        m = super(FeatureForm, self).save(commit=False)
        print('self-data')
        print(self.data)
        hotel_id = self.data['hotel_id']
        list_of_inv_tuples = HotelInventory.objects.filter(hotel_id=hotel_id).values_list('id')
        list_of_inv_ids = []
        for inv in list_of_inv_tuples:
            list_of_inv_ids.append(inv[0])

        features_to_be_deleted = hotelinventory_roomfeatures.objects.filter(
            hotelinventory_id__in=list_of_inv_ids).values_list('id')
        features_array = []
        for service in features_to_be_deleted:
            features_array.append(service[0])
            # instance = AddOnServices.objects.get(id=service[0]).delete()

        for item in features_array:
            hotelinventory_roomfeatures.objects.get(id=item).delete()

        bulkdata = self.data.getlist('inventory')
        list_of_tuple = []
        for sing_arr in bulkdata:
            mixedarray = re.findall(r'\d+', sing_arr)
            list_of_tuple.append(mixedarray)

        for tuple in list_of_tuple:
            if tuple[0] is not None and tuple[1] is not None:
                obj = hotelinventory_roomfeatures()
                # obj.price = 0
                # obj.inventory = HotelInventory.objects.get(id=tuple[0])
                obj.hotelinventory = HotelInventory.objects.get(id=tuple[0])
                obj.hotelroomfeature = HotelRoomFeature.objects.get(id=tuple[1])
                # obj.amenities = HotelAmenities.objects.get(id=tuple[1])
                # obj.status = True
                obj.save()

    class Meta:
        model = hotelinventory_roomfeatures
        fields = [
            'hotelinventory', 'hotelroomfeature'
        ]

    def __init__(self, hotel, *args, **kwargs):
        super(FeatureForm, self).__init__(*args, **kwargs)
        self.fields['hotelinventory'].queryset = HotelInventory.objects.filter(hotel=hotel)
        self.fields['hotelroomfeature'].queryset = HotelRoomFeature.objects.all()
