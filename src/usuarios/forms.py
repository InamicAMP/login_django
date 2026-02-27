from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Aspirante

class RegistroForm(UserCreationForm):

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Correo Electrónico"
    }))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # Campos adicionales
    clave_elector = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Clave de elector"
    }))

    nombre = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Nombre(s)"
    }))

    primer_apellido = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Primer Apellido"
    }))

    segundo_apellido = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Segundo Apellido"
    }))

    celular = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Número Celular"
    }))

    como_se_entero = forms.ChoiceField(
        choices=[
            ("", "Seleccione una opción"),
            ("Radio/TV", "Radio/TV"),
            ("Facebook", "Facebook"),
            ("Amigo/Familiar o Conocido", "Amigo/Familiar o Conocido"),
            ("Impresos (Carteles y/o lonas)", "Impresos (Carteles y/o lonas)"),
            ("Otros", "Otros")
        ],
        widget=forms.Select(attrs={"class": "form-select"})
    )