"""Defines URL patterns for users"""
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]