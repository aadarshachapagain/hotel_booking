from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.RewardPointListView.as_view(), name="reward-points-index"),
	path('create/', views.RewardPointCreate.as_view(), name="reward-points-create"),
	# path('show/<int:pk>', views.RewardPointDetail.as_view(), name="reward-points-show"),
	path('update/<int:pk>', views.RewardPointUpdate.as_view(), name="reward-points-update"),
	path('delete/<reward_id>', views.RewardPointDelete.as_view(), name="reward-points-delete"),

]
