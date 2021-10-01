from django.core.files.temp import NamedTemporaryFile
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import json
import decimal
import re

from account.staff_profile.models import StaffProfile
from hotel.bedType.models import BedType
from hotel.cancellation_policy.models import Cancellation_Policy
from hotel.child_supplement_policy.models import ChildSupplementPolicy
from hotel.cribsPolicy.models import cribsPolicy
from hotel.extraBed.models import ExtraBedPolicy
from hotel.inventoryOffers.models import InventoryOffers
from hotel.inventory_bed_type.models import Inventory_Bed_Type
from hotel.inventorygallery.models import InventoryGallery
from hotel.room_facilities.models import RoomFacilities
from ..amenities.models import HotelAmenities
from hotel.roomfeature.models import HotelRoomFeature
from hotel.roomtype.models import HotelRoomType
from .models import HotelInventory, hotelinventory_roomfeatures, hotelinventory_amenities, \
    hotelinventory_roomfacility
from .models import Hotels
from .forms import HotelInvForm
from account.Language.models import Language
from hotel.priceOfRoom.models import PriceInDiffSys
from hotel.addonservices.models import AddOnServices
from django.forms import model_to_dict
from hotel.inventory.defaultpriceforms import DefaultPriceForm


def toapproveinv(request):
    hotels = HotelInventory.objects.filter(is_active=False)
    data = {
        'all_items': hotels
    }
    return render(request, 'hotelInventory/invapproval.html', data)


def mass_approve(request):
    if request.method == 'POST':
        for i in request.POST.getlist('id[]'):
            HotelInventory.objects.filter(id=i).update(is_active=True)
        return JsonResponse({
            'success': True,
        })


def invapprovalpreview(request, item_id):
    # return  HttpResponse("sfa")
    object = HotelInventory.objects.get(pk=item_id)
    # hotelAddress = HotelAddress.objects.get(hotel_id=item_id)

    galleries = InventoryGallery.objects.filter(hotel_inventory_id=item_id)
    # context['cancellations'] = Cancellation_Policy.objects.filter(inventory=item_id)
    # context['bed_types'] = Inventory_Bed_Type.objects.filter(inventory=item_id)
    # context['item_id'] = item_id
    offers_rental = InventoryOffers.objects.filter(hotel_inventory=item_id)

    data = {
        'object': object,
        'galleries': galleries,
        'roomtypes': HotelRoomType.objects.filter(hotelinventory=item_id),
        'roomfeatures': HotelRoomFeature.objects.filter(hotelinventory=item_id),
        'amenities': HotelAmenities.objects.filter(hotelinventory=item_id),
        # 'cancellations': Cancellation_Policy.objects.filter(inventory=item_id),
        'bed_types': Inventory_Bed_Type.objects.filter(inventory=item_id),
        'item_id': item_id,
        'offers_rental': offers_rental

    }
    # data123={'var':123}
    return render(request, 'hotelInventory/invpreview.html', data)


def invapproveddone(request, item_id):
    HotelInventory.objects.filter(id=item_id).update(is_active=True)
    return redirect("hotel:invapprovehotel")


@method_decorator([login_required], name='dispatch')
class InventoryListView(ListView):
    model = HotelInventory
    template_name = 'hotelInventory/index.html'

    def get_context_data(self, object_list=None, **kwargs):
        hotel_id = self.kwargs['hotel_id']
        allaccounts = self.request.user.account_type.all()
        for account in allaccounts:
            if account.type == "hotel_owner":
                owner_id = self.request.user.id
                context = super(InventoryListView, self).get_context_data(**kwargs)
                context['hotel_id'] = hotel_id
                hotelsinv = HotelInventory.objects.filter(hotel_id=hotel_id)
                context['hotelsinv'] = hotelsinv
                return context
            elif account.type == "hotel_staff":
                user_id = self.request.user.id
                if account.type == "hotel_staff":
                    context = super(InventoryListView, self).get_context_data(**kwargs)
                    context['hotel_id'] = hotel_id
                    hotelsinv = HotelInventory.objects.filter(hotel_id=hotel_id)
                    context['hotelsinv'] = hotelsinv
                    return context


