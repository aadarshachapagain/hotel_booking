from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<int:pk>',views.childSupplementDelete.as_view(),name="childSupplement-delete"),
    path('deleteInv/<int:pk>',views.childSupplementDeleteInv.as_view(),name="childSupplement-delete-inv"),
    path('<item_id>', views.childSupplementListView.as_view(), name="childSupplement"),
    path('create/<item_id>', views.childSupplementCreate.as_view(), name="childSupplement-create"),
    # path('show/<int:pk>',views.BankDetailDetail.as_view(),name="bank-detail-show"),
    path('update/<int:pk>', views.childSupplementUpdate.as_view(), name="childSupplement-update"),
    path('updateInv/<int:pk>/<inventory_id>', views.childSupplementUpdateInv.as_view(), name="childSupplement-update-inv"),
]
