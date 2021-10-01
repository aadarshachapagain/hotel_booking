from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.CreditPointListView.as_view(), name="credit-points-index"),
	path('create/', views.CreditPointCreate.as_view(), name="credit-points-create"),
	# path('show/<int:pk>', views.CreditPointDetail.as_view(), name="credit-points-show"),
	path('update/<int:pk>', views.CreditPointUpdate.as_view(), name="credit-points-update"),
	path('delete/<credit_id>', views.CreditPointDelete.as_view(), name="credit-points-delete"),

]
