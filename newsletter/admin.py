from django.contrib import admin
from .models import Subscribers


class SubscribersAdmin(admin.ModelAdmin):

    fields = (
        'email',
        'unsubscribe'
    )

    ordering = (
        '-date',
    )

admin.site.register(Subscribers, SubscribersAdmin)

