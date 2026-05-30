from django import forms
from .models import ContactSubmission


class ContactSubmissionForm(forms.ModelForm):

    class Meta:
        model = ContactSubmission
        fields = [
            "full_name",
            "email",
            "phone",
            "interest",
            "message",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["full_name"].widget.attrs.update({
            "placeholder": "Full Name"
        })

        self.fields["email"].widget.attrs.update({
            "placeholder": "Email Address"
        })

        self.fields["phone"].widget.attrs.update({
            "placeholder": "Phone Number (Optional)"
        })

        self.fields["message"].widget.attrs.update({
            "placeholder": "Your Message"
        })