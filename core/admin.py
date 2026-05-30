from django.contrib import admin
from .models import ContactSubmission


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "interest",
        "submitted_at",
    )

    search_fields = (
        "full_name",
        "email",
        "message",
    )

    list_filter = (
        "interest",
        "submitted_at",
    )