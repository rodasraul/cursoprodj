from atexit import register
from django.contrib import admin
from .models import Prueba

# Register your models here.
# Interfaz de Admin que vera la BD Prueba
admin.site.register(Prueba)
