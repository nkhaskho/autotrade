from django import forms
from vehicles.models import *

class AddVehicleForm(forms.Form):
    #for_sale, model, brand, fuel_type, kilometers, price, owner
    for_sale = forms.BooleanField(
        label="For sale: ", 
        initial=True,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            },
            choices=[("For sale", "Not for sale")]
        )
    )
    model = forms.CharField(
        label="Model: ", 
        initial=None,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    brand = forms.Select(
        label="Password: ", 
        widget=forms.Select(
            attrs={
                "class": "form-control"
            },
            choices=Brand.objects.all()
        )
    )

