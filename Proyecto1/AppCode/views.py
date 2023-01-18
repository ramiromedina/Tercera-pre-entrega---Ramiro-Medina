from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCode.models import Odontologo, Paciente, Turno
from AppCode.forms import OdontologoFormulario, PacienteFormulario, TurnoFormulario
from django.db.models import Q

# Create your views here.
def inicio(request):
      return render(request, "AppCode/inicio.html")

def odontologos(request):
      if request.method == 'POST':

            miFormulario = OdontologoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  odonto = Odontologo (nombre=informacion['nombre'], apellido=informacion['apellido'],
                  numero_matricula=informacion['numero_matricula']) 

                  odonto.save()

                  return render(request, "AppCode/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= OdontologoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCode/odontologos.html", {"miFormulario":miFormulario})

def listar_odontologos(request):
    contexto = {
        'odontologos': Odontologo.objects.all()
    }
    return render(
        request=request,
        template_name='AppCode/listar_odontologos.html',
        context=contexto,
    )


def buscar_odontologos(request):
    if request.method == "POST":
        data = request.POST
        odontologos = Odontologo.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(apellido__contains=data['busqueda']) | Q(numero_matricula__contains=data['busqueda']))
        contexto = {
            'odontologos': odontologos
        }
        return render(
            request=request,
            template_name='AppCode/listar_odontologos.html',
            context=contexto,
      )

def pacientes(request):
      if request.method == 'POST':

            miFormulario = PacienteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  paciente = Paciente (nombre=informacion['nombre'], apellido=informacion['apellido'],
                  dni=informacion['dni'], edad=informacion['edad'], email=informacion['email']) 

                  paciente.save()

                  return render(request, "AppCode/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= PacienteFormulario() #Formulario vacio para construir el html

      return render(request, "AppCode/pacientes.html", {"miFormulario":miFormulario})

def listar_pacientes(request):
    contexto = {
        'pacientes': Paciente.objects.all()
    }
    return render(
        request=request,
        template_name='AppCode/listar_pacientes.html',
        context=contexto,
    )


def buscar_pacientes(request):
    if request.method == "POST":
        data = request.POST
        pacientes = Paciente.objects.filter(
            Q(nombre__contains=data['busqueda']) | Q(apellido__contains=data['busqueda']) | Q(dni__contains=data['busqueda'])
            | Q(edad__contains=data['busqueda']) | Q(email__contains=data['busqueda']))
        contexto = {
            'pacientes': pacientes
        }
        return render(
            request=request,
            template_name='AppCode/listar_pacientes.html',
            context=contexto,
      )

def turnos(request):
      if request.method == 'POST':

            miFormulario = TurnoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  turno = Turno (fecha=informacion['fecha'], apellido_doctor=informacion['apellido_doctor'],
                  dni_paciente=informacion['dni_paciente']) 

                  turno.save()

                  return render(request, "AppCode/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= TurnoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCode/turnos.html", {"miFormulario":miFormulario})

def listar_turnos(request):
    contexto = {
        'turnos': Turno.objects.all()
    }
    return render(
        request=request,
        template_name='AppCode/listar_turnos.html',
        context=contexto,
    )


def buscar_turnos(request):
    if request.method == "POST":
        data = request.POST
        turnos = Turno.objects.filter(
            Q(fecha__contains=data['busqueda']) | Q(apellido_doctor__contains=data['busqueda']) | Q(dni_paciente__contains=data['busqueda']))
        contexto = {
            'turnos': turnos
        }
        return render(
            request=request,
            template_name='AppCode/listar_turnos.html',
            context=contexto,
      )
