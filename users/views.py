from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
from .forms import UsersForm
from django.contrib import messages
from hashutils import make_pw_hash, check_pw_hash


# Create your views here.
def store(request):
    if request.method == 'POST':
        form = UsersForm(request.POST or None, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            hash_password = make_pw_hash(form.cleaned_data.get('hash_password'))
            post.hash_password = hash_password
            post.save()
            messages.success(request, ('User has been added to list'))
            return redirect('user-home')
        else:
            context = {
                'error': form.errors
            }
            messages.success(request, ('Please enter the data correctly'))
            return render(request, 'users/create.html', context)


def update(request, user_id):
    if request.method == 'POST':
        item = Users.objects.get(id=user_id)
        form = UsersForm(request.POST or None, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('User Has Been Updated'))
            return redirect('user-home')
        else:
            item = Users.objects.get(id=user_id)
            messages.success(request, ('User cannot Be Updated'))
            return render(request, 'users/create.html', {'item': item})


def index(request):
    all_items = Users.objects.all
    return render(request, 'users/index.html', {'all_items': all_items})


def create(request):
    all_items = Users()
    return render(request, 'users/create.html', {'all_items': all_items})


def edit(request, user_id):
    all_items = Users.objects.get(id=user_id)
    return render(request, 'users/create.html', {'all_items': all_items})


def show(request, user_id):
    all_item = Users.objects.get(id=user_id)
    return render(request, 'users/show.html', {'all_item': all_item})


def delete(request, user_id):
    item = Users.objects.get(id=user_id)
    item.delete()
    messages.success(request, ('Item has been deleted'))
    return redirect('user-home')
