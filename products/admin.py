from django.contrib import admin
from .models import Product, Category, WoodType


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'wood_type',
        'sku',
        'name',
        'price',
        'rating',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class WoodTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WoodType, WoodTypeAdmin)
