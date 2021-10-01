from django.contrib import admin
from django.urls import path, include
from . import views
from . import addressview

urlpatterns = [
    path('', addressview.index, name="address-home"),
    path('create', addressview.create, name="address-create"),
    path('delete/<address_id>',addressview.delete, name='address-delete'),
    path('edit/<address_id>',addressview.edit, name='address-edit'),
    path('update/<address_id>',addressview.update, name='address-update'),
    path('show/<address_id>',addressview.show, name='address-show'),
    path('store',addressview.store, name='address-store'),
]