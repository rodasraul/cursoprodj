from django.shortcuts import render
from django.views.generic import ListView

# Importamos el FormView para trabajar con la vista generica simple
from django.views.generic.edit import FormView

# Importamos el modelo Empleado de otra aplicacion, haremos registro de datos
from applications.persona.models import Empleado

# Importamos el modelo Departamento, haremos registro de datos
from .models import Departamento

# Importamos el formulario que acabamos de crear
from .forms import NewDepartamentoForm

# Create your views here.


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'

# Vista generica FormView, guarda dos modelos (tablas)
class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    # Hacemos referencia al formulario que creamos en forms.py
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('************** Estamos en el FORM VALID*************')

        # Procesando en modelo DEPARTAMENTO
        # Departamento pertenece a otro modelo, necesitamos 1 instancia de ese modelo
        # Variable depa utiliza la clase Departamento
        #con esto ya se creo una instancia para departamento
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
        )
        # Con el metodo save() guardamos el valor en la BD
        depa.save()

        # Procesando en modelo EMPLEADO
        # Una forma de crear los registros es recuperar variables y asignarlo a cada campo 
        #Recuperamos datos que se envian por POST de Empleado desde forms.py
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']

        # Importamos del modelo Empleado de la otra aplicacion
        # Para crear un registro de la tabla empleado
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '3',
            departamento = depa,
            full_name = nombre + ' ' + apellido
        )
        return super(NewDepartamentoView, self).form_valid(form)
