from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<int:pk>',views.CreditCardDelete.as_view(),name="credit-card-delete"),
    path('', views.CreditCardListView.as_view(), name="credit-card"),
    path('create/', views.CreditCardCreate.as_view(), name="credit-card-create"),
    path('show/<int:pk>',views.CreditCardDetail.as_view(),name="credit-card-show"),
    path('update/<int:pk>', views.CreditCardUpdate.as_view(), name="credit-card-update"),
]
