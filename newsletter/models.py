import uuid
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from django.db import models


class Subscribers(models.Model):
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    unsubscribe = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.email

    def _generate_unsubscribe(self):
        """
        Generate a random, unique identifier using UUID
        """
        return uuid.uuid4().hex.upper()

    def send_welcome_newsletter(self):
        """
        Send welcome newsletter email
        """
        subscriber_email = self.email
        unsubscribe_id = self.unsubscribe
        subject = render_to_string(
            'newsletter/newsletter_emails/welcome_newsletter_subject.txt', {
                'subscriber_email': subscriber_email
                }
            )
        body = render_to_string(
            'newsletter/newsletter_emails/welcome_newsletter_body.txt', {
                'unsubscribe_url': settings.UNSUBSCRIBE_URL,
                'unsubscribe_id': unsubscribe_id,
                'contact_email': settings.DEFAULT_FROM_EMAIL
                }
            )

        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [subscriber_email])

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the unsubscribe identifier
        """
        if not self.unsubscribe:
            self.unsubscribe = self._generate_unsubscribe()
        super().save(*args, **kwargs)
