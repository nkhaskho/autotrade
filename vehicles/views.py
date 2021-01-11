from django.shortcuts import render, redirect
from .models import *
from .forms import *


def vehicles_view(request):
    vehicles = Vehicle.objects.filter(for_sale=True)
    return render(request, "vehicles.html", {"vehicles": vehicles, "user": request.user})

def vehicle_details(request, id):
    vehicle = Vehicle.objects.get(pk=id)
    print(vehicle.for_sale)
    return render(request, "vehicledetails.html", {"vehicle": vehicle, "user": request.user})

def addvehicle_view(request):
    message = ""
    form = AddVehicleForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            try:
                model = form.cleaned_data.get("model")
                vehicle = Vehicle(
                    owner=request.user,
                    fuel_type=form.cleaned_data.get("fuel_type"),
                    model=form.cleaned_data.get("model"),
                    for_sale=form.cleaned_data.get("for_sale"),
                    kilometers=form.cleaned_data.get("kilometers"),
                    price=form.cleaned_data.get("price"),
                    brand=form.cleaned_data.get("brand"),
                )
                print(vehicle)
                vehicle.save()
                message = "{} saved successfully.".format(vehicle)
            except Exception as exp:
                message = exp
            
    return render(request, "addvehicle.html", {
        "form": form, 
        "user": request.user, 
        "message": message}
    )
