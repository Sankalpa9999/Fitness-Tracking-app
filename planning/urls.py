# planning/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_planner, name='workout_planner'),
    path('create/', views.create_workout_plan, name='create_workout_plan'),
    path('add-session/<int:plan_id>/', views.add_workout_session, name='add_workout_session'),
    path('schedule/', views.schedule_workout, name='schedule_workout'),
]
