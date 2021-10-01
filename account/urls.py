from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from account.views import NormalUserLoginViewSet

# from hotel.owner.views import OwnerUpdate

# router = routers.DefaultRouter()
# router.register('userstore', NormalUserLoginViewSet)
# app_name = 'account'
urlpatterns = [
    # acis
    # path('', include(router.urls)),
    # path('api-token-auth/',obtain_auth_token,name='api-token-auth'),
    path('api/users/', include('account.api.urls')),
    path('faq/', include('account.faq.urls')),
    # path('api/users/', views.NormalUserLoginViewSet, name='account-create'),
    # ads

    path('signup/', views.signup, name="hotelowner_signup"),
    path('temp/', views.temp, name="temp"),
    path('travelowner/', views.signup, name="travelowner_signup"),
    # path('login/', views.login, name="login"),
    # path('staff/', views.StaffSignUpView.as_view(), name="hotelstaff_signup"),
    # path('travelstaff/', views.StaffSignUpView.as_view(), name="travelstaff_signup"),
    path('normaluser/', views.NormalUserSignUpView, name="normaluser_signup"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    # url(r'^normalactivate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.activate, name='activate'),
    path('ResetPassword/', views.reset_account_password, name="reset_account_password"),
    path('mass_active/', views.mass_active, name="mass_active"),
    path('user/', views.UserList, name="user_list"),
    path('user_active/<id>/<active>', views.UserActive, name="user_active"),
    path('update/<id>', views.UserUpdate, name="user_update"),
    path('find_account_type/<id>', views.find_account_type, name="find_account_type"),
    path('ownerprofile/', include('account.owner_profile.urls')),
    path('staffprofile/', include('account.staff_profile.urls')),
    path('language/', include('account.Language.urls')),
    path('bulkinvitation/', views.bulkinvitation, name="bulkinvitation"),
    path('uploadbulkemail/', views.uploadbulkemail, name="uploadbulkemail"),
    path('unsubscribe/', views.unsubscribe, name="unsubscribe"),
    path('agreement/', views.agreement, name="agreement"),


]
