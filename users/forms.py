from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator
from .models import CustomUser
import re

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico", max_length=150, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    name = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(label="Apellido", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Edad", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    control_number = forms.CharField(label="Número de control", max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tel = forms.CharField(label="Teléfono", max_length=10,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']

    def clean(self):
        print("Ejecutando validaciones en clean()")  # Debugging
        cleaned_data = super().clean()
        
        email = cleaned_data.get("email")
        control_number = cleaned_data.get("control_number")
        tel = cleaned_data.get("tel")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # Validar correo de UTEZ
        if email and not email.endswith("@utez.edu.mx"):
            raise forms.ValidationError("El correo debe pertenecer a @utez.edu.mx")

        # Validar matrícula (exactamente 10 caracteres)
        if control_number and re.match(r'^\d{5}[a-zA-Z]{2}\d{3}$', control_number):
            raise forms.ValidationError("La matrícula debe tener exactamente 10 caracteres.")

        # Validar teléfono (exactamente 10 dígitos)
        if tel and not re.match(r'^\d{10}$', tel):
            raise forms.ValidationError("El teléfono debe tener exactamente 10 dígitos.")

        # Validar contraseña (mínimo 8 caracteres, 1 número, 1 mayúscula y 1 carácter especial)
        if password1 and not re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&?])[A-Za-z\d!#$%&?]{8,}$', password1):
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres, 1 número, 1 mayúscula y 1 símbolo (!, #, $, %, & o ?)")

        # Validar que las contraseñas sean iguales
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data



class CustomUserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'required': True,
            'title': 'Debe ingresar un correo electrónico válido'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'required': True
        })
    )
    pass