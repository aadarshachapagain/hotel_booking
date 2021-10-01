
from django.contrib import admin
from django.urls import path, include
from hotel.cancellation_policy import views

urlpatterns = [
  
    path('test', views.getCancellationPolicy.as_view(), name="test"),
    path('delete/<include_id>',views.Cancellation_PolicyDelete.as_view(),name="canceldelete"),
    path('<item_id>', views.Cancellation_PolicyListView.as_view(), name="cancelindex"),
    path('show/<int:pk>',views.Cancellation_PolicyDetail.as_view(),name="cancelshow"),
    path('update/<int:pk>', views.Cancellation_PolicyUpdate.as_view(), name="cancelupdate"),
    path('updateInv/<int:pk>/<inventory_id>', views.Cancellation_PolicyUpdateInv.as_view(), name="cancelupdateInv"),
    path('deleteInv/<int:pk>',views.Cancellation_PolicyDeleteInv.as_view(),name="canceldeleteInv"),
    path('create/<item_id>', views.Cancellation_PolicyCreate.as_view(), name="cancelcreate"),
    # path('manyupdateinclude/<item_id>', views.includemanyupdate, name="includemanyupdate"),
    path('updateinclude', views.updateinclude, name="cancelupdatesingle"),
    path('editsinglecancel/<item_id>', views.editsingle, name="canceleditsingle"),

]