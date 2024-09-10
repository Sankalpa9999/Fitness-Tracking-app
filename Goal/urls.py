# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.set_goal, name='set_goal'),
    path('track/<int:goal_id>/', views.track_progress, name='track_progress'),
    path('history/', views.goal_history, name='goal_history'),
    # Add more URLs as needed
]
