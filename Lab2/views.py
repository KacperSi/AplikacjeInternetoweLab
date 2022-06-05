from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TeamRegisterForm, MentorRegisterForm

from django.contrib.auth.models import User
from .models import Mentor

from django.contrib.auth import get_user_model


def register(request):
    if request.method == 'POST':
        form = TeamRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'A password setting form has been sent to your email. Please use it to complete the registration.')
            render(request, 'Lab2/register.html', {'form': form})
    else:
        form = TeamRegisterForm()
    return render(request, 'Lab2/register.html', {'form': form})

def MentorRegister(request):
    if request.method == 'POST':
        form = MentorRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your application has been accepted!')
            render(request, 'Lab2/register.html', {'form': form})
    else:
        form = MentorRegisterForm(request.POST)
    return render(request, 'Lab2/register.html', {'form': form})
