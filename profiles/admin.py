from django.contrib import admin

from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
    )

admin.site.register(UserProfile, ProfileAdmin)