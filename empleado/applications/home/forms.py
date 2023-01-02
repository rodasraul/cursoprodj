# Paquete que ayudara a crear formulario
# Creare codigo en python
# Conectar campos definidos en el modelo con las vistas creas en views
from django import forms
# importamos el modelo prueba
from .models import Prueba

class PruebasForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""
        model = Prueba
        #fields = ('__all__')
        fields = [ 
            'titulo',
            'subtitulo',
            'cantidad',
            ]
        # Widgets para personalizar una variable, es un DICCIONARIO
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingreso texto aquí',
                }
            ),
            'subtitulo': forms.TextInput(
                attrs = {
                    'placeholder': 'Sub titulo aqui....',
                }
            ),
        }
        
    # Metodo para validar el campo cantidad
    # Las validaciones deben hacerse en los formularios
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        # Validamos el valor ingresado en cantidad
        if cantidad < 10:   
            # Mostramos un mensaje de error si el valor no cumple condicion
            raise forms.ValidationError('Ingrese numero mayor a 10')
        # Si el valor es de 10 a mas se hace el return de cantidad
        return cantidad
