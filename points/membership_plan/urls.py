from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('delete/<int:pk>', views.Membership_planDelete.as_view(), name="memplandelete"),
    path('', views.Membership_planListView.as_view(), name="memplanindex"),
    # path('show/<int:pk>', views.Membership_planDetail.as_view(), name="tourcompanyshow"),
    path('update/<int:pk>', views.Membership_planUpdate.as_view(), name="memplanupdate"),
    path('create/', views.Membership_planCreate.as_view(), name="memplancreate"),

]

