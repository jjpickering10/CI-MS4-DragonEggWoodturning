from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Subscribers, Newsletter


@receiver(post_save, sender=Subscribers)
def update_send_welcome_email(sender, instance, created, **kwargs):
    """
    Send welcome newsletter
    """
    if created:
        instance.send_welcome_newsletter()


@receiver(post_save, sender=Newsletter)
def update_send_newsletter(sender, instance, created, **kwargs):
    """
    Send newsletter
    """
    if created:
        instance.send_newsletter()