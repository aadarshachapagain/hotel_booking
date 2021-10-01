"""travel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

import travel
from account import views
from travel.utils import croppedImagePreview
from travel.views import dashboard, error, termsandconditions, checkEmail, forbidden
from travel.views import current_module
from travel.views import check_login
from django.contrib.auth.views import LoginView
import travel

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('user/', include('users.urls')),
    path('hotel/', include('hotel.urls')),
    # path('travel_tour/', include('travel_tour.urls')),
    # path('rental/', include('rental.urls')),
    # path('restaurant/', include('restaurant.urls')),
    path('booking/', include('booking.urls')),
    path('points/', include('points.urls')),

    # path('hotel/', include('hotel.urls',namespace='hotel')),
    path('account/', include('account.urls')),
    path('system/', include('django.contrib.auth.urls')),
    path('address/', include('users.urlsaddress')),
    path('reverify/', views.linktoverification, name="reverify"),
    path('reverifyadmin/', views.linktoverificationadmin, name="reverifyadmin"),
    path('checkfcm/', views.tochoice, name="choice"),
    # path('', views.tochoice, name="choice"),
    path('login/', LoginView.as_view(), name='login'),
    # path('login/', check_login, name='login'),
    path('', check_login, name='check_login'),
    path('myCropper/', croppedImagePreview, name='check_login'),
    path('dashboard', dashboard, name="dashboard"),
    path('404', error, name="404"),
    path('403', forbidden, name="403"),
    path('termsandconditions', termsandconditions, name="termsandconditions"),
    path('checkEmail', checkEmail, name="checkEmail"),
    path('current_module/<module_name>', current_module, name="current_module"),
    # path('blog/', include('blog.urls')),

    url(r'session_security/', include('session_security.urls')),
    # url(r'^api/login/', include('rest_social_auth.urls_token'), name='my'),
    # url(r'^api/login/', include('rest_social_auth.urls_session')),
    # path('admindashboard/', current_module, name="current_module"),

    path('listing/', include('listing.urls')),
    path('groups/', include('group.urls')),

    # path('check/', views.custom_reset_password, name="custom_reset_password"),
    path('propertyDetail/', include('hotel.propertyDetail.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = travel.views.handler404
handler403 = travel.views.handler403
