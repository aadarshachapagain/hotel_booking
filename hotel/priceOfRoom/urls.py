from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('create/<int:inv_id>', views.PriceOfDiffSystemCreate.as_view(), name="inventory-price-create"),
    path('list/<int:inv_id>', views.PriceOfDiffSystemListView.as_view(), name="inventory-price-list"),
    path('delete/<int:pk>', views.PriceOfDiffSystemDelete.as_view(), name="inventory-price-delete"),
    path('update/<int:pk>', views.PriceOfDiffSystemUpdate.as_view(), name="inventory-price-update"),
    path('new/<inv_id>', views.PriceOfRoom.as_view(), name="room-price-create"),


]
