from django.urls import path

from roomsharing.rs_organizations.views import organization_list_view

app_name = "rs_organizations"
urlpatterns = [path("", organization_list_view, name="list")]
