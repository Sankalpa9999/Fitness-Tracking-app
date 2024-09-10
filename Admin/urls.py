from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminpanel, name='adminsite'),
    
    
    # Workouts
    path('workout-details/', views.workout_details_view, name='workout_details'),
    path('update-workout/<int:workout_id>/', views.update_workout_view, name='update_workout'),
    path('delete-workout/<int:workout_id>/confirm/', views.confirm_delete_workout, name='confirm_delete_workout'),
    
    
    
    # Exercise
    path('exercises/', views.admin_exercise_list, name='admin_exercise_list'),
    path('exercises/update/<int:pk>/', views.exercise_update, name='exercise_update'),
    path('exercises/delete/<int:pk>/', views.exercise_delete, name='exercise_delete'),
    
    
    
    # Goals
    path('goals/', views.admin_goals_view, name='admin_goals'),
    path('goals/update/<int:goal_id>/', views.update_goal_view, name='update_goal'),
    path('goals/delete/<int:goal_id>/', views.delete_goal_view, name='delete_goal'),
    
    
    # Scheduled Workouts 
    path('admin/scheduled-workouts/', views.view_scheduled_workouts, name='view_scheduled_workouts'),
    path('admin/scheduled-workouts/add/',views. add_scheduled_workout, name='add_scheduled_workout'),
    path('admin/scheduled-workouts/update/<int:pk>/', views.update_scheduled_workout, name='update_scheduled_workout'),
    path('admin/scheduled-workouts/delete/<int:pk>/', views.delete_scheduled_workout, name='delete_scheduled_workout'),



     # Admin Workout Plan URLs
    path('admin/workout-plans/', views.admin_view_workout_plans, name='admin_view_workout_plans'),
    path('admin/workout-plans/<int:plan_id>/edit/', views.admin_edit_workout_plan, name='admin_edit_workout_plan'),
    path('admin/workout-plans/<int:plan_id>/delete/', views.admin_delete_workout_plan, name='admin_delete_workout_plan'),

    # Admin Workout Session URLs
    path('admin/workout-sessions/', views.admin_view_workout_sessions, name='admin_view_workout_sessions'),
    path('admin/workout-sessions/<int:session_id>/edit/', views.admin_edit_workout_session, name='admin_edit_workout_session'),
    path('admin/workout-sessions/<int:session_id>/delete/', views.admin_delete_workout_session, name='admin_delete_workout_session'),


    # Admin Profile
    path('create-admin-profile/', views.create_admin_profile, name='create_admin_profile'),
    path('update-admin-profile/', views.update_admin_profile, name='update_admin_profile'),
    path('admin-profile/', views.admin_profile, name='admin_profile'),
    



    # Admin Progress 

    path('admin/progress/', views.admin_progress_list, name='admin_progress_list'),
    path('admin/progress/update/<int:progress_id>/', views.update_progress_view, name='update_progress_view'),
    path('admin/progress/delete/<int:progress_id>/', views.delete_progress_view, name='delete_progress_view'),



    # Admin manage member
    path('admin/members/', views.admin_member_list_and_details, name='admin_member_list_and_details'),
    path('admin/member/update/<int:pk>/', views.update_member, name='update_member'),
    path('admin/member/delete/<int:pk>/', views.delete_member, name='delete_member'),
   
]
