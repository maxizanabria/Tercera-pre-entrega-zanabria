from django import forms

class pacientesFormulario(forms.Form):
    pacientes = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20)
    