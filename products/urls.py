from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_discount/<int:product_id>/', views.add_discount, name='add_discount'),
    path('category_discount/<int:category_id>/', views.category_discount, name='category_discount'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('edit_product_images/<int:product_id>/', views.edit_product_images, name='edit_product_images'),
    path('delete_product_images/<int:image_id>/', views.delete_product_images, name='delete_product_images'),
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
]