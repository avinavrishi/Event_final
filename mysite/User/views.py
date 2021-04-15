from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request,'User/home.html')

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid:
            user=form.save()
            login(request, user)
            return render(request, 'home/home.html')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    else:
        form=UserCreationForm
    return render(request, "User/register.html", context={"form":form})
