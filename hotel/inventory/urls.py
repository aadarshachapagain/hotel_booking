from django.contrib import admin
from django.urls import path, include
from . import views
from . import priceviews

# from . import viewshotelinv

urlpatterns = [
    # class based view
    path('delete/<inv_id>', views.InventoryDelete.as_view(), name="hotelinvdelete"),
    path('<int:hotel_id>', views.InventoryListView.as_view(), name="hotelinv-index"),
    path('create/<int:hotel_id>', views.InventoryCreate.as_view(), name="hotelinvcreate"),
    path('show/<int:pk>', views.InventoryDetail.as_view(), name="showinvdetail"),
    path('update/<int:pk>', views.InventoryUpdate.as_view(), name="hotelinvupdate"),
    path('admininvapproval', views.toapproveinv, name="invapprovehotel"),
    path('invapprovalpreview/<item_id>', views.invapprovalpreview, name="invapprovalpreview"),
    path('invapproveddone/<item_id>', views.invapproveddone, name="invapproveddone"),
    path('mass_approve_inv/', views.mass_approve, name="mass_approve_inv"),
    path('addonservices/', include('hotel.addonservices.urls')),
    path('price/', include('hotel.priceOfRoom.urls')),
    path('priceindaterange/', include('hotel.priceindaterange.urls')),
    path('defaultprice/<int:pk>', views.DefaultPriceUpdate.as_view(), name="defaultpriceofroom"),
    path('roomfeatures/', views.RoomFeatures.as_view(), name="roomfeatures"),
    path('cloneinventory/', views.cloneInventory, name="cloneinventory"),
]
