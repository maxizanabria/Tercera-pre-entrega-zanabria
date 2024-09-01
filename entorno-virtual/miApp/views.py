from django.shortcuts import render
from django.http import HttpResponse
from miApp.models import Pacientes
from miApp.forms import pacientesFormulario



def inicio(req):
    return render(req, 'app/inicio.html')


def pacientes(req):
    return render(req, 'app/pacientes.html')

def consultas(req):
    return render(req, 'app/consultas.html')


def estudios(req):
    return render(req, 'app/estudios.html')

def pacientes_Formulario(req):
    if req.method == 'POST':
        # Asegúrate de que los nombres de los campos coincidan con los del formulario
        nombre = req.POST['nombre']
        apellido = req.POST['apellido']
        email = req.POST['email']
        
        if nombre and apellido:  # Verifica que los campos no estén vacíos
            pacientes = Pacientes(nombre=nombre, apellido=apellido, email=email)
            pacientes.save()
            return render(req, "app/inicio.html")
        else:
            # Puedes agregar un mensaje de error o manejar este caso de alguna forma
            pass

    return render(req, "app/pacientesFormulario.html")
