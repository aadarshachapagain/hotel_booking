from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:pk>',views.RoomFacilitiesDelete.as_view(),name="room-facilities-delete"),
    path('', views.RoomFacilitiesList.as_view(), name="room-facilities"),
    path('create/', views.RoomFacilitiesCreate.as_view(), name="room-facilities-create"),
    path('show/<int:pk>',views.RoomFacilitiesDetail.as_view(),name="room-facilities-show"),
    path('update/<int:pk>', views.RoomFacilitiesUpdate.as_view(), name="room-facilities-update"),

]