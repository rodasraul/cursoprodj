# Para trabajar con formularios
from django import forms

# Formulario que NO depende de la tabla de BD
class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    shorname = forms.CharField(max_length=20)
    