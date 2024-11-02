from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from accounts.forms import LoginForm, SignUpForm


def user_logout(request):
    logout(request)
    return redirect("home")


def user_login(request): 
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect("/")
    else: 
        form = LoginForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)

def user_signup(request): 
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            email= form.cleaned_data.get("email")
            password= form.cleaned_data.get("password")
            password_confirmation= form.cleaned_data.get(
                "password_confirmation")
            
            if password == password_confirmation:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                
                login(request, user)
                return redirect("/")
            else:
                form.add("password", "Passwords do not match")
    else: 
        form = SignUpForm
        
    context = {"form": form}
    return render(request, "accounts/signup.html", context)