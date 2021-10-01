from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile, File
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.http.request import QueryDict
from django.forms import formset_factory
from django.urls import reverse

from account.staff_profile.models import StaffProfile
from hotel.bankDetail.models import BankDetail
from hotel.cancellation_policy.models import Cancellation_Policy
from travel.utils import deleteCroppedImagePreview
from users.models import Users
from ..models import Hotels
from .models import HotelGallery
from hotel.staff.models import HotelStaff
from hotel.owner.models import HotelOwner
from ..inventory.models import HotelInventory
from ..amenities.forms import HotelAmenityForm
from .forms import HotelGalleryForm
from django.contrib import messages
from django.template.defaultfilters import slugify
# from .forms import HotelGalleryFormset
from django.contrib.auth.decorators import login_required


# from hotel.gallery.forms import HotelGalleryFormset
# from django.utils.decorators import method_decorator

# Create your views here.
@login_required
def index(request):
    user_id = request.user.id
    usertmp = request.user.account_type.all()
    for user_account in usertmp:
        if user_account.type == 'hotel_staff':
            # hotel_id = HotelStaff.objects.values_list('hotel_id', flat=True).get(user_id=user_id)
            hotel_id = StaffProfile.objects.values_list('company_id', flat=True).get(user_id=user_id)
            # hotel_id=Hotels.objects.values_list('id',flat=True).filter(owner_id=owner_id).latest('created_at')
            # print(hotel_id)
            hotelgalleries = HotelGallery.objects.filter(hotel_id=hotel_id)
        elif user_account.type == 'hotel_owner':
            owner_id = request.user.id
            hotel_id = Hotels.objects.values_list('id', flat=True).filter(owner_id=owner_id).latest('created_at')
            # if 'current_hotel' in request.COOKIES:
            #     current_hotel = request.COOKIES['current_hotel']
            # print('cookie')
            # print(current_hotel)
            # hotel_id = HotelOwner.objects.values_list('current_hotel', flat=True).get(user_id=owner_id)
            # hotel_id = current_hotel
            hotelgalleries = HotelGallery.objects.filter(hotel_id=hotel_id)

    #     hotelgalleries=HotelGallery.objects.all
    data = {
        'hotelgalleries': hotelgalleries,
        'hotel_id': hotel_id
    }
    return render(request, 'hotelgalleries/index.html', data)


def indexofGallery(request, item_id):
    hotelgalleries = HotelGallery.objects.filter(hotel_id=item_id)
    data = {
        'hotelgalleries': hotelgalleries,
        'hotel_id': item_id
    }
    return render(request, 'hotelgalleries/index.html', data)


@login_required
def show(request, item_id):
    item = HotelGallery.objects.get(pk=item_id)
    return render(request, 'hotelgalleries/show.html', {'item': item})


@login_required
def create(request, item_id):
    # for previous templates
    previousInstances = HotelGallery.objects.filter(hotel_id=item_id)
    templates = HotelGallery.templates(request)
    previous_template = []
    # for instance in previousInstances:
    # 	previous_template.append(instance.title)
    # remaining_template = list(set(main_template) - set(previous_template))
    item = HotelGallery()
    hotel = Hotels.objects.all
    hotel_inv_id = 0
    data = {
        'item': item,
        'hotels': hotel,
        'inv_id': hotel_inv_id,
        'hotel_id': item_id,
        'templates': templates
    }
    return render(request, 'hotelgalleries/create.html', data)


@login_required
def invcreate(request, item_id):
    print(item_id)
    item = HotelGallery()
    hotel = Hotels.objects.all
    data = {
        'item': item,
        'hotels': hotel,
        'hotel_id': item_id,
    }
    return render(request, 'hotelgalleries/create.html', data)


