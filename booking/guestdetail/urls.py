from django.urls import path, include
from booking.guestdetail import views

urlpatterns = [

    path('', views.GuestDetailListView.as_view(), name="guestdetailindex"),
    path('create/', views.GuestDetailCreate.as_view(), name="guestdetailcreate"),
    path('update/<int:pk>', views.GuestDetailUpdate.as_view(), name="guestdetailupdate"),
    path('delete/<pk>', views.GuestDetailDelete.as_view(), name="guestdetaildelete"),

]
