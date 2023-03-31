from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("organizations/", views.organizations, name="organizations"),
    path("keys/", views.keys, name="keys"),
]
