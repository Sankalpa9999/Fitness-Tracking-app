from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'profile_picture', 'phone', 'DOB' ,'occupation', 'address', 'email']
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date'}),
        }
     
