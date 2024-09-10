from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from User. models import Member
from User.forms import MemberForm
from Dashboard. models import Workout
from Dashboard.forms import WorkoutForm
from Exercise.models import Exercise

from Exercise.forms import ExerciseForm
from Goal.models import Goal
from Goal.forms import GoalForm


from planning.models import ScheduledWorkout,WorkoutPlan, WorkoutSession
from planning.forms import ScheduledWorkoutForm,WorkoutPlanForm, WorkoutSessionForm

from django.db import IntegrityError


from .forms import AdminForm
from .models import AdminProfile


from Progress.models import Progress
from Progress.forms import ProgressForm

# Create your views here.



from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def adminpanel(request):
    admin = request.user
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        return redirect('create_admin_profile')
    
    user = Member.objects.count()
    members = Member.objects.all()
    exercises = Exercise.objects.all()
    goals = Goal.objects.all()
    print(profile.name)    
    return render(request, 'Admin/adminsite.html', {
        'user': user,
        'members': members,
        'exercises': exercises,
        'goals': goals,
        'profile': profile
    })

@login_required
def workout_details_view(request):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    members = Member.objects.all()
    
    # Retrieve all workouts and group them by member
    workouts_by_member = {}
    for member in members:
        workouts = Workout.objects.filter(user=member.user)
        workouts_by_member[member] = workouts

    return render(request, 'Admin/workout_details.html', {
        'members': members,
        'workouts_by_member': workouts_by_member,
        'profile':profile
        
    })
    
    
    
@login_required
def update_workout_view(request, workout_id):
    # Retrieve the specific workout by its ID
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    workout = get_object_or_404(Workout, id=workout_id)

    if request.method == 'POST':
        # Bind the form to the POST data and the specific workout instance
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            # Save the updated workout
            form.save()
            return redirect('workout_details')  # Redirect to the workout details page after saving
    else:
        # Populate the form with the current workout data
        form = WorkoutForm(instance=workout)

    return render(request, 'Admin/update_workout.html', {'form': form,'profile':profile})

@login_required
def confirm_delete_workout(request, workout_id):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    workout = get_object_or_404(Workout, id=workout_id)
    
    if request.method == 'POST':
        workout.delete()
        messages.success(request, 'The workout was successfully deleted.')
        return redirect('workout_details')  # Replace with the appropriate URL name for your workout list view
    
    return render(request, 'Admin/confirm_delete_workout.html', {'workout': workout,'profile':profile})


# Exercise


@login_required
def admin_exercise_list(request):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    exercises = Exercise.objects.all()
    return render(request, 'Admin/admin_exercise_list.html', {'exercises': exercises,'profile':profile})

