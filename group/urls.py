# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from group import views
from . import views
from rest_framework import routers

# from django.contrib.auth.decorators import login_required


app_name = 'group'
urlpatterns = [
    path('create/', views.GroupCreate.as_view(), name='group-create'),
    path('', views.GroupList.as_view(), name='group-index'),
    path('delete/<detail_id>', views.GroupDelete.as_view(), name="group-delete"),
    path('update/<int:pk>', views.GroupUpdate.as_view(), name="group-update"),
]
