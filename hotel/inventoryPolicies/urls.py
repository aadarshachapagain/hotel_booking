from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('<inventory_id>', views.InventoryPoliciesList.as_view(), name='inventoryPolicies-list'),
	path('policySave/', views.InventoryPoliciesSave.as_view(), name='inventoryPolicies-save'),
	url(r'^(?P<model>\w+)/(?P<operation>\w+)/(?P<id>\d+)/(?P<inv_id>\d+)/$', views.InventoryPoliciesCreate.as_view(),
	    name='inventoryPolicies-create'),
]
