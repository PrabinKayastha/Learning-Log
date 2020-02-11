"""Defines the URL pattern for learning_logs"""
from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # Page that hows all topic.
    path('topic/', views.topics, name='topics')
]
