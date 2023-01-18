from django import forms


class OdontologoFormulario(forms.Form):
    #Especificar los campos
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    numero_matricula = forms.IntegerField()


class PacienteFormulario(forms.Form):   
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    dni= forms.IntegerField()
    edad = forms.IntegerField()
    email= forms.EmailField()

class TurnoFormulario(forms.Form):
    fecha= forms.DateField()
    dni_paciente= forms.IntegerField()
    apellido_doctor= forms.CharField(max_length=50)
