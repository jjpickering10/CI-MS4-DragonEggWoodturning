from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='subscribe'),
    path('unsubscribe/<unsubscribe_id>/', views.unsubscribe, name='unsubscribe'),
]