from django.db import models
from Register.models import User
from datetime import date
# Create your models here.


class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    profile_picture = models.ImageField(upload_to='admin_profiles/', null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    DOB= models.DateField(null=True)
    occupation = models.CharField(max_length= 20, null=True)
    address = models.CharField(max_length=30, null=True)
        
    

    def __str__(self):
        return f"{self.user.username}'s Profile"