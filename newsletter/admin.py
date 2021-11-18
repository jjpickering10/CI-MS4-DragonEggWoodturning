from django.contrib import admin
from .models import Subscribers


class SubscribersAdmin(admin.ModelAdmin):

    list_display = (
        'email',
        'date',
        'unsubscribe',
    )

    ordering = (
        '-date',
    )

admin.site.register(Subscribers, SubscribersAdmin)

