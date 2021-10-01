from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('create/<int:hotel_id>', views.GroupRateCreate.as_view(), name="GroupRate-create"),
    path('<item_id>', views.GroupRateListView.as_view(), name="GroupRate"),
    path('update/<int:pk>', views.GroupRateUpdate.as_view(), name="GroupRate-update"),
    path('delete/<int:pk>', views.GroupRateDelete.as_view(), name="GroupRate-delete"),

]
