from django.contrib import admin

from .models import Amenity, Aptitude, Room, RoomAmenity, RoomAptitude


class RoomAptitudeInline(admin.TabularInline):
    model = RoomAptitude


class RoomAmenityInline(admin.TabularInline):
    model = RoomAmenity


class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomAptitudeInline, RoomAmenityInline]


admin.site.register(Room, RoomAdmin)
admin.site.register(Aptitude)
admin.site.register(RoomAptitude)
admin.site.register(Amenity)
admin.site.register(RoomAmenity)