@login_required
def store(request):
    if request.method == 'POST':
        form = HotelGalleryForm(request.POST, request.FILES)
        print('form.data')
        print(form.data)
        if form.is_valid():
            images = request.FILES.getlist('files[]')
            titles = request.POST.getlist('title[]')
            x = request.POST.getlist('x[]')
            y = request.POST.getlist('y[]')
            h = request.POST.getlist('height[]')
            w = request.POST.getlist('width[]')
            hotel = request.POST.get('hotel_id')
            print('request.POST')
            print(request.POST)
            for index, i in enumerate(images):
                alldata = HotelGallery()
                if x[index] != '':
                    alldata.image = myCropper(i, float(x[index]), float(y[index]), float(w[index]) + float(x[index]),
                                              float(h[index]) + float(y[index]))
                else:
                    alldata.image = i
                alldata.hotel_id = Hotels.objects.get(id=hotel)
                alldata.title = titles[index]
                alldata.save()
                deleteCroppedImagePreview(request, 'hotel_inventory')
                bank = BankDetail.objects.filter(hotel=hotel).count()
            #     if hotel is not None:
            #         if bank <= 0:
            #             return JsonResponse({
            #                 'success': True,
            #                 'a': reverse('hotel:bank-detail-create', kwargs={'hotel_id': hotel}),
            #             })
            #         else:
            #             return JsonResponse({
            #                 'success': True,
            #                 'a': reverse('hotel:hotelgallery-index', kwargs={'item_id': hotel}),
            #             })
            #     else:
            #         return JsonResponse({'fail': False})
            # else:
            #     return JsonResponse({'fail': False})

            if hotel is not None:
                # item = self.object
                if form.data['register'] == 'Save and Exit':
                    # url = reverse_lazy('hotel:hotelindex', kwargs={'hotel_id': item.hotel_id})
                    url = JsonResponse({
                        'success': True,
                        'a': reverse('hotel:hotelindex', kwargs={'hotel_id': hotel}),
                    })
                else:
                    # url = reverse_lazy('hotel:hotelfacilities-newcreate', kwargs={'hotel_id': item.hotel_id})
                    url = JsonResponse({
                        'success': True,
                        'a': reverse('hotel:childSupplement-create', kwargs={'item_id': hotel}),
                    })
                return url
            else:
                return JsonResponse({'fail': False})
        else:
            return JsonResponse({'fail': False})


@login_required
def update(request, item_id):
    if request.method == 'POST':
        item = HotelGallery.objects.get(pk=item_id)
        form = HotelGalleryForm(request.POST or None, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            deleteCroppedImagePreview(request, 'hotel_inventory')
            messages.success(request, ('Information Updated Successfull'))
            return redirect('hotel:hotelgallery', item_id=item_id)
        else:
            item = HotelGalleryForm.objects.get(pk=item_id)
            data = {
                'item': item,
                'form': form.errors
            }
            return render(request, 'hotelgalleries/create.html', data)


@login_required
def editsingle(request, item_id):
    item = HotelGallery.objects.get(pk=item_id)
    hotel = Hotels.objects.all
    hotelinv = HotelInventory.objects.all
    data = {
        'object': item,
        'hotel_id': item_id,
        'hotelsinv': hotelinv,
    }
    return render(request, 'hotelgalleries/editsingleimage.html', data)


def updatesingle(request, item_id):
    item = HotelGallery.objects.get(pk=item_id)
    hotel_id = item.hotel_id_id
    if request.method == 'POST':
        image = request.FILES.get('image')
        x = request.POST.get('x')
        y = request.POST.get('y')
        h = request.POST.get('height')
        w = request.POST.get('width')
        if image:
            if x != '':
                item.image = myCropper(image, float(x), float(y), float(w) + float(x), float(h) + float(y))
            else:
                item.image = image
        else:
            item.image = item.image
        item.save()
        # second attribute is same as mention in template. i.e. model
        deleteCroppedImagePreview(request, 'hotel_inventory')
    item_id = hotel_id
    return redirect('hotel:hotelgallery-index', item_id)


@login_required
def edit(request, item_id):
    item = HotelGallery()
    hotel = Hotels.objects.all
    hotelinv = HotelInventory.objects.all
    hotelgalleries = HotelGallery.objects.filter(hotel_id=item_id)
    templates = HotelGallery.templates(request)
    print(hotelgalleries)
    data = {
        'item': item,
        'hotel_id': item_id,
        'hotelsinv': hotelinv,
        'galleries': hotelgalleries,
        'templates': templates,
    }
    return render(request, 'hotelgalleries/create.html', data)


@login_required
def delete(request, item_id):
    item = HotelGallery.objects.get(pk=item_id)
    hotel_id = item.hotel_id
    item.delete()
    messages.success(request, ('Item Is Deleted'))
    return redirect('hotel:hotelgallery-index', hotel_id.id)


def myCropper(original_image, left, top, bottom, right):
    extName = original_image.name.split(".")[-1]
    imageName = original_image.name.replace(extName + '.', '')
    format = 'JPEG' if extName.lower() == 'jpg' else extName.upper()
    img_io = BytesIO()
    original_image = Image.open(original_image)
    cropped_img = original_image.crop((left, top, bottom, right))
    cropped_img.save(img_io, format)
    img_content = File(img_io, name=imageName)
    return img_content
