from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from authentication.forms import LoginForm
from vehicles.models import *


def login_view(request):
    message = ""
    if request.method == 'GET':
        form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)
            try:
                user = authenticate(username=username, password=password)
                if user is not None:
                    print("redirecting to home...")
                    login(request, user)
                    return redirect('home_path')
                else:
                    message = "User is None"
            except Exception as exp:
                print(exp)
                message = exp
        else:
            message = "Missing required credentials"
    else:
        form = LoginForm()
    print(message)
    return render(request, 'login.html', {'form': form, "message": message})


def home_view(request):
    user_vehicles = Vehicle.objects.filter(owner=request.user)
    return render(request, "home.html", {"user": request.user, "user_vehicles": user_vehicles})


def logout_view(request):
    return redirect('login_path')