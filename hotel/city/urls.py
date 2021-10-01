from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<city_id>',views.CityDelete.as_view(),name="city-delete"),
    path('', views.CityListView.as_view(), name="city"),
    path('create/', views.CityCreate.as_view(), name="city-create"),
    path('show/<int:pk>',views.CityDetail.as_view(),name="city-show"),
    path('update/<int:pk>', views.CityUpdate.as_view(), name="city-update"),
    # path('update/getstate/', views.getstate, name="getstate"),
]
