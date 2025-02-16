from django.db import models

# Create your models here.

class Producto(models.Model):
    #Aqui va los atributos de mi clase
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    #Que los campos urlsfields limitan los caracteres a 200 por defecto
    imagen = models.URLField()

    #Cuando imprimamos un objeto de tipo producto
    def __str__(self):
        return self.nombre