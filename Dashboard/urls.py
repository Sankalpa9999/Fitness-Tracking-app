from django.urls import path
from .views import dashboard_view, log_workout_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('log/', log_workout_view, name='log_workout'),
]
