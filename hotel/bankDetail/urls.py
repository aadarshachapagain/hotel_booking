from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<detail_id>',views.BankDetailDelete.as_view(),name="bank-detail-delete"),
    path('<hotel_id>', views.BankDetailListView.as_view(), name="bank-detail"),
    path('create/<hotel_id>', views.BankDetailCreate.as_view(), name="bank-detail-create"),
    # path('show/<int:pk>',views.BankDetailDetail.as_view(),name="bank-detail-show"),
    path('update/<int:pk>', views.BankDetailUpdate.as_view(), name="bank-detail-update"),
]
