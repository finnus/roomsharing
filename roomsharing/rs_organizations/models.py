from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from organizations.abstract import (
    AbstractOrganization,
    AbstractOrganizationInvitation,
    AbstractOrganizationOwner,
    AbstractOrganizationUser,
)


class Organization(AbstractOrganization):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    email = models.EmailField(null=False, blank=False)
    phone = models.CharField(max_length=200, null=True, blank=True)
    contact_person = models.CharField(max_length=200, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = _("Organization")
        verbose_name_plural = _("Organizations")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("organizations:detail", kwargs={"pk": self.pk})


class OrganizationOwner(AbstractOrganizationOwner):
    pass


class OrganizationUser(AbstractOrganizationUser):
    pass


class OrganizationInvitation(AbstractOrganizationInvitation):
    pass
