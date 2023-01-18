from django.urls import path
from AppCode import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('odontologos', views.odontologos, name="Odontologos"),
    path('pacientes', views.pacientes, name="Pacientes"),
    path('turnos', views.turnos, name="Turnos"),
    path('buscar/', views.buscar),
  
]