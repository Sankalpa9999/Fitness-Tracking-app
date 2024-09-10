# planning/models.py

from django.db import models
from django.conf import settings
from Exercise.models import Exercise

class WorkoutPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.exercise.name

class WorkoutSession(models.Model):
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='sessions')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    duration = models.DurationField(blank=True, null=True)
    rest_interval = models.DurationField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.exercise.name} - {self.sets} sets of {self.reps} reps"

class ScheduledWorkout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.workout_plan.exercise.name} on {self.date}"
