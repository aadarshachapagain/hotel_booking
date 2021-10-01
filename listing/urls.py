# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views
from rest_framework import routers

# from django.contrib.auth.decorators import login_required


app_name = 'listing'
urlpatterns = [
    path('api/', include('listing.api.urls')),
]
