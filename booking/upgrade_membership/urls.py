from django.urls import path
from django.conf.urls import url, include
from booking.upgrade_membership import views

# app_name = 'booking'
urlpatterns = [

    path('show', views.show_membership, name="show_membership"),
    path('upgrade/', views.upgrade_membership, name="upgrade_membership"),



]
