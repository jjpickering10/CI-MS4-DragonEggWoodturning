from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('all_categories/', views.all_categories, name='all_categories'),
]