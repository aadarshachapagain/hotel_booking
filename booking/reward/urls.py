from django.urls import path, include
from booking.reward import views

urlpatterns = [
	path('delete/<int:pk>', views.RewardDelete.as_view(), name="reward-delete"),
	path('', views.RewardView.as_view(), name="reward"),
	path('create/', views.RewardCreate.as_view(), name="reward-create"),
	path('show/<int:pk>', views.RewardDetail.as_view(), name="reward-show"),
	path('update/<int:pk>', views.RewardUpdate.as_view(), name="reward-update"),
]
