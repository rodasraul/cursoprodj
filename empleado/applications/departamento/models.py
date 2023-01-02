from django.db import models

# Create your models here.
# Modelo o Tabla de BD
class Departamento(models.Model):
    # ('Nombre') => nombre como se vera en el admin de django
    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    # Personalizar aspecto del modelo en el admin de DJANGO
    class Meta:
        # Django agregara la S al final del nombre
        verbose_name = 'Oficinas de la empresa'
        # En plural
        verbose_name_plural = 'Areas de la empresa'
        # Ordenando los registros en base al campo
        ordering = ['-name']
        # No se registrara combinacion de campos iguales
        unique_together = ('name', 'shor_name')

    def __str__(self):
        #return str(self.id) + ' ' + self.name + ' - ' + self.shor_name
        return self.name + ' - ' + self.shor_name

