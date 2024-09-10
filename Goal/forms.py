# forms.py

from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_type', 'target_value', 'start_date', 'end_date', 'achieved']
