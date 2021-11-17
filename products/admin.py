from django.contrib import admin
from .models import Product, Category, WoodType, Image, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'name',
        'price',
        'rating',
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


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'product',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'rating',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(WoodType, WoodTypeAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Review, ReviewAdmin)
