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

def pacientes_Form_2(request):

    if request.method == "POST":

            miFormulario = pacientesFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                pacientes = Pacientes(nombre=informacion["pacientes"], apellido=informacion["apellido"], email = informacion.get("email", None))
                
                pacientes.save()
                return render(request, "app/inicio.html")
    else:
            miFormulario = pacientesFormulario()

    return render(request, "app/pacientes-Form-2.html", {"miFormulario": miFormulario})


def busquedaPacientes(request):
    return render(request, "app/busquedaPacientes.html")

def buscar(request):

    if request.GET["apellido"]:

        apellido = request.GET['apellido']

        pacientes = pacientes.objects.filter(apellido__icontains=apellido)

        return render(request, "App/resultadoBusqueda.html", {"pacientes": pacientes, "apellido": apellido})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)