
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="user-home"),
    path('create', views.create, name="user-create"),
    path('delete/<user_id>',views.delete, name='user-delete'),
    path('edit/<user_id>',views.edit, name='user-edit'),
    path('update/<user_id>',views.update, name='user-update'),
    path('show/<user_id>',views.show, name='user-show'),
    path('store',views.store, name='user-store'),
]
