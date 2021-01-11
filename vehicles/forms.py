from django import forms
from vehicles.models import *

class AddVehicleForm(forms.Form):
    class Meta:
        model = Vehicle
        fields = ['model', 'brand', 'kilometers', 'fuel_type']


    """
    #for_sale, model, brand, fuel_type, kilometers, price, owner
    for_sale = forms.ChoiceField(choices=(("Option 1", "For sale"), ("Option 2", "Not for sale"),))

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
        attrs={
            "class": "form-control"
        },
        choices=list(Brand.objects.all())
    )

    #fuel_type = forms.ChoiceField(choices=('Option 1', 'Gas'),('Option 2', 'Diesel'),('Option 3', 'Essence'),)

    kilometers = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    """

