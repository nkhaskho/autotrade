from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class FuelType(models.Model):
    fuel_type = models.CharField(max_length=30)
    def __str__(self):
        return self.fuel_type


class Vehicle(models.Model):
    for_sale = models.BooleanField(default=False)
    model = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    kilometers = models.IntegerField()
    price = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return "{} - {}".format(self.model, self.brand)