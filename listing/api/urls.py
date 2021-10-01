from django.conf.urls import url
from rest_framework import routers
from django.urls import path, include
from listing.api import views

# from rest_framework.authtoken.views import obtain_auth_token
from listing.api.pulseRoute import for_pulse

router = routers.DefaultRouter()
# router.register('hotels', views.HotelViewSet)
# router.register('city', views.HotelCitySet)
# router.register('hotelname', views.HotelNameSet)
# router.register('landmark', views.HotelLandmarkSet)
# # router.register('country', views.CountrySet)

urlpatterns = [
    path('', include(router.urls)),
    path('listedProperties/', views.listedProperties, name='listedProperties'),
    path('bookingOnaDate/', views.bookingOnaDate, name='bookingOnaDate'),
    path('paymentSummary/', views.paymentSummary, name='paymentSummary'),
    path('paymentDetail/', views.paymentDetail, name='paymentDetail'),
    path('cancellationPolicy/', views.CancellationPolicyList.as_view(), name='cancellationPolicy'),
    path('childSupplementPolicy/', views.childSupplementPolicy, name='childSupplementPolicy'),
    path('extraBedPolicy/', views.extraBedPolicy, name='extraBedPolicy'),
    path('cribPolicy/', views.cribPolicy, name='cribPolicy'),
    url(r'^pulse/(?P<token>\w+)/(?P<module>\w+)/(?P<operation>\w+)/(?P<id>\d+)/$', for_pulse),

]
