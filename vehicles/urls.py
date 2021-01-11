from django.urls import path
from vehicles import views

urlpatterns = [
    path('vehicles/', views.vehicles_view, name="vehicles_path"),
    path('addvehicle/', views.addvehicle_view, name="newvehicle_path"),
    path('predict/', views.predictvehicle_view, name="predictvehicle_path"),
    path(r'vehicles/<int:id>', views.vehicle_details, name="vehicledetails_path"),
    path(r'delete/<int:vehicle_id>', views.delete_vehicle, name="delete_vehicle")
]