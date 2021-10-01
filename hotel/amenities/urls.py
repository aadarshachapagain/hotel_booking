from django.contrib import admin
from django.urls import path, include
# from . import viewsamenities
from . import views
# from . import views

urlpatterns = [
   
    # path('', views.index, name="hotelamenities"),   
    # path('create/', views.create, name="hotelamenities-create"),
    # path('store/', views.store, name="hotelamenities-store"),
    # path('update/<item_id>', views.update, name="hotelamenities-update"),
    # path('edit/<item_id>',views.edit,name="hotelamenities-edit"),
    # path('show/<item_id>',views.show,name="hotelamenities-show"),
    # path('delete/<item_id>',views.delete,name="hotelamenities-delete"),

    path('delete/<amenities_id>',views.AmenitiesDelete.as_view(),name="hotelamenities-delete"),
    path('', views.AmenitiesList.as_view(), name="hotelamenities"), 
    path('create/', views.AmenitiesCreate.as_view(), name="hotelamenities-create"),
    path('show/<int:pk>',views.AmenitiesDetail.as_view(),name="hotelamenities-show"),
    path('update/<int:pk>', views.AmenitiesUpdate.as_view(), name="hotelamenities-update"),

]