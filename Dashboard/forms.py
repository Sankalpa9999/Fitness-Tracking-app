from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['exercise', 'date', 'duration', 'calories_burned', 'distance_covered']
        
        widgets = {
            'exercise': forms.Select(attrs={'onchange': 'updateMuscleGroup()'}),  # Use JS to auto-fill muscle group
            'date': forms.DateInput(attrs={'type': 'date'}),
            'duration': forms.TextInput(attrs={'placeholder': 'HH:MM:SS', 'pattern': '([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]', 'title': 'Enter a valid duration (HH:MM:SS)'}),
        }