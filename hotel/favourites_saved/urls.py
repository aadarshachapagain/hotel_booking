# from django.contrib import admin
# from django.urls import path, include
# from . import views
#
# urlpatterns = [
#
#     path('delete/<address_id>', views.AddressDelete.as_view(), name="addressdelete"),
#     path('', views.AddressListView.as_view(), name="addressindex"),
#     # path('create/', views.AddressCreate.as_view(), name="addresscreate"),
#     path('show/<int:pk>', views.AddressDetail.as_view(), name="addressshow"),
#     path('update/<int:pk>', views.AddressUpdate.as_view(), name="addressupdate"),
#     # path('getdistance/',views.getDistance, name="getdistance"),
#     path('create/<item_id>', views.AddressCreate.as_view(), name="addresscreate"),
#     # For Ajax call to get data
#     path('update/getstate/', views.getstate, name="getstate"),
#     path('update/getcity/', views.getcity, name="getcity"),
#     path('update/getCountryPhone/', views.getCountryPhone, name="getCountryPhone"),
#     path('addlandmark/<address_id>', views.addlandmark, name="addlandmark"),
#     path('map', views.map, name="map"),
# ]
