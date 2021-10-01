from django.urls import path, include
from booking.customer import views

urlpatterns = [

    path('', views.CustomerListView.as_view(), name="customerindex"),
    path('create/', views.CustomerCreate.as_view(), name="customercreate"),
    path('update/<int:pk>', views.CustomerUpdate.as_view(), name="customerupdate"),
    path('delete/<pk>', views.CustomerDelete.as_view(), name="customerdelete"),

]
