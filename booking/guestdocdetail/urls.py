from django.urls import path, include
from booking.guestdocdetail import views

urlpatterns = [

    path('', views.GuestDocDetailListView.as_view(), name="guestdocdetailindex"),
    path('create/', views.GuestDocDetailCreate.as_view(), name="guestdocdetailcreate"),
    path('update/<int:pk>', views.GuestDocDetailUpdate.as_view(), name="guestdocdetailupdate"),
    path('delete/<pk>', views.GuestDocDetailDelete.as_view(), name="guestdocdetaildelete"),

]
