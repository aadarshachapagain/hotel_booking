from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<detail_id>',views.B2BDelete.as_view(),name="b2b-delete"),
    path('', views.B2BListView.as_view(), name="b2b"),
    path('create/', views.B2BCreate.as_view(), name="b2b-create"),
    # path('show/<int:pk>',views.BankDetailDetail.as_view(),name="bank-detail-show"),
    path('update/<int:pk>', views.B2BUpdate.as_view(), name="b2b-update"),
]
