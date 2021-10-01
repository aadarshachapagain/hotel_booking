from . import views, hotel_near_Landmark
from . import mutualviews
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

# from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('hotels', views.HotelViewSet)
router.register('city', views.HotelCitySet)
# router.register('hotelname', views.HotelNameSet)
router.register('landmark', views.HotelLandmarkSet)
# router.register('country', views.CountrySet)

urlpatterns = [
    path('', include(router.urls)),
    # path('hotelquery/', HotelQueryAPIView.as_view(), name='hotelquery')
    path('hotelquery/', HotelListAddressAPIView.as_view(), name='hotelquery'),
    path('hotellist/', HotelListAPIView.as_view(), name='hotellist'),
    path('hotelownerlist/', HotelOwnerListAPIView.as_view(), name='hotelownerlist'),
    path('hotelinventorylist/', HotelInventoryListAPIView.as_view(), name='hotelinventorylist'),
    path('newhotel/', NewHotelApi.as_view(), name='newhotelapi'),
    path('hotelgallerylist/', HotelGalleryListAPIView.as_view(), name='hotelgallerylist'),
    path('hoteladdresslist/', HotelAddressViewSet.as_view(), name='hotelsearchlist'),
    path('inventorysearchlist/', InventoryViewSet.as_view(), name='inventorylist'),
    # path('hotelfacilitylist/', HotelMiddleViewset.as_view(), name = 'hotelsearchlist'),
    path('mynew/', NewView.as_view(), name='newlist'),
    path('country/', views.CountrySet, name='countryset'),
    path('cityset/', views.HotelCitySet, name='cityyset'),

    # new may 28
    path('searchhotel/', HotelSearchViewSet.as_view(), name='hotelsearchlist'),
    path('inventorydetail/', views.defInventoryDetailAPIView, name='inventorydetail'),
    path('inventorylist/', views.defInventoryAPIView, name='inventorylist'),
    # path('inventorydetail/', views.InventoryDetailAPIView.as_view(), name='inventorydetail'),

    path('getdistance/', views.getDistance, name="getdistance"),
    path('getByCity/', views.getByCity, name="getByCity"),
    path('hotelsOnSpotlight/', views.getHotelsonSpotlight, name="getByspot"),
    path('mostlyUsedFacilities/', views.mostlyUsedFacilities, name='mostlyUsedFacilities'),
    path('hotelofferapi/', views.hotelOffers, name='hotel-offer-api'),
    path('allofferapi/', views.allofferapi, name='all-offer-api'),
    path('offerCard/', views.offerCard, name='offerCard'),
    path('shuffledallofferapi/', views.shuffledallofferapi, name='shuffledallofferapi'),
    path('hotelInventoryById/', views.hotelInventoryById, name='hotelInventoryById'),
    path('searchHotelByName/', views.searchHotelByName, name='searchHotelByName'),
    path('searchHotelByID/', views.searchHotelByID, name='searchHotelByID'),

    path('searchCityByName/', views.searchCityByName, name='searchCityByName'),
    path('getrooomfeatures', views.getrooomfeatures, name="getrooomfeatures"),
    path('addnewfeatures/', views.addnewfeatures, name="hotelroomfeatures-addnewfeatures"),

    path('gethotelnearLandmark/', hotel_near_Landmark.gethotelnearLandmark, name="gethotelnearLandmark"),
    path('globalSearch/', hotel_near_Landmark.globalSearch, name="globalSearch"),

    # -------------------------------For inventory filter--------------------------
    path('allbedpreferences/', views.allbedpreferences, name="allbedpreferences"),
    path('allroomfacilities/', views.allroomfacilities, name="allballroomfacilitiesdpreferences"),
    path('allhotelfacilities/', views.allhotelfacilities, name="allhotelfacilities"),
    path('min_maxprice/', views.min_maxprice, name="min_maxprice"),


    # -------------------------------For inventory filter--------------------------




#     ----------Mutual-----------------------------------------------------

    path('favourites/', mutualviews.addfavourites, name='addfavourites'),
    path('getfavourites/', mutualviews.getfavourites, name='getfavourites'),



#     ----------Mutual-----------------------------------------------------

]
