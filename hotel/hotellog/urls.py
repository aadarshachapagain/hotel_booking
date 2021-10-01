from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('delete/<HotelLog_id>',views.HotelLogDelete.as_view(),name="HotelLog-delete"),
    path('', views.HotelLogList.as_view(), name="HotelLog"), 
    path('create/', views.HotelLogCreate.as_view(), name="HotelLog-create"),
    path('show/<int:pk>',views.HotelLogDetail.as_view(),name="HotelLog-show"),
    path('update/<int:pk>', views.HotelLogUpdate.as_view(), name="HotelLog-update"),
]