from django.urls import path
from vehicles import views

urlpatterns = [
    path('vehicles/', views.vehicles_view, name="vehicles_path")
]