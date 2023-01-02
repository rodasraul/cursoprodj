from unittest.util import _MIN_COMMON_LEN
from django.db import models
from ckeditor.fields import RichTextField
from django.forms import ImageField

from applications.departamento.models import Departamento

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades del empleado'

    def __str__(self):
        return str(self.id) + ' - ' + self.habilidad

class Empleado(models.Model):
    """ Modelo para tabla empleado """
    # Lista de opciones para JOB
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
        ('4', 'Ingeniero'),
        ('5', 'Abogado'),
        ('6', 'Técnico'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres completos',
        max_length=120,
        blank=True
    )
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    # Personalizar el modelo en el admin de django
    class Meta:
        verbose_name = 'Trabajadores de la empresa'
        verbose_name_plural = 'Colaboradores'
        ordering = ['last_name', '-first_name']
        # VERIFICAR que no haya valores duplicados en estos campos
        unique_together = ('last_name', 'first_name')


    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' ' + self.last_name