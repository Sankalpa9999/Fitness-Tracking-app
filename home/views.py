from django.shortcuts import render
from django.http import HttpResponse
from User .models import Member
from django.utils.decorators import method_decorator
from Membership.decorators import membership_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactMessageForm
from django.contrib.auth.decorators import login_required

# Create your views here.



def index(request):
    return render(request, 'home/index.html')

def home(request):
    user = request.user
    profile = None
    if user.is_authenticated:
        try:
            profile = Member.objects.get(user=user)
        except Member.DoesNotExist:
            pass
    
    return render(request,'home/homepage.html',{'profile':profile})


def about(request):
    user = request.user
    profile = None
    if user.is_authenticated:
        try:
            profile = Member.objects.get(user=user)
        except Member.DoesNotExist:
            pass
        
    return render(request,'home/about.html',{'profile':profile})


@membership_required
def service(request):
    user = request.user
    profile = None
    if user.is_authenticated:
        try:
            profile = Member.objects.get(user=user)
        except Member.DoesNotExist:
            pass
    return render(request, 'Home/service.html', {'profile': profile})



@login_required
def contact_page(request):
    user = request.user
    profile = None
    if user.is_authenticated:
        try:
            profile = Member.objects.get(user=user)
        except Member.DoesNotExist:
            pass
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactMessageForm()

    return render(request, 'Home/contact.html', {'form': form,'profile':profile})