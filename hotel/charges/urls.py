from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<detail_id>',views.ChargesDelete.as_view(),name="charges-delete"),
    path('', views.ChargesListView.as_view(), name="charges"),
    path('create/', views.ChargesCreate.as_view(), name="charges-create"),
    path('update/<int:pk>', views.ChargesUpdate.as_view(), name="charges-update"),
]
