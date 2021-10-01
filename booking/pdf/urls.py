from . import views
from rest_framework import routers
from django.urls import path, include

urlpatterns = [
    path('pdf/<int:id>', views.GeneratePdf.as_view(), name='pdf'),
]