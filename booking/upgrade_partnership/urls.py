from django.urls import path
from django.conf.urls import url, include
from booking.upgrade_partnership import views

# app_name = 'booking'
urlpatterns = [

    path('show', views.show_partnership, name="show_partnership"),
    path('upgrade/', views.upgrade_partnership, name="upgrade_partnership"),



]
