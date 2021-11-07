from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('all_categories/', views.all_categories, name='all_categories'),
]