from django import forms
from .models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [
            'name', 'muscle_group', 'equipment', 'difficulty', 
            'description', 'thumbnail', 'video_url', 'steps'
        ]