from . import views
from account.views import NormalUserSignUpView
from account.views import NormalUserSignUpView
from rest_framework import routers
from django.urls import path, include
from hotel.api.views import HotelListAPIView, NewHotelApi, NewView, HotelSearchViewSet, HotelAddressViewSet, \
	InventoryViewSet

from hotel.api.views import HotelListAddressAPIView
from hotel.api.views import HotelInventoryListAPIView
from hotel.api.views import HotelOwnerListAPIView
from hotel.api.views import HotelGalleryListAPIView

urlpatterns = [
	path('points/', views.defPointsAPIView, name="points")

]
