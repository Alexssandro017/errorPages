from django.shortcuts import render, redirect
import json
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomUserLoginForm
from django.contrib.auth.decorators import login_required
from .message import message  # Asegúrate de que la clase Message esté correctamente importada
from django.contrib import messages
from .forms import CustomUserCreationForm  # Asegúrate de que tienes este formulario

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect("login")  # Cambia "login" por la URL de inicio de sesión
        else:
            # Capturar errores y enviarlos al frontend
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = CustomUserCreationForm()
    
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)

    # Creamos un mensaje de tipo "info"
    msg = message(
        "info",
        "Se ha cerrado sesión exitosamente",
        200,
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8MIbugIhZBykSmQcR0QPcfnPUBOZQ6bm35w&s"
    )

    # Pasamos el mensaje en formato JSON al template
    return render(request, "login.html", {"message": json.dumps(msg.to_dict())})

@login_required
def home_view(request):
    return render(request, 'home.html')