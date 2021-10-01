from decimal import Decimal
from django import forms
from hotel.inventory.models import hotelinventory_roomfeatures
from hotel.inventory.models import HotelInventory
from hotel.roomfeature.models import HotelRoomFeature
from hotel.bulkEdit.models import PriceAlterLog
import re
from hotel.roomtype.models import HotelRoomType
from django.db.models import F


class ChangeInInventory:

    def __init__(self):
        self.room_type_id = 0
        self.rate = 0
        self.altertype = ''
        self.hotel_id = 0
        self.altered_group = 0

    def changeprice(self):
        room_type_instance = HotelRoomType.objects.get(id=self.room_type_id)
        selected_inventory = HotelInventory.objects.filter(roomtype=room_type_instance, hotel_id=self.hotel_id)
        
        if self.altertype == 'increase':
            HotelInventory.objects.filter(roomtype=room_type_instance, hotel_id=self.hotel_id).update(
                european_plan=F('european_plan') + F('european_plan') * self.rate / 100)
            HotelInventory.objects.filter(roomtype=room_type_instance, hotel_id=self.hotel_id).update(
                bedandbreakfast_plan=F('bedandbreakfast_plan') + (F('bedandbreakfast_plan') * self.rate / 100))
            group_instance = HotelInventory.objects.filter(roomtype=room_type_instance, hotel_id=self.hotel_id)
            for g_i in group_instance:
                pal = PriceAlterLog()
                pal.hotel_inventory = HotelInventory.objects.get(id=g_i.id).id
                pal.altered_percent = self.rate
                pal.altered_type = 'increase'
                pal.hotel = self.hotel_id
                pal.altered_group = room_type_instance.id
                pal.save()

        if self.altertype == 'decrease':
            HotelInventory.objects.filter(roomtype=room_type_instance, hotel_id=self.hotel_id).update(
                european_plan=F('european_plan') - F('european_plan') * self.rate / 100)
            HotelInventory.objects.filter(roomtype=room_type_instance, hotel_id=self.hotel_id).update(
                bedandbreakfast_plan=F('bedandbreakfast_plan') - (F('bedandbreakfast_plan') * self.rate / 100))

            group_instance = HotelInventory.objects.filter(roomtype=room_type_instance, hotel_id=self.hotel_id)
            for g_i in group_instance:
                pal = PriceAlterLog()
                pal.hotel_inventory = HotelInventory.objects.get(id=g_i.id).id
                pal.altered_percent = self.rate
                pal.hotel = self.hotel_id
                pal.altered_group = room_type_instance.id
                pal.altered_type = 'decrease'
                pal.save()




