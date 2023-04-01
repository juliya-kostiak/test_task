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
    path("keys/<int:pk>/delete", views.DeleteKeys.as_view(), name="delete_key"),
    path("keys/<int:pk>/update", views.UpdateKey.as_view(), name="update_key"),
    path("keys/<str:id_org>/filter", views.filter_key, name="filter_key"),
]
