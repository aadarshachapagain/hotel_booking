
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
  
    path('delete/<owner_id>',views.OwnerDelete.as_view(),name="ownerdelete"),
    path('', views.OwnerListView.as_view(), name="ownerindex"), 
    path('create/', views.OwnerCreate.as_view(), name="ownercreate"),
    path('show/<int:pk>',views.OwnerDetail.as_view(),name="ownershow"),
    path('update/<int:pk>', views.OwnerUpdate.as_view(), name="ownerupdate"),

]