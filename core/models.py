from django.db import models


class ContactSubmission(models.Model):

    INTEREST_CHOICES = [
        ("Volunteer", "Volunteer"),
        ("Donate", "Donate"),
        ("Partner", "Partner"),
        ("General Inquiry", "General Inquiry"),
    ]

    full_name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    interest = models.CharField(
        max_length=50,
        choices=INTEREST_CHOICES,
        default="General Inquiry"
    )

    message = models.TextField()

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.full_name} - {self.interest}"