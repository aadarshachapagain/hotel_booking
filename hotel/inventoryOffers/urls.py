from django.urls import path, include
from . import views

urlpatterns = [
    path('delete/<inventory_offer_id>', views.InventoryOffersDelete.as_view(), name="inventory-offers-delete"),
    path('<hotel_id>', views.InventoryOffersListView.as_view(), name="inventory-offers-index"),
    path('create/<hotel_id>', views.InventoryOffersCreate.as_view(), name="inventory-offers-create"),
    path('show/<int:pk>', views.InventoryOffersDetail.as_view(), name="inventory-offers-show"),
    path('update/<int:pk>', views.InventoryOffersUpdate.as_view(), name="inventory-offers-update"),


]