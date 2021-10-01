from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.PointSettingListView.as_view(), name="point-setting-index"),
	path('create/', views.PointSettingCreate.as_view(), name="point-setting-create"),
	# path('show/<int:pk>', views.CreditPointDetail.as_view(), name="credit-points-show"),
	path('update/<int:pk>', views.PointSettingUpdate.as_view(), name="point-setting-update"),
	path('delete/<pointsetting_id>', views.PointSettingDelete.as_view(), name="point-setting-delete"),

]
