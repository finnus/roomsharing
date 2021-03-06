from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


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
    owner = models.OneToOneField(
        "users.User", related_name="user_of_room", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})
