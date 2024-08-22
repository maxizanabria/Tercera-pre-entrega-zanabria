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

            pacientes =  pacientesFormulario(nombre=req.POST['curso'],apellido=req.POST['apellido'])

            pacientes.save()

            return render(req, "app/inicio.html")

    return render(req,"app/pacientesFormulario.html")