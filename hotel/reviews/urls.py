from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('delete/<HotelReview_id>',views.HotelReviewDelete.as_view(),name="HotelReview-delete"),
    path('', views.HotelReviewList.as_view(), name="HotelReview"), 
    path('create/', views.HotelReviewCreate.as_view(), name="HotelReview-create"),
    path('show/<int:pk>',views.HotelReviewDetail.as_view(),name="HotelReview-show"),
    path('update/<int:pk>', views.HotelReviewUpdate.as_view(), name="HotelReview-update"),

]