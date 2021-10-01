from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('<hotel_id>', views.BulkEditList.as_view(), name='bulkedit-list'),
    url(r'^(?P<model>\w+)/(?P<operation>\w+)/(?P<id>\d+)/$', views.BulkEditCreate.as_view(), name='bulkedit-create'),
    # url(r'^(?P<model>\w+)/(?P<id>\d+)/$', views.BulkEditCreate.as_view(), name='bulkedit-create'),
]
