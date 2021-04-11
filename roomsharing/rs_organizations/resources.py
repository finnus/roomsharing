from import_export import resources

from .models import (
    Organization,
    OrganizationInvitation,
    OrganizationOwner,
    OrganizationUser,
)


class OrganizationResource(resources.ModelResource):
    class Meta:
        model = Organization


class OrganizationOwnerResource(resources.ModelResource):
    class Meta:
        model = OrganizationOwner


class OrganizationUserResource(resources.ModelResource):
    class Meta:
        model = OrganizationUser


class OrganizationInvitationResource(resources.ModelResource):
    class Meta:
        model = OrganizationInvitation
