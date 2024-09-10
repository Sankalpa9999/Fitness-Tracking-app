from django.shortcuts import render, redirect, get_object_or_404
from . models import Member
from django.contrib.auth.decorators import login_required
from .forms import MemberForm
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.


@login_required
def create_user(request):
    user = request.user
    try:
        member = Member.objects.get(user=user)
    except Member.DoesNotExist:
        member = None
        
    if request.method == 'POST':
        member_form = MemberForm(request.POST, request.FILES, instance=member)
        if member_form.is_valid():
            try:
                member = member_form.save(commit=False)
                if not member.user:
                    member.user = user
                member.save()
                messages.success(request, 'Profile Created Successfully!')
                return redirect('user_profile')
            except IntegrityError:
                return render(request, 'User/create_user.html', {
                    'member_form': member_form,
                    'error': 'Profile could not be created due to a database error.'
                })
    else:
        member_form = MemberForm(instance=member)

    return render(request, 'User/create_user.html', {
        'member_form': member_form,
    })
@login_required
def update_user(request):
    user = request.user
    try:
        member = Member.objects.get(user=user)
    except Member.DoesNotExist:
        member = None

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            try:
                if member:
                    form.save()  
                else:
                    member = form.save(commit=False)
                    member.user = user
                    member.save()  
                messages.success(request, 'Profile Updated Successfully!')
                return redirect('user_profile') 
            except IntegrityError:
                return render(request, 'User/update_user.html', {'form': form, 'error': 'Visitor profile could not be created due to a database error.'})
    else:
        form = MemberForm(instance=member)

    return render(request, 'User/update_user.html', {'form': form})

@login_required(login_url='login_view')
def user_profile(request):
    user = request.user
    try:
        profile = Member.objects.get(user=user)
    except Member.DoesNotExist:
        return redirect('create_user')

    context = {
        'profile': profile,
    }
    return render(request, 'User/user_profile_page.html', context)
