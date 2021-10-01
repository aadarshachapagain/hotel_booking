from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<int:pk>',views.specialRequestDelete.as_view(),name="specialRequest-delete"),
    # nisham suggested that special request are assigned by admin not vendor 03/24/2020
    # path('<item_id>', views.specialRequestListView.as_view(), name="specialRequest"),
    # path('create/<item_id>', views.specialRequestCreate.as_view(), name="specialRequest-create"),
    
    path('', views.specialRequestListView.as_view(), name="specialRequest"),
    path('create/', views.specialRequestCreate.as_view(), name="specialRequest-create"),
    path('update/<int:pk>', views.specialRequestUpdate.as_view(), name="specialRequest-update"),
]
