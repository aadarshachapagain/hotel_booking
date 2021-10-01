from django.urls import path, include
from booking.booking_table import views

urlpatterns = [
    path('delete/<int:pk>', views.BookingTableDelete.as_view(), name="booking-table-delete"),
    path('<company_id>', views.BookingTableView.as_view(), name="booking-table"),
    path('create/', views.BookingTableCreate.as_view(), name="booking-table-create"),
    # path('show/<int:pk>', views.BookingTableDetail.as_view(), name="booking-table-show"),
    path('detail/<int:pk>', views.BookingTableDetailAdmin.as_view(), name="admin-booking-table-show"),
    path('update/<int:pk>', views.BookingTableUpdate.as_view(), name="booking-table-update"),
    path('updateStatus/<pk>/<status>', views.BookingUpdateStatus, name="booking-updateStatus"),
    path('updateSeenStatus/<pk>/<status>', views.BookingUpdateSeenStatus, name="booking-update-seen-status"),
    path('show/<booking_id>', views.BookingDetail, name="booking-table-show"),

]
