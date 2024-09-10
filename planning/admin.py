from django.contrib import admin
from.models import  WorkoutPlan, ScheduledWorkout, WorkoutSession
# Register your models here.

admin.site.register(WorkoutPlan),
admin.site.register(ScheduledWorkout),
admin.site.register(WorkoutSession)