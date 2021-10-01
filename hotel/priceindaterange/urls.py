from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
   path('create/<int:inv_id>', views.PriceinDateRangeCreate.as_view(), name="inventory-priceindaterange-create"),
   path('list/<int:inv_id>', views.PriceinDateRangeListView.as_view(), name="inventory-priceindaterange-list"),
   path('delete/<int:pk>', views.PriceinDateRangeDelete.as_view(), name="inventory-priceindaterange-delete"),
   path('update/<int:pk>', views.PriceinDateRangeUpdate.as_view(), name="inventory-priceindaterange-update"),

]
