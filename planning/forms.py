# planning/forms.py

from django import forms
from .models import WorkoutPlan, WorkoutSession, ScheduledWorkout

class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['exercise', 'description']

class WorkoutSessionForm(forms.ModelForm):
    class Meta:
        model = WorkoutSession
        fields = ['exercise', 'sets', 'reps', 'duration', 'rest_interval']
        widgets = {
            'duration': forms.TextInput(attrs={'placeholder': 'HH:MM:SS', 'pattern': '([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]', 'title': 'Enter a valid duration (HH:MM:SS)'}),
            'rest_interval': forms.TextInput(attrs={'placeholder': 'HH:MM:SS', 'pattern': '([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]', 'title': 'Enter a valid duration (HH:MM:SS)'}),
        }

    def __init__(self, *args, **kwargs):
        self.workout_plan_exercise_name = kwargs.pop('workout_plan_exercise_name', None)
        super(WorkoutSessionForm, self).__init__(*args, **kwargs)

    def clean_exercise(self):
        exercise = self.cleaned_data.get('exercise')
        if exercise.name != self.workout_plan_exercise_name:
            raise forms.ValidationError("Selected exercise does not match the exercise displayed in the heading")
        return exercise


class ScheduledWorkoutForm(forms.ModelForm):
    class Meta:
        model = ScheduledWorkout
        fields = ['workout_plan', 'date']
        
        widgets = {
            
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
