"""Defines the URL patterns for the users"""

from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # Include default auth URLs
    path('', include('django.contrib.auth.urls')),
]
