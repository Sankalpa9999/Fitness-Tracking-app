from django.db import models
from django.conf import settings
from Exercise.models import Exercise

class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)  # Assuming 1 is a valid Exercise ID
    muscle_group = models.CharField(max_length=100, default='General')
    workout_type = models.CharField(max_length=100)
    date = models.DateField()
    duration = models.DurationField()
    calories_burned = models.IntegerField()
    distance_covered = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.workout_type} on {self.date}"

