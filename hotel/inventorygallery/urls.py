
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<inv_id>', views.index, name="inventorygallery"),
    path('create/<item_id>', views.create,name="inventorygallery-create"),
    path('gallery/<item_id>', views.indexlist,name="inventorygallery-indexlist"),
    path('store/', views.store, name="inventorygallery-store"),
    path('update/<item_id>', views.update, name="inventorygallery-update"),
    path('edit/<item_id>',views.edit,name="inventorygallery-edit"),
    path('editsingle/<item_id>',views.editsingle,name="inventorygallery-editsingle"),
    path('show/<item_id>',views.show,name="inventorygallery-show"),
    path('delete/<item_id>',views.delete,name="inventorygallery-delete"),

]
