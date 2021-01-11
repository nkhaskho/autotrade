from django import forms
from vehicles.models import *

class AddVehicleForm(forms.Form):
    """
    class Meta:
        model = Vehicle
        fields = ['model', 'brand', 'kilometers', 'fuel_type']
    """

    #for_sale, model, brand, fuel_type, kilometers, price, owner

    for_sale = forms.BooleanField(initial=True, required=False)

    model = forms.CharField(
        required=True,
        label="Model: ", 
        initial=None,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )    
    )

    fuel_type = forms.ModelChoiceField(
        queryset=FuelType.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )    
    )

    kilometers = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    price = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    photo = forms.ImageField()
    
    


class PredictedVehicleForm(forms.Form):

    model = forms.CharField(
        label="Model: ", 
        initial=None,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )    
    )

    fuel_type = forms.ModelChoiceField(
        queryset=FuelType.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )    
    )

    kilometers = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )


    
    

