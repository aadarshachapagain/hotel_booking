# from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

# from django.contrib.auth.decorators import login_required


app_name = 'hotel'
urlpatterns = [

    # path('address/', include('users.urlsaddress')),
    path('inventory/', include('hotel.inventory.urls')),
    path('cancellation/', include('hotel.cancellation_policy.urls')),
    path('booking/', include('hotel.booking.urls')),
    path('amenities/', include('hotel.amenities.urls')),
    path('roomFacilities/', include('hotel.room_facilities.urls')),
    path('hotelfacilities/', include('hotel.hotel_facilities.urls')),
    path('gallery/', include('hotel.gallery.urls')),
    path('invgallery/', include('hotel.inventorygallery.urls')),
    path('review/', include('hotel.reviews.urls')),
    path('owner/', include('hotel.owner.urls')),
    path('staff/', include('hotel.staff.urls')),
    path('address/', include('hotel.address.urls')),
    path('log/', include('hotel.hotellog.urls')),
    path('api/', include('hotel.api.urls')),
    path('city/', include('hotel.city.urls')),
    path('country/', include('hotel.Country.urls')),
    path('landmark/', include('hotel.landmark.urls')),
    path('state/', include('hotel.state.urls')),
    path('roomfeature/', include('hotel.roomfeature.urls')),
    path('roomtype/', include('hotel.roomtype.urls')),
    path('bedtype/', include('hotel.bedType.urls')),
    path('invbedtype/', include('hotel.inventory_bed_type.urls')),
    path('offers/', include('hotel.offers.urls')),
    path('inventoryOffers/', include('hotel.inventoryOffers.urls')),
    path('inventoryUpdate/', include('hotel.inventoryUpdate.urls')),
    path('bankDetail/', include('hotel.bankDetail.urls')),
    path('b2b/', include('hotel.b2b.urls')),
    path('bulkEdit/', include('hotel.bulkEdit.urls')),
    path('childSupplement/', include('hotel.child_supplement_policy.urls')),
    path('extraBed/', include('hotel.extraBed.urls')),
    path('cribs/', include('hotel.cribsPolicy.urls')),
    path('specialRequest/', include('hotel.specialRequest.urls')),
    path('inventoryPolicies/', include('hotel.inventoryPolicies.urls')),
    path('roomFacilityAssign/', include('hotel.roomFacilityAssign.urls')),
    path('hotelspotlight/', include('hotel.spotlight.urls')),
    path('delete/<int:pk>', views.HotelDelete.as_view(), name="hoteldelete"),
    # path('', login_required(views.HotelListView.as_view()), name="hotelindex"), 
    path('index/<hotel_id>', views.HotelListView.as_view(), name="hotelindex"),
    path('create/', views.HotelCreate.as_view(), name="hotelcreate"),
    path('create/<prop_id>', views.HotelCreate.as_view(), name="hotelcreate-withprop"),
    path('createorupdate/<prop_id>', views.createorupdate, name="hotelcreateorupdate-withprop"),
    path('show/<int:pk>', views.HotelDetail.as_view(), name="hotelshow"),
    path('update/<int:pk>', views.HotelUpdate.as_view(), name="hotelupdate"),
    path('', views.hotelDashboardView, name="hoteldashboard"),
    path('hotelinfo/<hotel_id>', views.whichHotel, name="whichhotel"),

    path('adminapproval', views.toapprovehotel, name="approvehotel"),
    path('approvalpreview/<item_id>', views.approvalpreview, name="approvalpreview"),
    path('approveddone/<item_id>', views.approveddone, name="approveddone"),
    path('cookiedelete/', views.cookiedelete, name="cookie-delete"),
    path('hotelselect/', views.hotelyouown, name="hotelselect"),
    path('calendar/<hotel_id>', views.calendar, name="calendar"),
    path('json/<hotel_id>', views.myjson, name="json"),
    path('check_available/', views.check_availability, name="check_available"),
    path('hotel_list/', views.hotelList, name="hotel_list"),
    path('hotel_status/<id>/<status>', views.hotelStatus, name="hotel_status"),
    path('mass_active/', views.mass_active, name="mass_active"),
    path('mass_approve/', views.mass_approve, name="mass_approve"),

    # path('inventoryselect/', views.inventoryyouown, name="inventoryselect")

    # path('apihotel/',views.HotelViewSet.as_view(),name="hotelapi")
    # path('edit/<item_id>', views.editHotel, name="edithotel"),
    path('update/<item_id>', views.updateHotel, name="hotelupdate"),
    path('charges/', include('hotel.charges.urls')),
    path('mealplan/', include('hotel.mealPlan.urls')),
    path('ss/', include('hotel.similarSystems.urls')),
    path('groupRate/', include('hotel.groupRate.urls')),
    path('creditCard/', include('hotel.CreditCard.urls')),
    path('paymentPolicies/', include('hotel.PaymentPolicies.urls')),
    path('commissionPaymentPolicies/', include('hotel.CommissionPaymentPolicies.urls')),

    path('booking_calendar/<hotel_id>', views.booking_calendar, name="booking_calendar"),
    path('booking_json/<hotel_id>', views.get_booking_calendar, name="hotel_booking_json"),
    path('payment/', include('hotel.payment.urls')),

]
