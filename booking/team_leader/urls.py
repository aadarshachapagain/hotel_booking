from django.urls import path, include
from . import views

urlpatterns = [
	
	path('delete/<leader_id>', views.TeamLeaderDelete.as_view(), name="team-leader-delete"),
	path('', views.TeamLeaderListView.as_view(), name="team-leader-index"),
	path('update/<int:pk>', views.TeamLeaderUpdate.as_view(), name="team-leader-update"),
	path('create/', views.TeamLeaderCreate.as_view(), name="team-leader-create"),
	# path('show/<int:pk>',views.TeamLeaderDetail.as_view(),name="tourcompanyshow"),
]
