from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Subscribers


@receiver(post_save, sender=Subscribers)
def update_save(sender, instance, created, **kwargs):
    """
    Send welcome newsletter
    """
    if created:
        instance.send_welcome_newsletter()