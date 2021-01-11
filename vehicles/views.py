from django.shortcuts import render, redirect
from vehicles.models import Vehicle


def vehicles_view(request):
    vehicles = Vehicle.objects.all()
    current_user = request.user
    return render(request, "vehicles.html", {"vehicles": vehicles, "current_user": current_user})
