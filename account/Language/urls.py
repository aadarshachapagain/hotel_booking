from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<country_id>',views.LanguageDelete.as_view(),name="language-delete"),
    path('', views.LanguageListView.as_view(), name="language"),
    path('create/', views.LanguageCreate.as_view(), name="language-create"),
    path('show/<int:pk>',views.LanguageDetail.as_view(),name="language-show"),
    path('update/<int:pk>', views.LanguageUpdate.as_view(), name="language-update"),
]
