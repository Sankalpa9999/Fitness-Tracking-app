# Membership/decorators.py
from django.shortcuts import redirect
from django.utils import timezone
from .models import UserMembership
from django.contrib.auth.decorators import login_required
from functools import wraps

def membership_required(view_func):
    @wraps(view_func)
    @login_required(login_url='login_view')  # Redirect to login page if user is not authenticated
    def _wrapped_view(request, *args, **kwargs):
        if not UserMembership.objects.filter(user=request.user, end_date__gte=timezone.now()).exists():
            return redirect('membership_plans')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
