from django.urls import path
from . import views

urlpatterns = [
    path('exerciselist/', views.exercise_list, name='exercise_list'),
    path('exercise/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('exercise/new/', views.exercise_create, name='exercise_create'),
    path('exercise/<int:pk>/edit/', views.exercise_update, name='exercise_update'),
]
