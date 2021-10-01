from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.BusinessCashBonusListView.as_view(), name="business-cash-bonus-index"),
	path('create/', views.BusinessCashBonusCreate.as_view(), name="business-cash-bonus-create"),
	# path('show/<int:pk>', views.VirtualPointDetail.as_view(), name="virtual-points-show"),
	path('update/<int:pk>', views.BusinessCashBonusUpdate.as_view(), name="business-cash-bonus-update"),
	path('delete/<virtual_id>', views.BusinessCashBonusDelete.as_view(), name="business-cash-bonus-delete"),

]
