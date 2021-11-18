from django.contrib import admin
from .models import Subscribers, Newsletter


class SubscribersAdmin(admin.ModelAdmin):

    list_display = (
        'email',
        'date',
        'unsubscribe',
    )

    ordering = (
        '-date',
    )


class NewsletterAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'date',
    )

    ordering = (
        '-date',
    )

admin.site.register(Subscribers, SubscribersAdmin)
admin.site.register(Newsletter, NewsletterAdmin)

