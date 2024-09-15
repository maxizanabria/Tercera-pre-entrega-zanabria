from django.shortcuts import render
from django.http import HttpResponse
from miApp.models import Pacientes
from miApp.forms import pacientesFormulario
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView





# vistas de proyecto



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('inicio') 
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})



def login(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes estar registrado para acceder a esta página.')
    return render(request, 'app/login.html')


class CustomLoginView(LoginView):
    template_name = 'app/login.html'  


def inicio(req):
    return render(req, 'app/inicio.html')

@login_required(login_url='login')
def pacientes(req):
    return render(req, 'app/pacientes.html')


@login_required(login_url='login')
def consultas(req):
    return render(req, 'app/consultas.html')

@login_required(login_url='login')
def estudios(req):
    return render(req, 'app/estudios.html')

@login_required(login_url='app/login.html')
def pacientes_Formulario(req):
    if req.method == 'POST':
        
        nombre = req.POST['nombre']
        apellido = req.POST['apellido']
        email = req.POST['email']
        
        if nombre and apellido:  
            pacientes = Pacientes(nombre=nombre, apellido=apellido, email=email)
            pacientes.save()
            return render(req, "app/inicio.html")
        else:
            
            pass

    return render(req, "app/pacientesFormulario.html")

@login_required(login_url='app/login.html')
def pacientes_Form_2(request):

    if request.method == "POST":

            miFormulario = pacientesFormulario(request.POST) 
            print(miFormulario)

            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                pacientes = Pacientes(nombre=informacion["pacientes"], apellido=informacion["apellido"], email = informacion.get("email", None))
                
                pacientes.save()
                return render(request, "app/inicio.html")
    else:
            miFormulario = pacientesFormulario()

    return render(request, "app/pacientes-Form-2.html", {"miFormulario": miFormulario})

@login_required(login_url='app/login.html')
def busquedaPacientes(request):
    return render(request, "app/busquedaPacientes.html")

@login_required(login_url='app/login.html')
def buscar(request):

    if request.GET["apellido"]:

        apellido = request.GET['apellido']

        pacientes = Pacientes.objects.filter(apellido__icontains=apellido)

        return render(request, "App/resultadoBusqueda.html", {"pacientes": pacientes, "apellido": apellido})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

@login_required(login_url='app/login.html')
def leerPacientes(request):

    pacientes = Pacientes.objects.all() # TRAE PACIENTES

    contexto= {"pacientes":pacientes} 

    return render(request, "App/leerPacientes.html",contexto)

@login_required(login_url='app/login.html')
def eliminarPacientes(request, pacientes_nombre):

    pacientes = pacientes.objects.get(nombre=pacientes_nombre)
    pacientes.delete()

    # RETORNA AL MENU 
    pacientes = pacientes.objects.all()  # trae todos los pacientes 

    contexto = {"pacientes": pacientes}

    return render(request, "app/leerPacientes.html", contexto)

@login_required(login_url='app/login.html')
def pacientesFormulario(request):  
    
    
    

    print("Entrando en la vista pacientesFormulario")  

    if request.method == 'POST':
        print("Solicitud POST recibida")

        miFormulario = pacientesFormulario(request.POST) 

        if miFormulario.is_valid():
            print("Formulario válido")  

            informacion = miFormulario.cleaned_data
            pacientes = Pacientes(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], )
            pacientes.save()

            return render(request, "app/inicio.html") 
        else:
            print("Formulario no válido")  

    else:
        print("Solicitud GET recibida")  
        miFormulario = pacientesFormulario()

    return render(request, "app/pacientesFormulario.html", {"miFormulario": miFormulario})