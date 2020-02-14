"""Defines the URL pattern for learning_logs"""
from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),

    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),

    # Details page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    
    # Page for adding new topics.
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding new entry.
    path('new_entry/<int:topic_id>', views.new_entry, name='new_topic'),

]
