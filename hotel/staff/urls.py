
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  
    path('delete/<int:pk>',views.StaffDelete.as_view(),name="staffdelete"),
    path('', views.StaffListView.as_view(), name="staffindex"), 
    path('create/', views.StaffCreate.as_view(), name="staffcreate"),
    path('show/<int:pk>',views.StaffDetail.as_view(),name="staffshow"),
    path('update/<int:pk>', views.StaffUpdate.as_view(), name="staffupdate"),

]