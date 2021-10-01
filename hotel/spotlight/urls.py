from django.contrib import admin
from django.urls import path, include
from hotel.spotlight import views

urlpatterns = [

    path('delete/<id>', views.SpotLightDelete.as_view(), name="spotlightdelete"),
    path('', views.SpotLightListView.as_view(), name="spotlightindex"),
    # path('show/<int:pk>',views.AddressDetail.as_view(),name="spotlightshow"),
    path('update/<int:pk>', views.SpotLightUpdate.as_view(), name="spotlightupdate"),
    path('create/', views.SpotLightCreate.as_view(), name="spotlightcreate"),

]
