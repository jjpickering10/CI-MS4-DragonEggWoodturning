import uuid
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

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the unsubscribe identifier
        """
        if not self.unsubscribe:
            self.unsubscribe = self._generate_unsubscribe()
        super().save(*args, **kwargs)
