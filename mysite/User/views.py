from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse


def home(request):

    return render(request,'User/home.html')

