# from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from group import views
from . import views
from rest_framework import routers

# from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('create/', views.PropertyDetailCreateView.as_view(), name="PropertyDetail-create"),
    path('', views.PropertyDetailListView.as_view(), name="PropertyDetail"),
    # path('delete/<detail_id>', views.GroupDelete.as_view(), name="group-delete"),
    path('update/<int:pk>', views.PropertyDetailUpdate.as_view(), name="PropertyDetail-update"),
    path('init/', views.OwnerNPropertyDetailView.as_view(), name="OwnerNPropertyDetail"),
    path('show/<int:pk>', views.PropertyDetailShow.as_view(), name="PropertyDetail-show"),
    path('proplist/', views.PropList, name="proplist"),
    path('verify_prop/<item_id>', views.verify_single_prop, name="verify_prop"),
    path('prop_status/<item_id>/<status>', views.change_prop_status, name="prop_status"),
    path('pdf_view/<prop_id>/<type>', views.pdf_view, name="pdf_view")
]
