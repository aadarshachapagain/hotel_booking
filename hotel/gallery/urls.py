
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name="hotelgallery"),
    url(r'^(?P<item_id>\d+)/',views.index,name="hotelgallery"),
    # url(r'^stores/',stores_views.detail),   
    path('create/<item_id>', views.create,name="hotelgallery-create"),
    # url(r'^create/(?P<id>\w+)/$', views.create, name="hotelgallery-create"),
    # url(r'^(?P<project_id>\w+)$', ProjectDetailView.as_view(), name="project_detail")
    path('store/', views.store, name="hotelgallery-store"),
    path('update/<item_id>', views.update, name="hotelgallery-update"),
    path('edit/<item_id>',views.edit,name="hotelgallery-edit"),
    path('editsingle/<item_id>',views.editsingle,name="hotelgallery-editsingle"),
    path('show/<item_id>',views.show,name="hotelgallery-show"),
    path('delete/<item_id>',views.delete,name="hotelgallery-delete"),
    path('indexgallery/<item_id>',views.indexofGallery,name="hotelgallery-index"),
    path('updatesingle/<item_id>', views.updatesingle, name="hotelgallery-updatesingle"),

]

