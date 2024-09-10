# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import GoalForm
from django.db.models import Sum 
from .models import Goal, Progress, Notification
from User .models import Member

@login_required
def set_goal(request):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            messages.success(request, 'Goal successfully set!')
            return redirect('track_progress', goal_id=goal.id)
    else:
        form = GoalForm()
    
    return render(request, 'Goal/set_goal.html', {'form': form,'profile': profile})

@login_required
def track_progress(request, goal_id):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    if request.method == 'POST':
        current_value = float(request.POST.get('current_value', 0))
        if current_value > 0:
            Progress.objects.create(goal=goal, current_value=current_value)
            check_goal_completion(goal)
            messages.success(request, 'Progress tracked successfully!')
        else:
            messages.error(request, 'Invalid progress value.')
        return redirect('track_progress', goal_id=goal_id)
    
    progress = Progress.objects.filter(goal=goal)
    notifications = Notification.objects.filter(user=request.user, read=False)
    return render(request, 'Goal/track_progress.html', {'goal': goal, 'progress': progress, 'notifications': notifications,'profile': profile})

@login_required
def check_goal_completion(goal):
    # Calculate the sum of current_value for the associated progress
    progress_sum = goal.progress_set.aggregate(total_progress=Sum('current_value'))['total_progress']
    # Check if progress_sum is not None and compare with target_value
    if progress_sum is not None and goal.target_value <= progress_sum:
        # Check if the goal has not already been achieved
        if not goal.achieved:
            goal.achieved = True
            goal.save()
            Notification.objects.create(user=goal.user, message=f'Congratulations {goal.user}! You have achieved your {goal.get_goal_type_display()} goal.')

@login_required
def goal_history(request):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    goals = Goal.objects.filter(user=request.user)
    return render(request, 'Goal/goal_history.html', {'goals': goals, 'profile': profile})