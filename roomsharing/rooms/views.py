from django.views.generic import DetailView
from django_filters.views import FilterView

from .filters import RoomFilter
from .models import Room, RoomAmenity, RoomAptitude, RoomImage


class RoomDetailView(DetailView):
    model = Room
    template_name = "rooms/room_detail.html"

    def get_context_data(self, **kwargs):
        room = self.get_object().pk
        context = super().get_context_data(**kwargs)

        context["roomaptitudes"] = RoomAptitude.objects.filter(
            room=room
        ).prefetch_related("room", "aptitude")
        context["roomamenities"] = RoomAmenity.objects.filter(
            room=room
        ).prefetch_related("room", "amenity")
        context["roomimages"] = RoomImage.objects.filter(room=room).prefetch_related(
            "room"
        )

        return context


room_detail_view = RoomDetailView.as_view()


class RoomListView(FilterView):
    model = Room
    template_name = "rooms/room_list.html"
    filterset_class = RoomFilter


room_list_view = RoomListView.as_view()
