
from django import forms
from .models import Progress

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['date', 'weight', 'performance', 'workout_frequency']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'weight': forms.NumberInput(attrs={'placeholder': 'Enter weight in kg'}),
            'performance': forms.TextInput(attrs={'placeholder': 'Enter performance'}),
            'workout_frequency': forms.NumberInput(attrs={'placeholder': 'Enter workout frequency per week'}),
        }