from django.urls import path

from roomsharing.rooms.views import room_detail_view, room_list_view

app_name = "rooms"
urlpatterns = [
    path("", room_list_view, name="list"),
    path("<int:pk>/", room_detail_view, name="detail"),
]
