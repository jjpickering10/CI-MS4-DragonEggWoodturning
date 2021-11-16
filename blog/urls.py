from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog_post/<int:blog_id>/', views.blog_post, name='blog_post'),
]