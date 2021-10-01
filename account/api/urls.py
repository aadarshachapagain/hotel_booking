from . import views
from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from account.api.views import UserCreateAPIView, UserPasswordResetAPIView, UserPasswordChangeAPIView
from account.api.views import UserLoginAPIView
from account.api import views

urlpatterns = [
	path('login/', UserLoginAPIView.as_view(), name='user_login'),
	path('register/', UserCreateAPIView.as_view(), name='user_register'),
	path('resetPassword/', UserPasswordResetAPIView.as_view(), name='user_password_reset'),
	path('changePassword/', UserPasswordChangeAPIView.as_view(), name='user_password_change'),
	path('fireBaseRegister/', views.fireBaseRegister, name='fireBaseRegister'),
	path('fireBaseLogin/', views.fireBaseLogin, name='fireBaseLogin'),
	path('faqAPI/', views.faqAPI, name='faqAPI'),
	path('ownerProfile/', views.ownerProfile, name='ownerProfile'),


]
