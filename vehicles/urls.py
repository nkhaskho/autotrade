from django.urls import path
from vehicles import views

urlpatterns = [
    path('vehicles/', views.vehicles_view, name="vehicles_path"),
    path('addvehicle/', views.addvehicle_view, name="newvehicle_path"),
    path(r'vehicles/<int:id>', views.vehicle_details, name="vehicledetails_path")
]