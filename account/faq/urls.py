from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<detail_id>',views.FAQDelete.as_view(),name="faq-delete"),
    path('', views.FAQListView.as_view(), name="faq"),
    path('create/', views.FAQCreate.as_view(), name="faq-create"),
    path('show/<int:pk>',views.FAQDetail.as_view(),name="faq-show"),
    path('update/<int:pk>', views.FAQUpdate.as_view(), name="faq-update"),
]
