# planning/views.py

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import WorkoutPlan, WorkoutSession, ScheduledWorkout
from django.contrib.auth.decorators import login_required 
from .forms import WorkoutPlanForm, WorkoutSessionForm, ScheduledWorkoutForm
from Dashboard.models import Workout  # Import Workout model
from django.core import serializers
from User .models import Member

@login_required
def workout_planner(request):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    workout_plans = WorkoutPlan.objects.filter(user=request.user)
    scheduled_workouts = ScheduledWorkout.objects.filter(user=request.user)
    workouts = Workout.objects.filter(user=request.user)  # Fetch workouts for the calendar
    return render(request, 'planning/workout_planner.html', {
        'workout_plans': workout_plans,
        'scheduled_workouts': scheduled_workouts,
        'workouts': workouts,
        'profile': profile,
    })

@login_required
def create_workout_plan(request):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST)
        if form.is_valid():
            workout_plan = form.save(commit=False)
            workout_plan.user = request.user
            workout_plan.save()
            return redirect('workout_planner')
    else:
        form = WorkoutPlanForm()
    return render(request, 'planning/create_workout_plan.html', {'form': form,'profile': profile})

@login_required
def add_workout_session(request, plan_id):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    workout_plan = get_object_or_404(WorkoutPlan, id=plan_id)
    if request.method == 'POST':
        form = WorkoutSessionForm(request.POST, workout_plan_exercise_name=workout_plan.exercise.name)
        if form.is_valid():
            workout_session = form.save(commit=False)
            workout_session.workout_plan = workout_plan
            workout_session.save()
            return redirect('workout_planner')
    else:
        form = WorkoutSessionForm(workout_plan_exercise_name=workout_plan.exercise.name)
    return render(request, 'planning/add_workout_session.html', {'form': form, 'workout_plan': workout_plan, 'profile': profile})

@login_required
def schedule_workout(request):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    if request.method == 'POST':
        form = ScheduledWorkoutForm(request.POST)
        if form.is_valid():
            scheduled_workout = form.save(commit=False)
            scheduled_workout.user = request.user
            scheduled_workout.save()
            return redirect('workout_planner')
    else:
        form = ScheduledWorkoutForm()
    return render(request, 'planning/schedule_workout.html', {'form': form,'profile': profile})
