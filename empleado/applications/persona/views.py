from django.shortcuts import render
# El paquete reverse_lazy es la mejor práctica para redirigir a paginas
# Se necesitara colocar nombre a los URL
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Empleado

# 1. Listar todos los empleados de la empresa.
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    # Indicar tamaño de bloques paginacion
    paginate_by = 10
    # Ordenando los resultados
    ordering = ['first_name', 'last_name']
    model = Empleado
    context_object_name = 'lista'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        lista = Empleado.objects.filter(
            # icontains, busca una cadena DENTRO de otra, incluso mayusculas y minusculas
            #full_name__icontains = palabra_clave
            first_name__icontains = palabra_clave
        )
        return lista
        
class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    # Indicar tamaño de bloques paginacion
    paginate_by = 10
    # Ordenando los resultados
    ordering = ['last_name', 'first_name']
    model = Empleado
    context_object_name = 'empleadoslista'


# 2. Listar todos los empleados que pertenecen a un area de la empresa.
class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    # La PEOR forma de hacer filtrado
    #queryset = Empleado.objects.filter(
        #departamento__shor_name = 'OIS'
        #departamento__name = 'Economia y Finanzas'
    #)
    context_object_name = 'empleados'
    # Mejor forma de hacer filtrado
    def get_queryset(self):
        # Recoger un argumento que envian por la URL
        area = self.kwargs['corto']
        lista = Empleado.objects.filter(
            #departamento__shor_name = 'OIS'
            #departamento__shor_name = 'OEF'
            departamento__shor_name=area
        )
        return lista

# 3. Listar empleados por trabajo.
class ListEmpleadoByTrabajo(ListView):
    template_name = 'persona/empleado_by_trabajo.html'
    context_object_name = 'trabajo'
    
    def get_queryset(self):
        clave_trabajo = self.request.GET.get("kwork", '')
        trabajo = Empleado.objects.filter(
            job=clave_trabajo
        )
        #print(trabajo)
        return trabajo

# 4. Listar los empleados por palabra clave.
class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('**************************')
        # self
        # request -> solicitudes enviadas al servidor, es objeto completo. 
        # GET -> (metodo) 
        # get -> (submetodo) recupera al identificador (id) "kword". Se agrega coma y '' porque es una TUPLA.
        palabra_clave = self.request.GET.get("kword", '')
        #print('=============\n', palabra_clave)
        # FILTRAMOS los datos, de un CONJUNTO DE REGISTROS (varios)
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        #print('LISTA RESULTADO:\n', lista)
        return lista

# 5. Listar habilidades de un empleado.
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        # Filtramos los datos de UN SOLO empleado (recupera un solo registro)
        empleado = Empleado.objects.get(id=56)
        #print(empleado.habilidades.all())
        return empleado.habilidades.all()

# DetailView es muy similar al ListView
# Es para ver los detalles (campos) de un registro
class DetalleEmpleado(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    # Intervenir un metodo, redifinirlo
    def get_context_data(self, **kwargs):
        context = super(DetalleEmpleado, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

# Plantilla que servira para redirigir luego que se agrego un registro
class SuccessView(TemplateView):
    template_name = "persona/success.html"

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    # OBLIGATORIO para el CreateView
    # para cargar campos determinados
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'image', ]
    # Agrega TODOS LOS CAMPOS del Modelo
    # fields = ('__all__')
    # CREATEVIEW necesita el success_url para redireccionar cuando se completo la ejecucion del formulario
    #success_url = '/success/' 
    success_url = reverse_lazy('persona_app:empleados_all') # Usamos etiquetas reverse_Lazy con nombre
    # '.' para que se cargue en la misma pagina.
    # No es bueno hacer esta redireccion, se debe hacer de la siguiente manera:

    # Este metodo es para interceptar el registro que se envía a la BD del modelo
    def form_valid(self, form):
        # declaramos la variable empleado y recuperamos la instancia vinculada a la BD
        empleado = form.save()
        # form.save(), a este momento el registro ya esta guardado en la BD, ahora lo podemos utilizar, y como muestra es que lo imprimimos
        # print(empleado)
        # A la instancia empleado que habiamos recuperado, estamos actualizado su valor full_name, solo en la variable
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        # la variable empleado -al ser una instancia del modelo empleado- se invoca al metodo SAVE() para que sus valores se actualicen, de esta manera el full_name se actualizara con el último valor creado
        empleado.save()
        # Se esta trabajando dentro de la vista generica
        return super(EmpleadoCreateView, self).form_valid(form)
    
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    # Para modificar - actualizar TODOS los campos
    #fields = ('__all__')
    # Para Actualizar-Modificar determinados campos
    fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'image', ]
    # Luego de guardarse correctamente se direcciona a la URL CORRECTO
    #success_url = reverse_lazy('persona_app:correcto')
    # Luego de guardarse correctamente se direcciona a la pagina empleados_admin
    success_url = reverse_lazy('persona_app:empleados_admin')

    # Para interceptar los valores antes que se guarden
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('********* METODO POST ********')
        print('==============================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('********** FORM VALID ********')
        print('******************************')
        empleados = form.save()
        empleados.full_name = empleados.first_name + ' ' + empleados.last_name
        empleados.save()
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    # Luego de guardarse correctamente se direcciona a la URL CORRECTO
    #success_url = reverse_lazy('persona_app:correcto')
    # Luego de guardarse correctamente se direcciona a la pagina empleados_admin
    success_url = reverse_lazy('persona_app:empleados_admin')

    

