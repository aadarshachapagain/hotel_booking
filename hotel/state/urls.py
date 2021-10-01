from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<State_id>',views.StateDelete.as_view(),name="State-delete"),
    path('', views.StateListView.as_view(), name="State"),
    path('create/', views.StateCreate.as_view(), name="State-create"),
    path('show/<int:pk>',views.StateDetail.as_view(),name="State-show"),
    path('update/<int:pk>', views.StateUpdate.as_view(), name="State-update"),
]
