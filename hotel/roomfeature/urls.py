from django.contrib import admin
from django.urls import path, include
# from . import viewsamenities
from . import views

# from . import views

urlpatterns = [


    path('delete/<feature_id>', views.HotelRoomFeaturesDelete.as_view(), name="hotelroomfeatures-delete"),
    path('', views.RoomFeatureList.as_view(), name="hotelroomfeatures"),
    path('create/', views.FeaturesCreate.as_view(), name="hotelroomfeatures-create"),
    path('show/<int:pk>', views.RoomFeatureDetail.as_view(), name="hotelroomfeatures-show"),
    path('update/<int:pk>', views.HotelRoomFeatureUpdate.as_view(), name="hotelroomfeatures-update"),



]