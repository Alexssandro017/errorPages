#Que define los formularios de los modelos en esta app
from django import forms
from .models import Producto

#Se debe de crear una clase para cada modelo
class productoForm(forms.ModelForm):
    #Meta es la clase que define la meta-informacion del formulario
    class Meta:
        #De que modelo se basa este formulario
        model = Producto

        #Que campos se van a ver en el formulario
        fields = ['nombre', 'precio', 'imagen']

        #Personalizar la pariencia del formulario (widgets)
        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form-input',
                    'placeholder': 'Nombre del producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Precio del prodcuto'
                }
            ),
            'imagen': forms.URLInput(
                attrs={
                    'class': 'form-input',
                    'placeholder': 'Imagen del producto'
                }
            )
        }

        #Para personalizar las etiquetas
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio (MXN)',
            'imagen': 'URL de la imagen'
        }

        #Mensajes de error
        error_messages = {
            'nombre': {
                'required': 'El nombre es obligatorio.'
            },
            'precio':{
                'required': 'El precio no puede estar vacio',
                'invalid': 'Ingresa un numero valido.'
            }
        }