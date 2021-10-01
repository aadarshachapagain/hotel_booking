from django.urls import path, include
from . import views

urlpatterns = [
	
	path('delete/<leader_id>', views.BusinessPartnersDelete.as_view(), name="business-partners-delete"),
	path('', views.BusinessPartnersListView.as_view(), name="business-partners-index"),
	path('update/<int:pk>', views.BusinessPartnersUpdate.as_view(), name="business-partners-update"),
	path('create/', views.BusinessPartnersCreate.as_view(), name="business-partners-create"),
	path('show/<int:pk>',views.BusinessPartnersDetail.as_view(),name="business-partners-show"),
]
