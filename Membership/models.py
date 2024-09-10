# models.py
from django.db import models
from User.models import User
from django.utils import timezone
from datetime import timedelta

class Membership(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basic Plan'),
        ('standard', 'Standard Plan'),
        ('premium', 'Premium Plan'),
    ]
    plan_type = models.CharField(max_length=10, choices=PLAN_CHOICES, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_days = models.IntegerField()

    def __str__(self):
        return self.plan_type

class UserMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()

    def is_active(self):
        return self.end_date > timezone.now()

    def __str__(self):
        return f"{self.user.username} - {self.membership.plan_type}"
