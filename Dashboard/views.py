from django.shortcuts import render, redirect
from .models import Workout
from .forms import WorkoutForm
from User .models import Member
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now, timedelta
from django.db.models import Count

# get_object_or_404
@login_required
def dashboard_view(request):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    workouts = Workout.objects.filter(user=request.user)

    common_workouts = workouts.values('exercise__name').annotate(count=Count('exercise')).order_by('-count')
    print (common_workouts)
    
    return render(request, 'dashboard/dashboard.html', {
        'workouts': workouts,
        'common_workout': common_workouts,
        'profile': profile,
        
    })

@login_required
def log_workout_view(request):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('dashboard')
    else:
        form = WorkoutForm()
    return render(request, 'dashboard/log_workout.html', {'form': form,'profile': profile})

# a= request.POST.get('key',None)
# if a == None:
    