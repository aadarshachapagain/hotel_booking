from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<detail_id>', views.SimilarSystemsDelete.as_view(), name="SimilarSystems-delete"),
    path('', views.SimilarSystemsListView.as_view(), name="SimilarSystems"),
    path('create/', views.SimilarSystemsCreate.as_view(), name="SimilarSystems-create"),
    path('update/<int:pk>', views.SimilarSystemsUpdate.as_view(), name="SimilarSystems-update"),
    path('byvendor/', views.byvendor, name="SimilarSystems-byvendor"),
]
