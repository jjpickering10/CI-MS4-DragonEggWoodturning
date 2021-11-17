from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Review


@receiver(post_save, sender=Review)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update product rating on save
    """
    instance.product.update_rating()
    print(instance.product.rating)


@receiver(post_delete, sender=Review)
def update_on_delete(sender, instance, **kwargs):
    """
    Update product rating on delete
    """
    instance.product.update_rating()
    print(instance.product.rating)