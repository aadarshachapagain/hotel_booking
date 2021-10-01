from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.http.request import QueryDict
from django.urls import reverse

from users.models import Users
from ..models import Hotels
from .models import InventoryGallery
from ..inventory.models import HotelInventory
from ..amenities.forms import HotelAmenityForm
from .forms import InventoryGalleryForm
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request, inv_id):
    inventorygallery = InventoryGallery.objects.filter(hotel_inventory_id=inv_id)
    hotel_id = HotelInventory.objects.get(id=inv_id).hotel.id
    data = {
        'inventorygallery': inventorygallery,
        'inv_id': inv_id,
        'hotel_id': hotel_id,
    }
    return render(request, 'inventorygallery/index.html', data)


@login_required
def show(request, item_id):
    item = InventoryGallery.objects.get(pk=item_id)
    return render(request, 'inventorygallery/show.html', {'item': item})


@login_required
def indexlist(request, item_id):
    # inventorygallery = InventoryGallery.objects.all
    inventorygallery = InventoryGallery.objects.filter(hotel_inventory_id=item_id)
    hotel_id = HotelInventory.objects.get(id=item_id).hotel_id
    data = {
        'inventorygallery': inventorygallery,
        'inv_id': item_id,
        'hotel_id': hotel_id,
    }
    return render(request, 'inventorygallery/index.html', data)


@login_required
def create(request, item_id):
    item = InventoryGallery()
    hotel = Hotels.objects.all
    hotel_inv_id = item_id
    hotel_id = HotelInventory.objects.values_list('hotel_id', flat=True).filter(id=item_id).latest('created_at')

    data = {
        'item': item,
        'hotels': hotel,
        'inv_id': hotel_inv_id,
        'hotel_id': hotel_id,

    }

    return render(request, 'inventorygallery/create.html', data)


@login_required
def store(request):
    if request.method == 'POST':
        form = InventoryGalleryForm(request.POST, request.FILES)
        if form.is_valid():
            img = request.FILES.getlist('files[]')
            title = request.POST.getlist('title[]')
            inventory = request.POST.get('hotelInventoryId')

            for j, i in enumerate(img):
                instance = InventoryGallery()
                instance.title = title[j]
                instance.image = i
                instance.hotel_inventory_id = HotelInventory.objects.get(id=inventory)
                temp = instance.save()
                
            if request.POST['register'] == 'Save and Exit':
                return JsonResponse({
                    'success': True,
                    'a': reverse('hotel:showinvdetail', kwargs={'pk': inventory}),
                })
            else:
                return JsonResponse({
                    'success': True,
                    'a': reverse('hotel:inventoryPolicies-create', kwargs={
                        "model": "extrabed",
                        "operation": "list",
                        "id": HotelInventory.objects.get(id=inventory).hotel_id,
                        "inv_id": inventory,
                    }),
                })
            
        else:
            return HttpResponse('failed...')

   


@login_required
def update(request, item_id):
    if request.method == 'POST':
        item = InventoryGallery.objects.get(pk=item_id)
        print('id')
        print(item.hotel_inventory_id.id)
        form = InventoryGalleryForm(request.POST or None, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('Information Updated Successfull'))
            return redirect('hotel:inventorygallery', item.hotel_inventory_id.id)
        else:
            data = {
                'object': item,
                'myerror': form.errors,
                'hotel_inv_id': item.hotel_inventory_id.id,
            }
            return render(request, 'inventorygallery/editsingleimage.html', data)


@login_required
def editsingle(request, item_id):
    item = InventoryGallery.objects.get(pk=item_id)

    data = {
        'object': item,
        'hotel_inv_id': item.hotel_inventory_id.id,
    }
    return render(request, 'inventorygallery/editsingleimage.html', data)


def edit(request, item_id):
    item = InventoryGallery()
    inventorygallery = InventoryGallery.objects.filter(hotel_inventory_id=item_id)
    hotel_inv_id = item_id
    hotel_id = HotelInventory.objects.values_list('hotel_id', flat=True).filter(id=item_id).latest('created_at')

    data = {
        'item': item,
        'hotel_id': hotel_id,
        'inv_id': item_id,
        'galleries': inventorygallery
    }
    return render(request, 'inventorygallery/create.html', data)


@login_required
def delete(request, item_id):
    item = InventoryGallery.objects.get(pk=item_id)
    inv_id = InventoryGallery.objects.values_list('hotel_inventory_id', flat=True).get(pk=item_id)
    item.delete()
    messages.success(request, ('Item Is Deleted'))
    return redirect('hotel:inventorygallery-indexlist', inv_id)
