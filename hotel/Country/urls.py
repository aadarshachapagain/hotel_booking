from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<country_id>',views.CountryDelete.as_view(),name="country-delete"),
    path('', views.CountryListView.as_view(), name="country"),
    path('create/', views.CountryCreate.as_view(), name="country-create"),
    path('show/<int:pk>',views.CountryDetail.as_view(),name="country-show"),
    path('update/<int:pk>', views.CountryUpdate.as_view(), name="country-update"),
]
