from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<int:pk>',views.extraBedPolicyDelete.as_view(),name="extraBedPolicy-delete"),
    path('deleteInv/<int:pk>',views.extraBedPolicyDeleteInv.as_view(),name="extraBedPolicy-delete-inv"),
    path('<item_id>', views.extraBedPolicyListView.as_view(), name="extraBedPolicy"),
    path('create/<item_id>', views.extraBedPolicyCreate.as_view(), name="extraBedPolicy-create"),
    # path('show/<int:pk>',views.BankDetailDetail.as_view(),name="bank-detail-show"),
    path('update/<int:pk>', views.extraBedPolicyUpdate.as_view(), name="extraBedPolicy-update"),
    path('updateInv/<int:pk>/<inventory_id>', views.extraBedPolicyUpdateInv.as_view(), name="extraBedPolicy-update-inv"),
]
