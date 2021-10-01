from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<int:pk>',views.cribsPolicyDelete.as_view(),name="cribsPolicy-delete"),
    path('deleteInv/<int:pk>',views.cribsPolicyDeleteInv.as_view(),name="cribsPolicy-delete-inv"),
    path('<item_id>', views.cribsPolicyListView.as_view(), name="cribsPolicy"),
    path('create/<item_id>', views.cribsPolicyCreate.as_view(), name="cribsPolicy-create"),
    # path('show/<int:pk>',views.BankDetailDetail.as_view(),name="bank-detail-show"),
    path('update/<int:pk>', views.cribsPolicyUpdate.as_view(), name="cribsPolicy-update"),
    path('updateInv/<int:pk>/<inventory_id>', views.cribsPolicyUpdateInv.as_view(), name="cribsPolicy-update-inv"),
]
