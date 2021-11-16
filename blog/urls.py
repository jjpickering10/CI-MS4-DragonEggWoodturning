from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog_post/<int:blog_id>/', views.blog_post, name='blog_post'),
    path('edit/edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('delete/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
