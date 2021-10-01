from django.urls import path, include
from booking.module_booking import views

urlpatterns = [
    path('delete/<int:pk>', views.ModuleBookingDelete.as_view(), name="module-booking-delete"),
    # path('<int:pk>', views.ModuleBookingView.as_view(), name="module-booking"),
    path('', views.AdminBookingList.as_view(), name="module-booking-admin"),
    path('create/', views.ModuleBookingCreate.as_view(), name="module-booking-create"),
    path('show/<int:pk>', views.ModuleBookingDetail.as_view(), name="module-booking-show"),
    path('update/<int:pk>', views.ModuleBookingUpdate.as_view(), name="module-booking-update"),
    path('<hotel_id>', views.list_booking, name="module-booking"),
]
