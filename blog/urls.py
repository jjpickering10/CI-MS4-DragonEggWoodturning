from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog_post/<int:blog_id>/', views.blog_post, name='blog_post'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path(
        'edit/edit_comment/<int:comment_id>/',
        views.edit_comment, name='edit_comment'),
    path(
        'delete/delete_comment/<int:comment_id>/',
        views.delete_comment, name='delete_comment'),
    path('like/like_post/<int:blog_id>/', views.like_post, name='like_post'),
]
