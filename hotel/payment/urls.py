from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('incoming_payments/', views.incomingPayment, name="incomingPayments"),
    path('incoming_payment_json/', views.incomingPayment_json, name="incomingPayment_json"),
    path('incoming_payments/<bookingConfirmation>', views.single_incoming_payments, name="single_incoming_payment"),
    path('outgoing_payments/', views.get_outgoing_payments, name="outgoing_payment"),
    path('outgoing_payment_json/', views.get_outgoing_payments_json, name="outgoingPayment_json"),
    path('outgoing_payments/<OutgoingPaymentId>', views.single_outgoing_payments, name="single_outgoing_payment"),
    path('dropzone/', views.renderdropzone, name="renderdropzone"),
    path('dropzoneuploads/', views.dropzoneuploads, name="dropzoneuploads"),

    # path('', views.CreditCardListView.as_view(), name="credit-card"),
    # path('create/', views.CreditCardCreate.as_view(), name="credit-card-create"),
    # path('show/<int:pk>',views.CreditCardDetail.as_view(),name="credit-card-show"),
    # path('update/<int:pk>', views.CreditCardUpdate.as_view(), name="credit-card-update"),
]
