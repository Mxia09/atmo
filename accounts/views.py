from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

def user_logout(request):
    logout(request)
    return redirect("")
