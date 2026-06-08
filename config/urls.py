from django.contrib import admin
from django.urls import path

from core.views import (
    home,
    projects,
    contact,
    contact_success,
    donations,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path("projects/", projects, name="projects"),

    path("contact/", contact, name="contact"),

    path("contact-success/", contact_success, name="contact_success"),

    path("donate/", donations, name="donations"),
]