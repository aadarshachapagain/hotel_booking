
from django.urls import path, include
from hotel.roomFacilityAssign import views

urlpatterns = [
  
    path('delete/<int:pk>',views.RoomFacilityAssignDelete.as_view(),name="room-facility-assign-delete"),
    path('<item_id>', views.RoomFacilityAssignListView.as_view(), name="room-facility-assign-index"),
    path('create/<item_id>', views.RoomFacilityAssignCreate.as_view(), name="room-facility-assign-create"),

]