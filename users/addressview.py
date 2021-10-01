from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Address
from .models import Users
from .forms import AddressForm
from django.contrib import messages

# Create your views here.
def store(request):
    if request.method == 'POST':
        form = AddressForm(request.POST or None)
        if form.is_valid():
            form.save()
            # all_items = Users.objects.all
            messages.success(request, ('User has been added to list'))
            return redirect('address-home')
        else:
            messages.success(request, ('Please enter the data correctly'))
            return render(request, 'address/create.html', {}) 

def update(request,address_id):
    if request.method == 'POST':
        item = Address.objects.get(id=address_id)
        form = AddressForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('User Has Been Updated'))
            return redirect('address-home')
        else:
            all_items = Address.objects.get(id=address_id)
            messages.success(request, ('User cannot Be Updated'))
            return render(request, 'address/create.html' ,{'all_items':all_items})
        
def index(request):
    all_items = Address.objects.all
    return render(request, 'address/index.html', {'all_items': all_items})

def create(request):
    all_items = Address()
    user  = Users.objects.all
    context = {
        'all_items': all_items,
        'users': user
    }
    return render(request, 'address/create.html', context)

def edit(request, address_id):
    all_items = Address.objects.get(id=address_id)
    return render(request, 'address/create.html', {'all_items': all_items})

def show(request, address_id):
    all_item = Address.objects.get(id=address_id)
    return render(request, 'address/show.html', {'all_item': all_item})

def delete(request, address_id):
    item = Address.objects.get(id=address_id)
    item.delete()
    messages.success(request, ('Item has been deleted'))
    return redirect('address-home')