class PriceAlterForm(forms.ModelForm):

    def clean(self):
        hotel_id = self.data['hotel_id']
        final_list = []
        room_type_id_list = HotelRoomType.objects.all()
        list_of_inv_ids = []
        list_of_inv_tuples = HotelInventory.objects.filter(hotel_id=hotel_id).values_list('id')

        for inv in list_of_inv_tuples:
            list_of_inv_ids.append(inv[0])

        for room_type in room_type_id_list:
            keyforvalue = 'ratechange' + str(room_type.id)
            keyforalter = 'altertype' + str(room_type.id)
            if keyforvalue in self.data and keyforalter in self.data:
                changetype = self.data[keyforalter]
                room_type_tuple = re.findall(r'\d+', keyforvalue)
                room_type_id = room_type_tuple[0]
                rate = Decimal.from_float(float(self.data[keyforvalue]))
                obj = ChangeInInventory()
                obj.room_type_id = room_type_id
                obj.rate = rate
                obj.altertype = changetype
                obj.hotel_id = hotel_id
                final_list.append(obj)

        for object in final_list:
            object.changeprice()

    # def save(self, commit=True):
    #     # m = super(PriceAlterForm, self).save(commit=False)
    #     print('self.data')
    #     print(self.data)
    #     hotel_id = self.data['hotel_id']
    #     final_list = []
    #     room_type_id_list = HotelRoomType.objects.all()
    #     list_of_inv_ids = []
    #     list_of_inv_tuples = HotelInventory.objects.filter(hotel_id=hotel_id).values_list('id')
    #     for inv in list_of_inv_tuples:
    #         list_of_inv_ids.append(inv[0])
    #
    #     for room_type in room_type_id_list:
    #         keyforvalue = 'ratechange' + str(room_type.id)
    #         keyforalter = 'altertype' + str(room_type.id)
    #         if keyforvalue in self.data and keyforalter in self.data:
    #             changetype = self.data[keyforalter]
    #             room_type_tuple = re.findall(r'\d+', keyforvalue)
    #             room_type_id = room_type_tuple[0]
    #             rate = Decimal.from_float(float(self.data[keyforvalue]))
    #             print('room_type')
    #             print(room_type_id)
    #             print('rate')
    #             print(rate)
    #             print('changetype')
    #             print(changetype)
    #             # single_room_type = HotelRoomType.objects.get(id=room_type_id)
    #             # selected_inv_roomtypes = hotelinventory_roomtype.objects.filter(hotelinventory__in=list_of_inv_ids)
    #             # selected_inv = []
    #             # for inv in selected_inv_roomtypes:
    #             #     item = HotelInventory.objects.get(id=inv.hotelinventory.id, hotel_id=hotel_id)
    #             #     selected_inv.append(item)
    #             # break
    #             obj = ChangeInInventory()
    #             obj.room_type_id = room_type_id
    #             obj.rate = rate
    #             obj.altertype = changetype
    #             obj.hotel_id = hotel_id
    #             final_list.append(obj)
    #
    #     for object in final_list:
    #         print('for bhitra')
    #         object.changeprice()
    #
    #
    #
    #
    #     # inv_of_type = []
    #     # print('final_list')
    #     # for item in final_list:
    #     #     room_type_instance = HotelRoomType.objects.get(id=item.room_type_id)
    #     #     inv_of_type = HotelInventory.objects.filter(roomtype=room_type_instance)
    #     #
    #     #     if item.altertype == 'increase':
    #     #         for iot in inv_of_type:
    #     #             si = HotelInventory.objects.get(id=iot.id)
    #     #             si.european_plan = si.european_plan + item.rate * (si.european_plan / 100)
    #     #             si.bedandbreakfast_plan = si.bedandbreakfast_plan + item.rate * (si.bedandbreakfast_plan / 100)
    #     #             si.save()
    #     #     if item.altertype == 'decrease':
    #     #         for dot in inv_of_type:
    #     #             sid = HotelInventory.objects.get(id=dot.id)
    #     #             sid.european_plan = sid.european_plan - item.rate * (sid.european_plan / 100)
    #     #             sid.bedandbreakfast_plan = sid.bedandbreakfast_plan - item.rate * (sid.bedandbreakfast_plan / 100)
    #     #             sid.save()
    #     #
    #     #     print('item.altertype')
    #     #     print(item.altertype)
    #     #     print('item.rate')
    #     #     print(item.rate)
    #     #     print('item.room_type_id')
    #     #     print(item.room_type_id)
    #
    #     # for single_inv in selected_inv:
    #     #     if changetype == 'increase':
    #     #         print('command is increase')
    #     #         si = HotelInventory.objects.get(id=single_inv.id)
    #     #         si.european_plan = si.european_plan + rate * (si.european_plan / 100)
    #     #         si.bedandbreakfast_plan = si.bedandbreakfast_plan + rate * (si.bedandbreakfast_plan / 100)
    #     #         si.save()
    #     #
    #     # for single_inv_dec in selected_inv:
    #     #     if changetype == 'decrease':
    #     #         print('command is decrease')
    #     #         sid = HotelInventory.objects.get(id=single_inv_dec.id)
    #     #         sid.european_plan = sid.european_plan - rate * (sid.european_plan / 100)
    #     #         sid.bedandbreakfast_plan = sid.bedandbreakfast_plan - rate * (sid.bedandbreakfast_plan / 100)
    #     #         sid.save()

    def save(self, commit=True):
        m = super(PriceAlterForm, self).save(commit=False)
        return m

    class Meta:
        model = PriceAlterLog
        fields = [
            'hotel', 'hotel_inventory', 'altered_percent', 'altered_type'
        ]

    def __init__(self, hotel, *args, **kwargs):
        super(PriceAlterForm, self).__init__(*args, **kwargs)
        self.fields['hotel_inventory'].queryset = HotelInventory.objects.filter(hotel=hotel)
        self.fields['altered_percent'].queryset = ''
