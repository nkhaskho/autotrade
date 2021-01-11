from django.shortcuts import render, redirect
from .models import *
from .forms import *


def vehicles_view(request):
    vehicles = Vehicle.objects.all()
    return render(request, "vehicles.html", {"vehicles": vehicles, "user": request.user})

def vehicle_details(request, id):
    vehicle = Vehicle.objects.get(pk=id)
    print(vehicle.for_sale)
    return render(request, "vehicledetails.html", {"vehicle": vehicle, "user": request.user})

def addvehicle_view(request):
    vehicle = Vehicle()
    message = ""
    form = AddVehicleForm()
    if request.method == 'GET':
        form = AddVehicleForm()
    if request.method == 'POST':
        form = AddVehicleForm(request.POST)
        if form.is_valid():
            model = form.cleaned_data.get("model")
    return render(request, "addvehicle.html", {"vehicle": vehicle, "user": request.user, "message": message})
