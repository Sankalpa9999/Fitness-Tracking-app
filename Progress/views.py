from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Progress
from .forms import ProgressForm
from django.contrib.auth.decorators import login_required
import plotly.express as px
import pandas as pd
from django.http import HttpResponse
from django.template import loader
from User .models import Member

@login_required
def progress_list(request):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    progresses = Progress.objects.filter(user=request.user).order_by('-date')
    for p in progresses:
        print(p)  # Print each progress to verify
    return render(request, 'Progress/progress_list.html', {'progresses': progresses,'profile': profile})


@login_required
def add_progress(request):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.user = request.user
            progress.save()
            print(progress)  # Print the progress to verify
            return redirect('progress_list')
    else:
        form = ProgressForm()
    return render(request, 'Progress/add_progress.html', {'form': form,'profile': profile})


@login_required
def edit_progress(request, progress_id):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    progress = get_object_or_404(Progress, id=progress_id, user=request.user)
    if request.method == 'POST':
        form = ProgressForm(request.POST, instance=progress)
        if form.is_valid():
            form.save()
            return redirect('progress_list')
    else:
        form = ProgressForm(instance=progress)
    return render(request, 'Progress/edit_progress.html', {'form': form,'profile': profile})


@login_required
def progress_charts(request):
    user = request.user
    profile = None
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        pass
    progresses = Progress.objects.filter(user=request.user).order_by('date')
    dates = [p.date for p in progresses]
    weights = [p.weight for p in progresses]
    performances = [p.performance for p in progresses]
    workout_frequencies = [p.workout_frequency for p in progresses]

    print(dates, weights, performances, workout_frequencies)  # Debug print

    df = pd.DataFrame({
        'Date': dates,
        'Weight': weights,
        'Performance': performances,
        'Workout Frequency': workout_frequencies
    })

    weight_fig = px.line(df, x='Date', y='Weight', title='Weight Over Time')
    performance_fig = px.line(df, x='Date', y='Performance', title='Performance Over Time')
    workout_frequency_fig = px.line(df, x='Date', y='Workout Frequency', title='Workout Frequency Over Time')

    weight_chart = weight_fig.to_html(full_html=False)
    performance_chart = performance_fig.to_html(full_html=False)
    workout_frequency_chart = workout_frequency_fig.to_html(full_html=False)

    return render(request, 'Progress/progress_chart.html', {
        'weight_chart': weight_chart,
        'performance_chart': performance_chart,
        'workout_frequency_chart': workout_frequency_chart,
        'profile': profile,
    })
