from django.http import HttpResponse
from django.template import Template, Context
from miApp.models import Pacientes
from django.template import loader


def saludo(request):
    return HttpResponse("hola django ")



def probando_template(request):

    nom = "Alejandro"
    ap = "Pascual"
    
    lista_notas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



    diccionario = {"nombre": nom, "apellido": ap,  "notas": lista_notas}


    plantilla = loader.get_template('template1.html')
    
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)


def agregar_Pacientes(request, nom, apellido):
    Pacientes = Pacientes(nombre=nom, apellido=apellido)
    Pacientes.save()

    return HttpResponse("Paciente agregado")