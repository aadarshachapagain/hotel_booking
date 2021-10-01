from . import views
from . import rentalviews
from . import filterviews
from . import bookinginfoviews

from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    # path('hotelquery/', HotelListAddressAPIView.as_view(), name='hotelquery'),
    path('customer/', views.CustomerLoginAPIView.as_view(), name='customer_login'),
    path('customerProfile/<int:pk>', views.CustomerProfileAPIView.as_view(), name='customer_login'),
    path('availableInv/', views.availableInv, name="availableInv"),
    # path('tried', views.processRawData, name="processRawData"),
    path('first_hotel_list/', views.first_hotel_list, name='first_hotel_list'),
    path('init_booking/', views.init_booking, name='init_booking'),
    path('paymentAPI/', views.paymentAPI, name='paymentAPI'),
    path('guest_detail_old/', views.GuestDetailAPIView.as_view(), name='guest_detail'),
    path('guest_doc_detail/', views.GuestDocDetailAPIView.as_view(), name='guest_doc_detail'),
    path('payment/', views.PaymentAPIView.as_view(), name='payment'),
    # path('check_again/', views.check_again, name='check_again'),
    path('start_booking/', views.start_booking, name='start_booking'),
    path('guest_detail/', views.guest_detail, name='guest_detail'),
    path('booking_confirmed/', views.booking_confirmed, name='booking_confirmed'),
    path('referperson', views.referperson, name='referperson'),
    path('referrelation/', views.referrelation, name='referrelation'),
    path('gettrendingDestinations/', views.trendingDestinations, name='trendingDestinations'),
    path('check_available_inv_again/', views.check_available_inv_again, name='check_available_inv_again'),
    path('my_booking/', views.my_booking, name='my_booking'),
    # path('send_available_inv_dummy/', views.send_available_inv_dummy, name='send_available_inv_dummy'),

    # for travel and tour
    # path('first_package_list/', views.first_package_list, name='first_package_list'),
    # path('package_search_by_theme/', views.package_search_by_theme, name='package_search_by_theme'),
    # path('gettrendingPackages/', views.trendingPackages, name='trendingPackages'),
    path('review/', views.review, name='review'),

# ---------------------------------------Rental Booking----------------------------
#     path('available_rental/', rentalviews.available_rental, name='final_booking'),
    path('all_filter/', filterviews.filterinventory, name='filterinventory'),
    path('hotel_filter/', filterviews.hotel_filter, name='hotel_filter'),
    path('booking_tilldate/', bookinginfoviews.booking_tilldate, name='booking_tilldate'),






]

