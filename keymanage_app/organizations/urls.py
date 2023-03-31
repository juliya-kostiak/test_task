from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("organizations/", views.organizations, name="organizations"),
    path("keys/", views.keys, name="keys"),
    path("add_org", views.add_org, name="add_org"),
    path("add_key", views.add_key, name="add_key"),
    path("organizations/<int:pk>/update", views.UpdateOrg.as_view(), name="update_org"),
    path("organizations/<int:pk>/delete", views.DeleteOrg.as_view(), name="delete_org"),
]
