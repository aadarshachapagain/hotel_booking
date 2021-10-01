from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<int:pk>', views.LandmarkDelete.as_view(), name="landmark-delete"),
    path('', views.LandmarkListView.as_view(), name="landmark"),
    path('create/', views.LandmarkCreate.as_view(), name="landmark-create"),
    path('show/<int:pk>', views.LandmarkDetail.as_view(), name="landmark-show"),
    path('update/<int:pk>', views.LandmarkUpdate.as_view(), name="landmark-update"),
]
