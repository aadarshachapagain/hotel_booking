
from django.contrib import admin
from django.urls import path, include
from account.owner_profile import views

urlpatterns = [
  
    path('delete/<owner_id>',views.OwnerDelete.as_view(),name="ownerprofiledelete"),
    path('', views.OwnerListView.as_view(), name="ownerprofileindex"),
    path('create/', views.OwnerCreate.as_view(), name="ownerprofilecreate"),
    path('show/<int:pk>',views.OwnerDetail.as_view(),name="ownerprofileshow"),
    path('update/<int:pk>', views.OwnerUpdate.as_view(), name="ownerprofileupdate"),
    path('downloadId/', views.downloadId, name="download-Id"),
    # path('pdf_view/', views.pdf_view, name="pdf_view"),

]