@login_required
def exercise_update(request, pk):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('admin_exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'Exercise/exercise_form.html', {'form': form,'profile':profile})

@login_required
def exercise_delete(request, pk):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    exercise = get_object_or_404(Exercise, pk=pk)
    if request.method == 'POST':
        exercise.delete()
        return redirect('admin_exercise_list')
    return render(request, 'Exercise/exercise_confirm_delete.html', {'exercise': exercise,'profile':profile})




#User Goals


def admin_goals_view(request):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    goals = Goal.objects.all()  # Fetch all goals
    return render(request, 'Admin/admin_goals.html', {'goals': goals,'profile':profile})


@login_required
def update_goal_view(request, goal_id):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    goal = get_object_or_404(Goal, id=goal_id)
    
    if request.method == 'POST':
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect('admin_goals')  # Redirect to the goals page after saving
    else:
        form = GoalForm(instance=goal)

    return render(request, 'Admin/update_goal.html', {'form': form, 'goal': goal,'profile':profile})

@login_required
def delete_goal_view(request, goal_id):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    
    goal = get_object_or_404(Goal, id=goal_id)
    if request.method == 'POST':
        goal.delete()
        return redirect('admin_goals')  # Redirect to the goals page after deleting
    return render(request, 'Admin/delete_goal_confirm.html', {'goal': goal,'profile':profile})


# Scheduled workouts 
@login_required
def view_scheduled_workouts(request):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    scheduled_workouts = ScheduledWorkout.objects.all()
    return render(request, 'Admin/view_scheduled_workouts.html', {'scheduled_workouts': scheduled_workouts,'profile':profile})

# Add Scheduled Workout
@login_required
def add_scheduled_workout(request):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    if request.method == 'POST':
        form = ScheduledWorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_scheduled_workouts')
    else:
        form = ScheduledWorkoutForm()
    return render(request, 'Admin/add_scheduled_workout.html', {'form': form,'profile':profile})

# Update Scheduled Workout
@login_required
def update_scheduled_workout(request, pk):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    scheduled_workout = get_object_or_404(ScheduledWorkout, pk=pk)
    if request.method == 'POST':
        form = ScheduledWorkoutForm(request.POST, instance=scheduled_workout)
        if form.is_valid():
            form.save()
            return redirect('view_scheduled_workouts')
    else:
        form = ScheduledWorkoutForm(instance=scheduled_workout)
    return render(request, 'Admin/update_scheduled_workout.html', {'form': form,'profile':profile})

# Delete Scheduled Workout
@login_required
def delete_scheduled_workout(request, pk):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    scheduled_workout = get_object_or_404(ScheduledWorkout, pk=pk)
    if request.method == 'POST':
        scheduled_workout.delete()
        return redirect('view_scheduled_workouts')
    return render(request, 'Admin/delete_scheduled_workout_confirm.html', {'scheduled_workout': scheduled_workout,'profile':profile})





# Workout Plans

@login_required
def admin_view_workout_plans(request):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    workout_plans = WorkoutPlan.objects.all()
    return render(request, 'Admin/admin_view_workout_plans.html', {'workout_plans': workout_plans,'profile':profile})

# Edit a workout plan
@login_required
def admin_edit_workout_plan(request, plan_id):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    workout_plan = get_object_or_404(WorkoutPlan, id=plan_id)
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST, instance=workout_plan)
        if form.is_valid():
            form.save()
            return redirect('admin_view_workout_plans')
    else:
        form = WorkoutPlanForm(instance=workout_plan)
    return render(request, 'Admin/admin_edit_workout_plan.html', {'form': form, 'workout_plan': workout_plan,'profile':profile})

# Delete a workout plan
@login_required
def admin_delete_workout_plan(request, plan_id):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    workout_plan = get_object_or_404(WorkoutPlan, id=plan_id)
    if request.method == 'POST':
        workout_plan.delete()
        return redirect('admin_view_workout_plans')
    return render(request, 'Admin/admin_delete_workout_plan.html', {'workout_plan': workout_plan,'profile':profile})

# Display all workout sessions
@login_required
def admin_view_workout_sessions(request):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    workout_sessions = WorkoutSession.objects.select_related('workout_plan__user', 'exercise').all()
    return render(request, 'Admin/admin_view_workout_sessions.html', {'workout_sessions': workout_sessions,'profile':profile})

# Edit a workout session
@login_required
def admin_edit_workout_session(request, session_id):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    workout_session = get_object_or_404(WorkoutSession, id=session_id)
    if request.method == 'POST':
        form = WorkoutSessionForm(request.POST, instance=workout_session)
        if form.is_valid():
            form.save()
            return redirect('admin_view_workout_sessions')
    else:
        form = WorkoutSessionForm(instance=workout_session)
    return render(request, 'Admin/admin_edit_workout_session.html', {'form': form, 'workout_session': workout_session,'profile':profile})

# Delete a workout session
@login_required
def admin_delete_workout_session(request, session_id):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    workout_session = get_object_or_404(WorkoutSession, id=session_id)
    if request.method == 'POST':
        workout_session.delete()
        return redirect('admin_view_workout_sessions')
    return render(request, 'Admin/admin_delete_workout_session.html', {'workout_session': workout_session,'profile':profile})






# Admin Profile

