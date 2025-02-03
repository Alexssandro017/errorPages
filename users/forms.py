from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.core.validators import RegexValidator
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'surname', 'control_number', 'age', 'tel', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico',
                'required': True,
                'pattern': r'^[a-zA-Z0-9]+@utez\.edu\.mx$',
                'title': 'Debe ingresar un correo válido (ejemplo@utez.edu.mx)'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre',
                'required': True,
                'minlength': 3,
                'maxlength': 50
            }),
            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido',
                'required': True,
                'minlength': 3,
                'maxlength': 50
            }),
            'control_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de control',
                'required': True,
                'pattern': r'^\d{5}[a-zA-Z]{2}\d{3}$',
                'title': 'Debe contener 10 dígitos numéricos y formato correcto (ejemplo: 12345ab678)'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edad',
                'required': True,
                'min': 18,
                'max': 99,
                'title': 'Debe ser mayor de edad'
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teléfono',
                'required': True,
                'pattern': r'^\d{10}$',
                'title': 'Debe contener exactamente 10 dígitos'
            }),
        }
       

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