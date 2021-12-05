import uuid
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from django.db import models


class Subscribers(models.Model):
    """
    Subscribers model
    """
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

        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [
            subscriber_email], fail_silently=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the unsubscribe identifier
        """
        if not self.unsubscribe:
            self.unsubscribe = self._generate_unsubscribe()
        super().save(*args, **kwargs)


class Newsletter(models.Model):
    """
    Newsletter model
    """
    title = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.title

    def send_newsletter(self):
        """
        Send newsletter email
        """
        emails = Subscribers.objects.all()

        title = self.title
        message = self.message

        for email in emails:
            subscriber_email = email.email
            unsubscribe_id = email.unsubscribe

            subject = render_to_string(
                'newsletter/newsletter_emails/newsletter_subject.txt', {
                    'title': title
                    }
                )
            body = render_to_string(
                'newsletter/newsletter_emails/newsletter_body.txt', {
                    'unsubscribe_url': settings.UNSUBSCRIBE_URL,
                    'unsubscribe_id': unsubscribe_id,
                    'contact_email': settings.DEFAULT_FROM_EMAIL,
                    'message': message,
                    'subscriber_email': subscriber_email
                    }
                )

            send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [
                subscriber_email], fail_silently=False)
