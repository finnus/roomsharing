from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from roomsharing.rs_organizations.models import Organization


class Room(models.Model):
    # characteristics of the room
    name = models.CharField(_("Name"), max_length=200)
    description = models.TextField(_("Description"), max_length=4000)
    capacity_from = models.IntegerField(_("Capacity from"), default=10)
    capacity_to = models.IntegerField(_("Capacity to"), default=15)
    square_meters = models.IntegerField(_("Square Meters"), null=True, blank=True)
    rules = models.TextField(_("Square Meters"), max_length=2000, blank=True, null=True)
    published = models.BooleanField(_("Published"), default=False)
    # relations
    owner_organization = models.ForeignKey(
        Organization,
        related_name="rooms_of_organization",
        related_query_name="room_of_organization",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")
        unique_together = [["name", "owner_organization"]]


class Aptitude(models.Model):
    name = models.CharField(_("Name"), max_length=30, unique=True)
    description = models.CharField(_("Description"), max_length=200)
    icon = models.CharField(_("Icon"), max_length=25, default="bi-question-circle")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Aptitude")
        verbose_name_plural = _("Aptitudes")


class RoomAptitude(models.Model):
    room = models.ForeignKey(
        Room,
        related_name="roomaptitudes_of_room",
        related_query_name="roomaptitude_of_room",
        on_delete=models.CASCADE,
    )
    aptitude = models.ForeignKey(
        Aptitude,
        related_name="roomaptitudes_of_aptitude",
        related_query_name="roomaptitude_of_aptitude",
        on_delete=models.PROTECT,
    )
    specification = models.CharField(_("Specification"), max_length=400)

    def __str__(self):
        return self.room.name + ": " + self.aptitude.name

    class Meta:
        verbose_name = _("Room Aptitude")
        verbose_name_plural = _("Room Aptitudes")
        unique_together = [["room", "aptitude"]]


class Amenity(models.Model):
    name = models.CharField(_("Name"), max_length=30)
    description = models.CharField(_("Description"), max_length=200)
    icon = models.CharField(_("Icon"), max_length=25, default="bi-question-circle")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Amenity")
        verbose_name_plural = _("Amenities")


class RoomAmenity(models.Model):
    room = models.ForeignKey(
        Room,
        related_name="roomamenities_of_room",
        related_query_name="roomamenity_of_room",
        on_delete=models.CASCADE,
    )
    amenity = models.ForeignKey(
        Amenity,
        related_name="roomamenities_of_amenity",
        related_query_name="roomamenity_of_aptitude",
        on_delete=models.PROTECT,
    )
    specification = models.CharField(_("Specification"), max_length=400)

    def __str__(self):
        return self.room.name + ": " + self.amenity.name

    class Meta:
        verbose_name = _("Room Amenity")
        verbose_name_plural = _("Room Amenities")
        unique_together = [["room", "amenity"]]