@login_required
def create_admin_profile(request):
    user = request.user
    admin_profile = AdminProfile.objects.filter(user=user).first()

    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES, instance=admin_profile)
        if form.is_valid():
            try:
                admin_profile = form.save(commit=False)
                admin_profile.user = user  # Ensuring the user is always set
                admin_profile.save()
                messages.success(request, 'Admin Profile Created Successfully!')
                return redirect('admin_profile')
            except IntegrityError:
                messages.error(request, 'Profile could not be created due to a database error.')
    else:
        form = AdminForm(instance=admin_profile)

    return render(request, 'Admin/create_admin_profile.html', {'form': form})




@login_required
def admin_profile(request):
    user = request.user
    try:
        profile = AdminProfile.objects.get(user=user)

    except AdminProfile.DoesNotExist:
        return redirect('create_admin_profile')

    context = {
        'profile': profile,
    }
    return render(request, 'Admin/admin_profile_page.html', context)



@login_required
def update_admin_profile(request):
    user = request.user
    try:
        # Attempt to retrieve the admin profile associated with the current user
        admin_profile = AdminProfile.objects.get(user=user)
    except AdminProfile.DoesNotExist:
        admin_profile = None

    if request.method == 'POST':
        # Instantiate the form with POST data and files
        form = AdminForm(request.POST, request.FILES, instance=admin_profile)
        if form.is_valid():
            try:
                if admin_profile:
                    # Update existing profile
                    form.save()
                else:
                    # Create a new profile if it doesn't exist
                    admin_profile = form.save(commit=False)
                    admin_profile.user = user
                    admin_profile.save()
                messages.success(request, 'Admin Profile Updated Successfully!')
                return redirect('admin_profile')  # Replace 'admin_profile' with your actual success URL name
            except IntegrityError:
                messages.error(request, 'Profile could not be updated due to a database error.')
    else:
        # Instantiate the form with the existing admin profile instance
        form = AdminForm(instance=admin_profile)

    # Render the form in the template
    return render(request, 'Admin/update_admin_profile.html', {'form': form})



#User's  Progress 

@login_required
def admin_progress_list(request):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    progresses = Progress.objects.all()
    return render(request, 'Admin/admin_progress_list.html', {'progresses': progresses,'profile':profile})


@login_required
def update_progress_view(request, progress_id):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    progress = get_object_or_404(Progress, id=progress_id)
    if request.method == 'POST':
        form = ProgressForm(request.POST, instance=progress)
        if form.is_valid():
            form.save()
            messages.success(request, 'Progress updated successfully!')
            return redirect('admin_progress_list')
    else:
        form = ProgressForm(instance=progress)
    return render(request, 'Admin/update_progress.html', {'form': form,'profile':profile})


@login_required
def delete_progress_view(request, progress_id):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    progress = get_object_or_404(Progress, id=progress_id)
    if request.method == 'POST':
        progress.delete()
        messages.success(request, 'Progress deleted successfully!')
        return redirect('admin_progress_list')
    return render(request, 'Admin/delete_progress_confirm.html', {'progress': progress,'profile':profile})




# Manage Users 

@login_required
def admin_member_list_and_details(request):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    members = Member.objects.all()  # Fetch all members
    member_details = {}

    for member in members:
        member_details[member] = {
            'details': {
                'name': member.name,
                'profile_picture': member.profile_picture,
                'phone': member.phone,
                'DOB': member.DOB,
                'occupation': member.occupation,
                'address': member.address,
                'email': member.email,
            },
            'workouts': Workout.objects.filter(user=member.user),
        }
    
    return render(request, 'Admin/admin_member_list_and_details.html', {
        'members': members,
        'member_details': member_details,
        'profile':profile
    })


@login_required
def update_member(request, pk):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin_member_list_and_details'))
    else:
        form = MemberForm(instance=member)
    
    return render(request, 'Admin/update_member.html', {'form': form, 'member': member,'profile':profile})


@login_required
def delete_member(request, pk):
    admin = request.user
    profile=None
    try:
        profile = AdminProfile.objects.get(user=admin)
    except AdminProfile.DoesNotExist:
        pass
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect(reverse('admin_member_list_and_details'))
    
    return render(request, 'Admin/confirm_delete_member.html', {'member': member,'profile':profile})