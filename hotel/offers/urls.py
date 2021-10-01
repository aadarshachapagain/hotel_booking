from django.urls import path, include
from hotel.offers import views

urlpatterns = [
    path('delete/<offer_id>', views.OffersDelete.as_view(), name="offers-delete"),
    path('mass_delete/', views.mass_delete, name="offers-mass-delete"),
    path('', views.OffersListView.as_view(), name="offers-index"),
    path('create/', views.OffersCreate.as_view(), name="offers-create"),
    path('show/<int:pk>', views.OffersDetail.as_view(), name="offers-show"),
    path('update/<int:pk>', views.OffersUpdate.as_view(), name="offers-update"),
]