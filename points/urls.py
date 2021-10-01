from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'points'
urlpatterns = [
	path('reward_point/', include('points.reward_point.urls')),
	path('credit_point/', include('points.credit_point.urls')),
	path('virtual_point/', include('points.virtual_point.urls')),
	path('api/', include('points.api.urls')),
	path('mem_plan/', include('points.membership_plan.urls')),
	path('point_setting/', include('points.point_setting.urls')),
]
