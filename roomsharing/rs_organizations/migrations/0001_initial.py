# Generated by Django 3.0.12 on 2021-04-11 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import organizations.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "created",
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified",
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "slug",
                    organizations.fields.SlugField(
                        blank=True,
                        editable=False,
                        help_text="The name in all lowercase, suitable for URL identification",
                        max_length=200,
                        populate_from="name",
                        unique=True,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(max_length=4000)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "contact_person",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("website", models.URLField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Organization",
                "verbose_name_plural": "Organizations",
            },
        ),
        migrations.CreateModel(
            name="OrganizationUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified",
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("is_admin", models.BooleanField(default=False)),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization_users",
                        to="rs_organizations.Organization",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rs_organizations_organizationuser",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "organization user",
                "verbose_name_plural": "organization users",
                "ordering": ["organization", "user"],
                "abstract": False,
                "unique_together": {("user", "organization")},
            },
        ),
        migrations.CreateModel(
            name="OrganizationOwner",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified",
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "organization",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="owner",
                        to="rs_organizations.Organization",
                    ),
                ),
                (
                    "organization_user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rs_organizations.OrganizationUser",
                    ),
                ),
            ],
            options={
                "verbose_name": "organization owner",
                "verbose_name_plural": "organization owners",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrganizationInvitation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("guid", models.UUIDField(editable=False)),
                (
                    "invitee_identifier",
                    models.CharField(
                        help_text="The contact identifier for the invitee, email, phone number, social media handle, etc.",
                        max_length=1000,
                    ),
                ),
                (
                    "created",
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "modified",
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "invited_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rs_organizations_organizationinvitation_sent_invitations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "invitee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rs_organizations_organizationinvitation_invitations",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="organization_invites",
                        to="rs_organizations.Organization",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="organization",
            name="users",
            field=models.ManyToManyField(
                related_name="rs_organizations_organization",
                through="rs_organizations.OrganizationUser",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
