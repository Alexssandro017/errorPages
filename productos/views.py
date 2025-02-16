from django.shortcuts import render, redirect
from .models import Producto
from .forms import productoForm
from django.http import JsonResponse

# Create your views here.
def agregar_producto(request):
    #Checar si vengo desde el formulario enviado
    if request.method == 'POST':
        #Mandaron el formulario
        form = productoForm(request.POST)
        #Validar qu el formualrio este correcto
        if form.is_valid():
            #Si es valido lo guardo
            form.save()
            return redirect('ver') #Redirecciona a la lista de productos
    #Si no vengo de enviar el formulario (si solo lo quiero ver)
    else:
        form = productoForm()
    #Vamos a pintar el formulario
    return render(request, 'agregar.html', {'form':form})

def ver_producto(request):
    #Obetner de la DB todos los productos
    productos = Producto.objects.all()
    #Estamos devolvioendo al fornt un objeto desde el back
    return render(request, 'ver.html', {'productos': productos})

#Esta funcion pinta el html que carga los productos con JSON
def index(request):
    return render (request, 'productos.html')

#Esta otra funcion que devuelve todos los PRoductos como un JSON
def lista_productos(request):
    productos = Producto.objects.all()

    #Generar un diccionario al aire que ordene los productos
    data = [
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]

    return JsonResponse(data, safe = False)