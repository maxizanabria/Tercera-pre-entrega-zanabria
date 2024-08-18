from django.shortcuts import render
from django.http import HttpResponse



def inicio(req):
    return render(req, 'app/inicio.html')


def pacientes(req):
    return render(req, 'app/pacientes.html')

def consultas(req):
    return render(req, 'app/consultas.html')


def estudios(req):
    return render(req, 'app/estudios.html')