from hotel.inventory.decorators import inventory_detail_decorator


@method_decorator([inventory_detail_decorator], name='dispatch')
@method_decorator([login_required], name='dispatch')
class InventoryDetail(DetailView):
    model = HotelInventory
    template_name = 'hotelInventory/show.html'
    queryset = HotelInventory.objects.all()

    def render_to_response(self, context, **response_kwargs):
        item_id = self.kwargs['pk']
        response = super(InventoryDetail, self).render_to_response(context, **response_kwargs)
        response.set_cookie("hotel_inventory", item_id)
        return response

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['pk']
        inventory = HotelInventory.objects.get(id=item_id)
        inventorygallery = InventoryGallery.objects.filter(hotel_inventory_id=item_id)
        context = super(InventoryDetail, self).get_context_data(**kwargs)
        context['galleries'] = inventorygallery
        context['item_id'] = item_id
        context['roomFeatures'] = HotelRoomFeature.objects.filter(hotelinventory=item_id)
        context['roomFacilitiesBasic'] = inventory.roomfacility.filter(category='Basic')
        context['roomFacilitiesAdvanced'] = hotelinventory_roomfacility.objects.filter(roomfacility__category='Advanced', hotelinventory=item_id)
        context['bedTypes'] = Inventory_Bed_Type.objects.filter(inventory=item_id)
        context['roomAmenities'] = HotelAmenities.objects.filter(hotelinventory=item_id).order_by('category')
        return context


@method_decorator([login_required], name='dispatch')
class InventoryDelete(SuccessMessageMixin, DeleteView):
    model = HotelInventory
    pk_url_kwarg = 'inv_id'
    success_url = reverse_lazy('hotel:hotelinv-index')

    def get(self, request, *args, **kwargs):
        messages.warning(self.request, "Successfully Deleted!!!")
        return self.post(request, *args, **kwargs)


