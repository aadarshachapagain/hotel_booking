from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.VirtualPointListView.as_view(), name="virtual-points-index"),
	path('create/', views.VirtualPointCreate.as_view(), name="virtual-points-create"),
	# path('show/<int:pk>', views.VirtualPointDetail.as_view(), name="virtual-points-show"),
	path('update/<int:pk>', views.VirtualPointUpdate.as_view(), name="virtual-points-update"),
	path('delete/<virtual_id>', views.VirtualPointDelete.as_view(), name="virtual-points-delete"),

]
