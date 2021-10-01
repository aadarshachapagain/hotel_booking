from django.contrib import admin
from django.urls import path, include
# from . import viewsamenities
from . import views

# from . import views

urlpatterns = [

    path('delete/<int:pk>', views.FacilitiesDelete.as_view(), name="hotelfacilities-delete"),
    path('', views.FacilitiesList.as_view(), name="hotelfacilities"),
    path('create/', views.FacilitiesCreate.as_view(), name="hotelfacilities-create"),
    path('create/<hotel_id>', views.HotelFeatureCreate.as_view(), name="hotelfacilities-newcreate"),
    path('show/<int:pk>', views.FacilitiesDetail.as_view(), name="hotelfacilities-show"),
    path('update/<int:pk>', views.FacilitiesUpdate.as_view(), name="hotelfacilities-update"),

]
