from django.views.generic import DetailView, ListView

from .models import Room


class RoomDetailView(DetailView):
    model = Room
    template_name = "rooms/room_detail.html"


room_detail_view = RoomDetailView.as_view()


class RoomListView(ListView):
    model = Room
    template_name = "rooms/room_list.html"


room_list_view = RoomListView.as_view()
