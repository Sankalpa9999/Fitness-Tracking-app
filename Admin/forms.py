from django import forms
from .models import AdminProfile

class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ['name', 'profile_picture', 'phone', 'DOB', 'occupation', 'address']
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
