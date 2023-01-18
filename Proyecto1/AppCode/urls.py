from django.urls import path
from AppCode import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('odontologos', views.odontologos, name="Odontologos"),
    path('listarodontologos', views.listar_odontologos, name="ListarOdontologos"),
    path('buscarodontologos', views.buscar_odontologos, name="BuscarOdontologos"),
    path('pacientes', views.pacientes, name="Pacientes"),
    path('listarpacientes', views.listar_pacientes, name="ListarPacientes"),
    path('buscarpacientes', views.buscar_pacientes, name="BuscarPacientes"),
    path('turnos', views.turnos, name="Turnos"),
    path('listarturnos', views.listar_turnos, name="ListarTurnos"),
    path('buscarturnos', views.buscar_turnos, name="BuscarTurnos"),
  
]