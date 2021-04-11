from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from organizations.base_admin import (
    BaseOrganizationAdmin,
    BaseOrganizationOwnerAdmin,
    BaseOrganizationUserAdmin,
    BaseOwnerInline,
)

from .models import Organization, OrganizationOwner, OrganizationUser


class OwnerInline(BaseOwnerInline):
    model = OrganizationOwner


@admin.register(Organization)
class OrganizationAdmin(BaseOrganizationAdmin, ImportExportModelAdmin):
    inlines = [OwnerInline]


@admin.register(OrganizationUser)
class OrganizationUserAdmin(BaseOrganizationUserAdmin, ImportExportModelAdmin):
    pass


@admin.register(OrganizationOwner)
class OrganizationOwnerAdmin(BaseOrganizationOwnerAdmin, ImportExportModelAdmin):
    pass
