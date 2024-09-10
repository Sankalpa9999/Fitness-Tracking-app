from django.conf import settings
from django.db import models

class Progress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField(null=True, blank=True)
    performance = models.FloatField(null=True, blank=True)
    workout_frequency = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"