from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(
        label="Username: ", 
        initial=None,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        label="Password: ", 
        initial=None,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

