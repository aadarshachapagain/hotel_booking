
from django.urls import path, include
from . import views



urlpatterns = [


    path('delete/<roomtype_id>', views.HotelRoomTypeDelete.as_view(), name="hotelroomtype-delete"),
    path('', views.HotelRoomTypeList.as_view(), name="hotelroomtype"),
    path('create/', views.HotelRoomTypeCreate.as_view(), name="hotelroomtype-create"),
    path('show/<int:pk>', views.HotelRoomTypeDetail.as_view(), name="hotelroomtype-show"),
    path('update/<int:pk>', views.HotelRoomTypeUpdate.as_view(), name="hotelroomtype-update"),

]