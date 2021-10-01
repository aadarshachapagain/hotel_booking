from django.urls import path, include
from booking.points_on_sale import views

urlpatterns = [
	path('delete/<int:pk>', views.PointOnSaleDelete.as_view(), name="points_on_sale_delete"),
	path('', views.PointOnSaleListView.as_view(), name="points_on_sale_index"),
	path('create/', views.PointOnSaleCreate.as_view(), name="points_on_sale_create"),
	# path('show/<int:pk>', views.RewardDetail.as_view(), name="reward-show"),
	path('update/<int:pk>', views.PointOnSaleUpdate.as_view(), name="points_on_sale_index_update"),
]
