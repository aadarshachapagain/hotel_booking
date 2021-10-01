from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name="hotelBookindex"),
    # path('detail/<hotelbook_id>', views.showdetail, name="hotelbookdetail"),
    path('create/', views.create, name="hotelbookcreate"),
    # path('store/', viewshotelinv.store, name="hotelinvstore"),
    # path('delete/<hotelbook_id>', views.delete, name="hotelbookdelete"),
    # path('edit/<hotelbook_id>', views.edit, name="hotelBookedit"),
    # path('update/<hotelbook_id>', views.update, name="hotelBookUpdate"),


    # class based view
    path('', views.BookingListView.as_view(), name="hotelbookindex"), 
    path('delete/<hotelbook_id>',views.BookingDelete.as_view(),name="hotelbookdelete"),
    
    # path('create/', views.InventoryCreate.as_view(), name="hotelinvcreate"),
    path('show/<int:pk>',views.BookingDetail.as_view(),name="hotelbookdetail"),
    path('update/<int:pk>', views.BookingUpdate.as_view(), name="hotelBookUpdate"),


]


   
