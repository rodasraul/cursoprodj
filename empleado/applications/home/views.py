from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

#from applications.home.models import Prueba
from .models import Prueba

#Importamos el forms.py que enlazaremos - el formulario PruebaForm
from .forms import PruebasForm

# Create your views here.
class InicioView(TemplateView):
    template_name = 'inicio.html'

class IndexView(TemplateView):
    template_name = 'home/home.html'

class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ['A', 'B', 'C']
    context_object_name = 'lista_prueba'

class ModeloPruebaListView(ListView):
    # Cumpliendo el modelo MVT Model View Template
    model = Prueba # Modelo de donde extrae los datos
    template_name = "home/pruebas.html" # Template Salida en HTML
    context_object_name = 'lista_prueba' # Variable que se enviara al HTML

class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    #fields = ('__all__')
    #fields = [ 'titulo', 'subtitulo', 'cantidad' ]
    # Con esta linea enlazamos al nuevo formulario que hemos creado
    form_class = PruebasForm
    # Cuando complete se diriga a la pagina principal
    success_url = '/'

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'

class PruebaHome1View(TemplateView):
    template_name = 'home/home1.html'

class PruebaHome2View(TemplateView):
    template_name = 'home/home2.html'

class PruebaHome3View(TemplateView):
    template_name = 'home/home3.html'
