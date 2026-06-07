from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import EmailMessage
import os
import resend

from .forms import ContactSubmissionForm


def home(request):
    return render(request, "home.html")


def projects(request):
    return render(request, "projects.html")


def contact(request):

    if request.method == "POST":

        form = ContactSubmissionForm(request.POST)

        if form.is_valid():

            submission = form.save()

            subject = (
                f"New Inquiry from "
                f"{submission.full_name} "
                f"({submission.email})"
            )

            message = f"""
New message received from the Divine Ministries website.

CONTACT DETAILS
--------------------------
Name: {submission.full_name}
Email: {submission.email}
Phone: {submission.phone}
Interest: {submission.interest}

MESSAGE
--------------------------
{submission.message}
"""

            resend.api_key = os.getenv("RESEND_API_KEY")

            resend.Emails.send({
                "from": "onboarding@resend.dev",
                "to": ["elshaddaimhango@gmail.com"],
                "subject": subject,
                "text": message,
            })

            return redirect("contact_success")

    else:
        form = ContactSubmissionForm()

    return render(
        request,
        "contact.html",
        {
            "form": form
        }
    )


def contact_success(request):
    return render(request, "contact_success.html")