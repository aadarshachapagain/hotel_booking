
from django.contrib import admin
from django.urls import path, include
from hotel.PaymentPolicies import views

urlpatterns = [
    path('<item_id>', views.PaymentPoliciesListView.as_view(), name="payment-policies"),
    path('create/<item_id>', views.PaymentPoliciesCreate.as_view(), name="payment-policies-create"),
    path('delete/<int:pk>',views.PaymentPoliciesDelete.as_view(),name="payment-policies-delete"),
]