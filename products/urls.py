from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('all_categories/', views.all_categories, name='all_categories'),
    path('add_discount/<int:product_id>/', views.add_discount, name='add_discount'),
    path('category_discount/<int:category_id>/', views.category_discount, name='category_discount'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
]