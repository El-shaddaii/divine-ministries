from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import EmailMessage

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

            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=["elshaddaimhango@gmail.com"],
                reply_to=[submission.email],
            )
#            try:
#                email.send()
#                print("EMAIL SENT")
#            except Exception as e:
#                print("EMAIL ERROR:", str(e))
 
            email.send(fail_silently=False)             
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