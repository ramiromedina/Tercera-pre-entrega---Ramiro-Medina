from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
def inicio(request):
      return render(request, "AppCode/inicio.html")

def odontologos(request):
      return render(request, "AppCode/odontologos.html")

def pacientes(request):
      return render(request, "AppCode/pacientes.html")

def turnos(request):
      return render(request, "AppCode/turnos.html")

def buscar(request):
      return render(request, "AppCode/inicio.html")