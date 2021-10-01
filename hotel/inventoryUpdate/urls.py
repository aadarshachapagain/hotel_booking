from django.urls import path

from . import views

urlpatterns = [
    # For Ajax call to get data
    path('getHotelDetail/', views.get_all_rooms, name="getHotelDetail"),
    path('room_separation/', views.room_separation, name="room_separation"),
    path('getRoomDetailByCategory/', views.get_room_detail_by_category, name="getRoomDetailByCategory"),
    path('separation_hotel_during_update/', views.separation_hotel_during_update,
         name="separation_hotel_during_update"),
    path('updateInventoryDetail/', views.update_inventory_detail, name="updateInventoryDetail"),
    path('condition_to_update_availability/', views.condition_to_update_availability,
         name="condition_to_update_availability"),

]
