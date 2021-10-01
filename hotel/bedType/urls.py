from django.urls import path, include
from django.conf.urls import url
from hotel.bedType import views

urlpatterns = [
	path('delete/<bed_id>', views.BedTypeDelete.as_view(), name="bed-type-delete"),
	path('', views.BedTypeListView.as_view(), name="bed-type"),
	path('create/', views.BedTypeCreate.as_view(), name="bed-type-create"),
	path('show/<int:pk>', views.BedTypeDetail.as_view(), name="bed-type-show"),
	path('update/<int:pk>', views.BedTypeUpdate.as_view(), name="bed-type-update"),
]
