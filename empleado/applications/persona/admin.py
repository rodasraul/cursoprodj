from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)

# Personalizar la tabla en el admin de django
class EmpleadoAdmin(admin.ModelAdmin):
    # Solo se llaman a los atributos que existen en el modelo
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    # Para llamar a full_name creare una funcion que le de el valor
    def full_name(self, obj):
        print(obj.first_name)
        return obj.first_name + ', ' + obj.last_name

    # Agregamos filtro para buscar en la tabla en el mismo admin de django
    search_fields = ('first_name',)
    list_filter = ('departamento', 'job','habilidades',)

    # Filtro horizontal abrira otro cuadro donde se agregaran las habilidades
    filter_horizontal = ('habilidades',)

# Agregamos la clase con las columnas a mostrar en el admin de django
admin.site.register(Empleado, EmpleadoAdmin)
