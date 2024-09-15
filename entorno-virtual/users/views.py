from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout as auth_logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect('inicio')  
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'login.html'

def logout_view(request):
    auth_logout(request)
    return redirect('inicio')


