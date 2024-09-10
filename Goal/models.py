# models.py

from django.db import models
from django.conf import settings
from django.utils import timezone

class Goal(models.Model):
    GOAL_TYPES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('endurance_improvement', 'Endurance Improvement'),
        ('flexibility', 'Flexibility'),
        
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    goal_type = models.CharField(max_length=50, choices=GOAL_TYPES)
    target_value = models.FloatField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s {self.get_goal_type_display()} Goal"

class Progress(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    current_value = models.FloatField()
    date_recorded = models.DateField(default=timezone.now)

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    read = models.BooleanField(default=False)
