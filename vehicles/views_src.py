from django.shortcuts import render, redirect
from users.models import *
from users.forms import LoginForm


def login_view(request):
    message = ""
    if request.method == 'GET':
        form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            try:
                user = User.objects.get(username=username, password=password)
                if user is not None:
                    print("redirecting to home...")
                    #redirect('www.google.com')
                    return render(request, "home.html", {"username": username})
            except Exception as exp:
                print(exp)
                message = "Invalid credentials"
        else:
            message = "Missing required credentials"
    else:
        form = LoginForm()
    print(message)
    return render(request, 'login.html', {'form': form, "message": message})

def home_view(request):
    return render(request, "home.html", {})

def logout_view(request):
    return redirect('login_path')


def vehicles_view(request):
    vehicles = Vehicle.objects.all()
    return render(request, "vehicles.html", {"vehicles": vehicles})