from django.db import models
from Register.models import User
from datetime import date
# Create your models here.


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    name = models.CharField(max_length=255, null=True)
    profile_picture = models.ImageField(upload_to='user_profiles/', null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    DOB= models.DateField(null=True)
    occupation = models.CharField(max_length= 20, null=True)
    address = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    
    
    def calculate_age(self):
        if self.DOB:
            today =date.today()
            age = today.year - self.DOB - ((today.month, today.day)<(self.DOB.month, self.DOB.day))
            return age
        return None
        
    

    def __str__(self):
        return f"{self.user.username}'s Profile"