@method_decorator([login_required], name='dispatch')
class InventoryCreate(SuccessMessageMixin, CreateView):
    template_name = 'hotelInventory/create.html'
    model = HotelInventory
    form_class = HotelInvForm
    success_message = 'Information Added Successfully'

    def get_success_url(self):
        item = self.object
        if self.form.data['register'] == 'Save and Exit':
            return reverse_lazy('hotel:showinvdetail', kwargs={'pk': item.id})
        else:
            return reverse_lazy('hotel:room-facility-assign-create', kwargs={'item_id': item.id})

    @transaction.atomic
    def form_valid(self, form):
        inv = form.save(commit=False)
        item = self.object
        self.form = form
        # for room type
        roomtype = form.data.get('roomtype')
        type = HotelRoomType.objects.get(id=roomtype)
        # for room type
        inv.european_plan = form.data.get('european_plan') if form.data.get('european_plan') else 0
        inv.bedandbreakfast_plan = form.data.get('bedandbreakfast_plan') if form.data.get('bedandbreakfast_plan') else 0
        # discount for adult
        plan = []
        if form.data.get('european_plan'):
            plan.append('ep')
        if form.data.get('bedandbreakfast_plan'):
            plan.append('bb')
        
        if 'adult_max' in form.data:
            adult_max = int(form.data['adult_max'])
            
            priceforadultarray=[]
            if (adult_max > 1):
                for p in plan:
                    for j in range(0, adult_max - 1):
                        keyadult = "adult" + str(j) + '-' + p
                        plan = 'European Plan' if p == 'ep' else 'Bed and Breakfast Plan'
                        priceforadult = {}
                        if keyadult in form.data:
                            if form.data[keyadult] == '':
                                priceforadult.update({"for": keyadult})
                                priceforadult.update({"rate": '0'})
                                priceforadult.update({"plan": plan})
                                priceforadult.update({"adult_max": j+1})
                            elif form.data[keyadult] != '':
                                priceforadult.update({"for": keyadult})
                                priceforadult.update({"rate": form.data[keyadult]})
                                priceforadult.update({"plan": plan})
                                priceforadult.update({"adult_max": j+1})
                            priceforadultarray.append(priceforadult)
                inv.priceforadult = json.dumps(priceforadultarray)
            elif (adult_max == 1):
                inv.priceforadult = ''
        # discount for adult
        inv.roomtype = type
        inv.is_active = False
        inv.save()
    
        hotel = Hotels.objects.get(id=HotelInventory.objects.get(id=inv.pk).hotel_id)
        # assign policy to new inventory
        # newPolicy = Cancellation_Policy.objects.filter(change_status='new', hotel_id=hotel.pk)
        # for new in newPolicy:
        #     instance = Cancellation_Policy()
        #     instance.hotelInventory = HotelInventory.objects.get(id=inv.pk)
        #     instance.parent = new
        #     instance.hotel = Hotels.objects.get(id=HotelInventory.objects.get(id=inv.pk).hotel_id)
        #     instance.change_status = 'assigned'
        #     instance.save()

        newPolicy = ChildSupplementPolicy.objects.filter(change_status='new', hotel_id=hotel.pk)
        for new in newPolicy:
            instance = ChildSupplementPolicy()
            instance.hotelInventory = HotelInventory.objects.get(id=inv.pk)
            instance.parent = new
            instance.hotel = Hotels.objects.get(id=HotelInventory.objects.get(id=inv.pk).hotel_id)
            instance.change_status = 'assigned'
            instance.save()

        newPolicy = cribsPolicy.objects.filter(change_status='new', hotel_id=hotel.pk)
        for new in newPolicy:
            instance = cribsPolicy()
            instance.hotelInventory = HotelInventory.objects.get(id=inv.pk)
            instance.parent = new
            instance.hotel = Hotels.objects.get(id=HotelInventory.objects.get(id=inv.pk).hotel_id)
            instance.change_status = 'assigned'
            instance.save()

        newPolicy = ExtraBedPolicy.objects.filter(change_status='new', hotel_id=hotel.pk)
        for new in newPolicy:
            instance = ExtraBedPolicy()
            instance.hotelInventory = HotelInventory.objects.get(id=inv.pk)
            instance.parent = new
            instance.hotel = Hotels.objects.get(id=HotelInventory.objects.get(id=inv.pk).hotel_id)
            instance.change_status = 'assigned'
            instance.save()

        # for selected views
        roomfeatures = form.data.getlist('room_feature')
        if roomfeatures:
            for feature in roomfeatures:
                feature = HotelRoomFeature.objects.get(id=feature)
                hotelinventory_roomfeatures.objects.create(hotelinventory=inv, hotelroomfeature=feature)
        # for selected views
    
        # for new views
        alt_view_names = form.data.getlist('alt_view_name')
        if alt_view_names[0] != '':
            for name in alt_view_names:
                room_feature = HotelRoomFeature()
                room_feature.name = name
                room_feature.status = 'vendor'
                room_feature.save()
            
                hotelinventory_roomfeatures.objects.create(hotelinventory=inv, hotelroomfeature=room_feature)
        # for new views

        # assigning bed type to this room
        bed_type = form.data.getlist('bed_type')
        bed_count = form.data.getlist('bed_count')
        if bed_count[0] != '':
            for index, count in enumerate(bed_count):
                bed_type_instance = Inventory_Bed_Type()
                bed_type_instance.bed_type = BedType.objects.get(id=bed_type[index])
                bed_type_instance.inventory = inv
                bed_type_instance.save()
        # assigning bed type to this room
    
        # adding new bed type to this room
        bed_names = form.data.getlist('alt_bed_name')
        bed_counts = form.data.getlist('alt_bed_count')
        if bed_names[0] != '':
            for index, name in enumerate(bed_names):
                bed = BedType()
                bed.name = name
                bed.count = bed_counts[index]
                bed.description = None
                bed.roomtype = type
                bed.status = "vendor"
                bed.save()
            
                bed_type_instance = Inventory_Bed_Type()
                bed_type_instance.bed_type = bed
                bed_type_instance.inventory = inv
                bed_type_instance.save()
        # adding new bed type to this room

        # room amenities
        amenities = form.data.getlist('room_amenity')
        for amen in amenities:
            amenity = HotelAmenities.objects.get(id=amen)
            hotelinventory_amenities.objects.create(hotelinventory=inv, hotelamenities=amenity)
        # room amenities

        # extra amenities
        alt_amenities = form.data.getlist('alt_amenity_name')
        if alt_amenities[0] != '':
            for alt_amenity in alt_amenities:
                amenity_instance = HotelAmenities()
                amenity_instance.name = alt_amenity
                amenity_instance.status = 'vendor'
                amenity_instance.category = 'General'
                amenity_instance.save()
        
                hotelinventory_amenities.objects.create(hotelinventory=inv, hotelamenities=amenity_instance)
        # extra amenities

        # basic room facilities
        facilities = form.data.getlist('room_facility')
        for facility in facilities:
            fac = RoomFacilities.objects.get(id=facility)
            hotelinventory_roomfacility.objects.create(hotelinventory=inv, roomfacility=fac)
        # basic room facilities
    
        if 'paidservices' in form.data and form.data['paidservices'] != '':
            paidamenities = form.data['paidservices']
            paidamenities_list = json.loads(paidamenities)

            # Paid Add ons
            for pa in paidamenities_list:
                facid = pa['facid']
                facprice = pa['facprice']
                flatorpercent = pa['flatorpercent']

                service_instance = AddOnServices()
                service_instance.inventory = inv
                service_instance.amenities = HotelAmenities.objects.get(id=facid)
                service_instance.price = facprice
                service_instance.flatorpercent = flatorpercent
                service_instance.status = True
                service_instance.save()
            # Paid Add ons

        if 'freeservices' in form.data and form.data['freeservices'] != '':
            freeamenities = form.data['freeservices']
            freeamenities_list = json.loads(freeamenities)
            # Free Adons

            for fa in freeamenities_list:
                free_fac_id = int(re.search(r'\d+', fa).group())
                free_service_instance = AddOnServices()
                free_service_instance.inventory = inv
                free_service_instance.amenities = HotelAmenities.objects.get(id=free_fac_id)
                free_service_instance.price = 0
                free_service_instance.status = True
                free_service_instance.save()

            # Free Adons

        return super(InventoryCreate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        hotel_id = self.kwargs['hotel_id']
        context = super(InventoryCreate, self).get_context_data(**kwargs)
        context['hotels'] = Hotels.objects.all().order_by('id').reverse()
        allaccounts = self.request.user.account_type.all()
        for account in allaccounts:
            if account.type == "hotel_staff":
                user_id = self.request.user.id
                hotel_id = StaffProfile.objects.values_list('company_id', flat=True).get(user_id=user_id)
                context['hotel_id'] = hotel_id
            else:
                context['hotel_id'] = hotel_id

        context['roomamenities'] = HotelAmenities.objects.all().order_by('category')
        context['language'] = Language.objects.all().order_by('id').reverse()
        context['roomfeatures'] = HotelRoomFeature.objects.all()
        context['roomfacilities'] = RoomFacilities.objects.filter(category='Basic')
        context['roomtypes'] = HotelRoomType.objects.all().order_by('id').reverse()
        context['bed_types'] = BedType.objects.all()
        return context


@method_decorator([login_required], name='dispatch')
class InventoryUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'hotelInventory/edit.html'
    model = HotelInventory
    form_class = HotelInvForm
    success_message = 'Information Updated Successfully'

    def get_success_url(self):
        item = self.object
        if self.form.data['register'] == 'Save and Exit':
            return reverse_lazy('hotel:showinvdetail', kwargs={'pk': item.id})
        else:
            return reverse_lazy('hotel:room-facility-assign-create', kwargs={'item_id': item.id})

    @transaction.atomic
    def form_valid(self, form):
        self.form=form
        hotelinventory = form.save(commit=False)
        hotelinventory.is_active = False
        hotelinventory.european_plan = form.data.get('european_plan') if form.data.get('european_plan') else 0
        hotelinventory.bedandbreakfast_plan = form.data.get('bedandbreakfast_plan') if form.data.get('bedandbreakfast_plan') else 0
        roomtypes = form.data.get('roomtype')
        type = HotelRoomType.objects.get(id=roomtypes)
        hotelinventory.roomtype = type
        plan=[]
        if form.data.get('european_plan'):
            plan.append('ep')
        if form.data.get('bedandbreakfast_plan'):
            plan.append('bb')

        if 'adult_max' in form.data:
            adult_max = int(form.data['adult_max'])
    
            priceforadultarray = []
            if (adult_max > 1):
                for p in plan:
                    for j in range(0, adult_max - 1):
                        keyadult = "adult" + str(j) + '-' + p
                        plan = 'European Plan' if p == 'ep' else 'Bed and Breakfast Plan'
                        priceforadult = {}
                        if keyadult in form.data:
                            if form.data[keyadult] == '':
                                priceforadult.update({"for": keyadult})
                                priceforadult.update({"rate": '0'})
                                priceforadult.update({"plan": plan})
                                priceforadult.update({"adult_max": j + 1})
                            elif form.data[keyadult] != '':
                                priceforadult.update({"for": keyadult})
                                priceforadult.update({"rate": form.data[keyadult]})
                                priceforadult.update({"plan": plan})
                                priceforadult.update({"adult_max": j + 1})
                            priceforadultarray.append(priceforadult)
        
                hotelinventory.priceforadult = json.dumps(priceforadultarray)
            elif (adult_max == 1):
                hotelinventory.priceforadult = ''

        hotelinventory.save()

        item = self.object
        item_id = item.id

        # delete room feature
        hotelinventory.roomfeatures.through.objects.filter(hotelinventory=item_id).delete()
        # delete basic room facility
        hotelinventory.roomfacility.through.objects.filter(hotelinventory=item_id,
                                                           roomfacility__category='Basic').delete()
        # delete room amenities
        hotelinventory.amenities.through.objects.filter(hotelinventory=item_id).delete()
        # delete bed type
        Inventory_Bed_Type.objects.filter(inventory=item_id).delete()

        # for selected views - room features
        roomfeatures = form.data.getlist('room_feature')
        if roomfeatures:
            for feature in roomfeatures:
                feature = HotelRoomFeature.objects.get(id=feature)
                hotelinventory_roomfeatures.objects.create(hotelinventory=hotelinventory, hotelroomfeature=feature)
        # for selected views - room features

        # for new views
        alt_view_names = form.data.getlist('alt_view_name')
        if alt_view_names[0] != '':
            for name in alt_view_names:
                room_feature = HotelRoomFeature()
                room_feature.name = name
                room_feature.status = 'vendor'
                room_feature.save()
        
                hotelinventory_roomfeatures.objects.create(hotelinventory=hotelinventory, hotelroomfeature=room_feature)
        # for new views

        # basic room facilities
        facilities = form.data.getlist('room_facility')
        for facility in facilities:
            fac = RoomFacilities.objects.get(id=facility)
            hotelinventory_roomfacility.objects.create(hotelinventory=hotelinventory, roomfacility=fac)
        # basic room facilities

        # room amenities
        amenities = form.data.getlist('room_amenity')
        for amen in amenities:
            amenity = HotelAmenities.objects.get(id=amen)
            hotelinventory_amenities.objects.create(hotelinventory=hotelinventory, hotelamenities=amenity)
        # room amenities

        # extra amenities
        alt_amenities = form.data.getlist('alt_amenity_name')
        if alt_amenities[0] != '':
            for alt_amenity in alt_amenities:
                amenity_instance = HotelAmenities()
                amenity_instance.name = alt_amenity
                amenity_instance.category = 'General'
                amenity_instance.status = 'vendor'
                amenity_instance.save()
    
                hotelinventory_amenities.objects.create(hotelinventory=hotelinventory, hotelamenities=amenity_instance)
        # extra amenities

        # assigning bed type to this room
        bed_type = form.data.getlist('bed_type')
        bed_count = form.data.getlist('bed_count')
        if bed_count[0] != '':
            for index, count in enumerate(bed_count):
                bed_type_instance = Inventory_Bed_Type()
                bed_type_instance.bed_type = BedType.objects.get(id=bed_type[index])
                bed_type_instance.inventory = hotelinventory
                bed_type_instance.save()
        # assigning bed type to this room

        # adding new bed type to this room
        bed_names = form.data.getlist('alt_bed_name')
        bed_counts = form.data.getlist('alt_bed_count')
        if bed_names[0] != '':
            for index, name in enumerate(bed_names):
                bed = BedType()
                bed.name = name
                bed.count = bed_counts[index]
                bed.description = None
                bed.roomtype = type
                bed.status = "vendor"
                bed.save()

                bed_type_instance = Inventory_Bed_Type()
                bed_type_instance.bed_type = bed
                bed_type_instance.inventory = hotelinventory
                bed_type_instance.save()
        # adding new bed type to this room

        return super(InventoryUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(InventoryUpdate, self).get_context_data(**kwargs)
        
        inventory_id = self.get_object().id
        hotel_id = HotelInventory.objects.values_list('hotel_id', flat=True).filter(id=inventory_id).latest(
            'created_at')
        item = self.object
        item_id = item.id
        addedservices = []
        freeaddedservices = []
        context['hotel_id'] = hotel_id
        # Filtered for Selected
        roomamenities = list(HotelAmenities.objects.exclude(hotelinventory=item_id).order_by('category'))
        for room in roomamenities:
            room.checked = ''
        selectedamenities = list(HotelAmenities.objects.filter(hotelinventory=item_id).order_by('category'))
        for selected in selectedamenities:
            selected.checked = 'checked'
        
        roomamenities.extend(selectedamenities)
        roomamenities.sort(key=lambda i: i.category)
        context['finalamentity'] = roomamenities
        context['roomtypes'] = HotelRoomType.objects.all()
        context['bed_types'] = BedType.objects.all()
        context['selectedbedtypes'] = Inventory_Bed_Type.objects.filter(inventory=item_id)
        context['selectedroomfeatures'] = HotelRoomFeature.objects.filter(hotelinventory=item_id)
        context['roomfeatures'] = HotelRoomFeature.objects.exclude(hotelinventory=item_id)
        context['selectedroomfacilities'] = RoomFacilities.objects.filter(hotelinventory=item_id, category='Basic')
        context['roomfacilities'] = RoomFacilities.objects.filter(category='Basic').exclude(hotelinventory=item_id)
        services = AddOnServices.objects.filter(inventory_id=item_id, status=True, price__gt=0)
        freeservices = AddOnServices.objects.filter(inventory_id=item_id, status=True, price=0)
        for serv in services:
            dict_serv = model_to_dict(serv)
            str_price = str(decimal.Decimal(serv.price))
            del dict_serv['price']
            dict_serv.update({'price': str_price})
            addedservices.append(dict_serv)
        for freeserv in freeservices:
            free_dict_serv = model_to_dict(freeserv)
            free_str_price = str(decimal.Decimal(freeserv.price))
            del free_dict_serv['price']
            free_dict_serv.update({'price': free_str_price})
            freeaddedservices.append(free_dict_serv)

        clean_data = json.dumps(addedservices)
        free_clean_data = json.dumps(freeaddedservices)
        context['addonservices'] = clean_data
        context['freeaddonservices'] = free_clean_data
        return context


@method_decorator([login_required], name='dispatch')
class DefaultPriceUpdate(SuccessMessageMixin, UpdateView):
    template_name = 'hotelInventory/defaultprice.html'
    model = HotelInventory
    form_class = DefaultPriceForm
    success_message = 'Information Updated Successfully'

    def form_valid(self, form):
        hotelinventory = form.save(commit=False)
        adult_max = int(form.data['adult_max'])
        priceforadult = {}

        if (adult_max > 1):
            for j in range(0, adult_max - 1):
                keyadult = "adult" + str(j)
                if keyadult in form.data:
                    priceforadult[keyadult] = form.data[keyadult]
        elif (adult_max == 1):
            priceforadult = ''
        hotelinventory.priceforadult = json.dumps(priceforadult)
        hotelinventory.save()
        return super(DefaultPriceUpdate, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, form.errors)
        return self.render_to_response(self.get_context_data(object=form.data))

    def get_context_data(self, **kwargs):
        context = super(DefaultPriceUpdate, self).get_context_data(**kwargs)
        inventory_id = self.get_object().id
        context['inv_id'] = inventory_id
        hotel_id = HotelInventory.objects.get(id=inventory_id).hotel_id
        context['hotel_id'] = hotel_id
        context['adult_max'] = self.get_object().adult_max
        context['priceforadult'] = self.get_object().priceforadult
        return context

    def get_success_url(self):
        item = self.object
        return reverse_lazy('hotel:showinvdetail', kwargs={'pk': item.id})


class RoomFeatures(FormView):
    template_name = 'hotelInventory/roomfeatures.html'
    form_class = HotelInvForm

    def form_invalid(self, form):
        print('from.data')
        print(form.data)
        return self.render_to_response(self.get_context_data(form=form))


import os
from django.conf import settings
from django.core.files.base import File
from hotel.inventoryUpdate.models import InventoryUpdate as InvUpdate


def cloneInventory(request):
    if request.method == 'POST':
        source_inventory_id = int(request.POST['inventory_id'])
        clone_count = int(request.POST.get('count'))
        message = 'Clonning \n Inventory ID: {source_inventory_id} --> {clone_count} times'.format(
            source_inventory_id=source_inventory_id, clone_count=clone_count
        )
        hotel_id = HotelInventory.objects.get(id=source_inventory_id).hotel_id
        print(message)

        source_inventory = HotelInventory.objects.get(id=source_inventory_id)
        source_cribs_policies = cribsPolicy.objects.filter(hotelInventory_id=source_inventory_id)
        source_path = os.path.join(settings.MEDIA_ROOT, source_inventory.image.name)
        result_inventory = source_inventory
        image_name = os.path.basename(source_inventory.image.name)

        child_supplement_pilocies = ChildSupplementPolicy.objects.filter(hotelInventory_id=source_inventory_id)
        cancellation_policies = Cancellation_Policy.objects.filter(hotelInventory_id=source_inventory_id)
        extrabed_policies = ExtraBedPolicy.objects.filter(hotelInventory_id=source_inventory_id)
        inventory_galleries = InventoryGallery.objects.filter(hotel_inventory_id_id=source_inventory_id)
        hotel_inventory_facilities = hotelinventory_roomfacility.objects.filter(hotelinventory_id=source_inventory_id)
        hotel_inventory_amanities = hotelinventory_amenities.objects.filter(hotelinventory_id=source_inventory_id)
        hotel_inventory_room_features = hotelinventory_roomfeatures.objects.filter(
            hotelinventory_id=source_inventory_id)
        hotel_inventory_updates = InvUpdate.objects.filter(inventory_id=source_inventory_id)

        # Clone Inventory and create different image file accordingly
        result_inventories_list = []
        for c in range(clone_count):
            result_inventory.pk = None
            result_inventory.image.instance = source_inventory.image.instance
            result_inventory.save()
            try:
                with open(source_path, 'rb') as f:
                    data = f.read()
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(data)
                img_temp.flush()
                result_inventory.image.save(image_name, File(img_temp), save=True)
            except:
                pass
            result_inventories_list.append(result_inventory.id)

        # Clone cribs policies
        for crb in source_cribs_policies:
            for ril in result_inventories_list:
                new_cribpolicy = cribsPolicy.objects.get(id=crb.id)
                new_cribpolicy.pk = None
                new_cribpolicy.hotelInventory = HotelInventory.objects.get(id=ril)
                new_cribpolicy.save()

        # Clone Child supplment policies
        for csp in child_supplement_pilocies:
            for ril in result_inventories_list:
                new_childpolicy = ChildSupplementPolicy.objects.get(id=csp.id)
                new_childpolicy.pk = None
                new_childpolicy.hotelInventory = HotelInventory.objects.get(id=ril)
                new_childpolicy.save()

        # Clone Cancellation policies
        for cp in cancellation_policies:
            for ril in result_inventories_list:
                new_cancelpolicy = Cancellation_Policy.objects.get(id=cp.id)
                new_cancelpolicy.pk = None
                new_cancelpolicy.hotelInventory = HotelInventory.objects.get(id=ril)
                new_cancelpolicy.save()

        # Clone Extrabed policies
        for eb in extrabed_policies:
            for ril in result_inventories_list:
                new_ebpolicy = ExtraBedPolicy.objects.get(id=eb.id)
                new_ebpolicy.pk = None
                new_ebpolicy.hotelInventory = HotelInventory.objects.get(id=ril)
                new_ebpolicy.save()

        # Clone inventories_galleries
        for ig in inventory_galleries:
            for ril in result_inventories_list:
                new_inv_gallery = InventoryGallery.objects.get(id=ig.id)
                new_inv_gallery.pk = None
                new_inv_gallery.hotel_inventory_id = HotelInventory.objects.get(id=ril)
                source_path_for_gallery = os.path.join(settings.MEDIA_ROOT, new_inv_gallery.image.name)
                try:
                    with open(source_path_for_gallery, 'rb') as f:
                        datum_gallery = f.read()

                    gallery_temp = NamedTemporaryFile(delete=True)
                    gallery_temp.write(datum_gallery)
                    gallery_temp.flush()
                    new_inv_gallery.image.save(image_name, File(gallery_temp), save=True)
                except:
                    pass
                new_inv_gallery.save()

        #  Clone Room Facilities
        for hirf in hotel_inventory_facilities:
            for ril in result_inventories_list:
                new_hotel_inventory_facility = hotelinventory_roomfacility.objects.get(id=hirf.id)
                new_hotel_inventory_facility.pk = None
                new_hotel_inventory_facility.hotelinventory = HotelInventory.objects.get(id=ril)
                new_hotel_inventory_facility.save()

        #  Clone Room Amenities
        for hia in hotel_inventory_amanities:
            for ril in result_inventories_list:
                new_hotel_inventory_amenity = hotelinventory_amenities.objects.get(id=hia.id)
                new_hotel_inventory_amenity.pk = None
                new_hotel_inventory_amenity.hotelinventory = HotelInventory.objects.get(id=ril)
                new_hotel_inventory_amenity.save()

        # Clone Room Feature (View)
        for hrf in hotel_inventory_room_features:
            for ril in result_inventories_list:
                new_hotel_inventory_feature = hotelinventory_roomfeatures.objects.get(id=hrf.id)
                new_hotel_inventory_feature.pk = None
                new_hotel_inventory_feature.hotelinventory = HotelInventory.objects.get(id=ril)
                new_hotel_inventory_feature.save()

        # Clone hotel_inventory_updates
        for hiu in hotel_inventory_updates:
            for ril in result_inventories_list:
                new_hotel_inventory_update = InvUpdate.objects.get(id=hiu.id)
                new_hotel_inventory_update.pk = None
                new_hotel_inventory_update.inventory = HotelInventory.objects.get(id=ril)
                new_hotel_inventory_update.save()

        print('Clonning Completed')
        return redirect('hotel:hotelinv-index', hotel_id=hotel_id)



