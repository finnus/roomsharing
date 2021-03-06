from django.contrib import admin
from django.db import models
from import_export.admin import ImportExportModelAdmin
from markdownx.widgets import AdminMarkdownxWidget

from .models import Amenity, Aptitude, Room, RoomAmenity, RoomAptitude, RoomImage


class RoomImageInline(admin.TabularInline):
    model = RoomImage


class RoomAptitudeInline(admin.TabularInline):
    model = RoomAptitude


class RoomAmenityInline(admin.TabularInline):
    model = RoomAmenity


@admin.register(Room)
class RoomAdmin(ImportExportModelAdmin):
    inlines = [RoomAptitudeInline, RoomAmenityInline, RoomImageInline]

    formfield_overrides = {
        models.TextField: {"widget": AdminMarkdownxWidget},
    }


@admin.register(Aptitude)
class AptitudeAdmin(ImportExportModelAdmin):
    pass


@admin.register(RoomAptitude)
class RoomAptitude(ImportExportModelAdmin):
    pass


@admin.register(Amenity)
class AmenityAdmin(ImportExportModelAdmin):
    pass


@admin.register(RoomAmenity)
class RoomAmenityAdmin(ImportExportModelAdmin):
    pass


@admin.register(RoomImage)
class RoomImageAdmin(ImportExportModelAdmin):
    pass
