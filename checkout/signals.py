from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_save(sender, instance, created, **kwargs):
    """
    Update order total when lineitem is updated
    """

    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_delete(sender, instance, **kwargs):
    """
    Update order total when lineitem is deleted
    """

    instance.order.update_total()
