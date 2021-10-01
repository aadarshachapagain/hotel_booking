
from django.contrib import admin
from django.urls import path, include
from hotel.CommissionPaymentPolicies import views

urlpatterns = [
    path('<item_id>', views.CommissionPaymentPoliciesListView.as_view(), name="commission-payment-policies"),
    path('create/<item_id>', views.CommissionPaymentPoliciesCreate.as_view(), name="commission-payment-policies-create"),
    path('delete/<int:pk>',views.CommissionPaymentPoliciesDelete.as_view(),name="commission-payment-policies-delete"),
]