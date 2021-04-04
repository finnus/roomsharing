from django.views.generic import DetailView, ListView

from .models import Room, RoomAptitude, RoomAmenity


class RoomDetailView(DetailView):
    model = Room
    template_name = "rooms/room_detail.html"

    def get_context_data(self, **kwargs):
        room = self.get_object().pk
        context = super().get_context_data(**kwargs)

        context["roomaptitudes"] = RoomAptitude.objects.filter(room=room).prefetch_related("room", "aptitude")
        context["roomamenities"] = RoomAmenity.objects.filter(room=room).prefetch_related("room", "amenity")

        return context


room_detail_view = RoomDetailView.as_view()


class RoomListView(ListView):
    model = Room
    template_name = "rooms/room_list.html"


room_list_view = RoomListView.as_view()
