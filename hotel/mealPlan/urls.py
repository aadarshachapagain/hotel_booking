from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('delete/<detail_id>', views.MealPlanDelete.as_view(), name="MealPlan-delete"),
    path('', views.MealPlanListView.as_view(), name="MealPlan"),
    path('create/', views.MealPlanCreate.as_view(), name="MealPlan-create"),
    path('update/<int:pk>', views.MealPlanUpdate.as_view(), name="MealPlan-update"),
]
