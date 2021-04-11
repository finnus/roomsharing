from import_export import resources

from .models import Amenity, Aptitude, Room, RoomAmenity, RoomAptitude, RoomImage


class RoomResource(resources.ModelResource):
    class Meta:
        model = Room


class RoomAmenityResource(resources.ModelResource):
    class Meta:
        model = RoomAmenity


class RoomAptitudeResource(resources.ModelResource):
    class Meta:
        model = RoomAptitude


class AmenityResource(resources.ModelResource):
    class Meta:
        model = Amenity


class AptitudeResource(resources.ModelResource):
    class Meta:
        model = Aptitude


class RoomImageResource(resources.ModelResource):
    class Meta:
        model = RoomImage
