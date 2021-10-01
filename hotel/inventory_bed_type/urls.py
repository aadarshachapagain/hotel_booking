
from django.contrib import admin
from django.urls import path, include
from hotel.inventory_bed_type import views

urlpatterns = [
  
    path('delete/<include_id>',views.Inventory_Bed_TypeDelete.as_view(),name="inv-bed-type-delete"),
    path('<item_id>', views.Inventory_Bed_TypeListView.as_view(), name="inv-bed-type-index"),
    path('show/<int:pk>',views.Inventory_Bed_TypeDetail.as_view(),name="inv-bed-type-show"),
    path('update/<int:pk>', views.Inventory_Bed_TypeUpdate.as_view(), name="inv-bed-type-update"),
    path('create/<item_id>', views.Inventory_Bed_TypeCreate.as_view(), name="inv-bed-type-create"),

]