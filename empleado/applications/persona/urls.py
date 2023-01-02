from django.contrib import admin
from django.urls import path

from . import views
# usando reverse_lazy debemos especificar la etiqueta NAME de una URL

# Usando reverse_lazy definimos la variable para todo el conjunto de URL
# La convencion recomienda usar el nombre del modelo seguido de _app
app_name = "persona_app"
urlpatterns = [
     path(
          'lista-todo-empleados/', 
          views.ListAllEmpleados.as_view(),
          name='empleados_all'
     ),
     path(
          'lista-by-area/<corto>', 
          views.ListByAreaEmpleado.as_view(),
          name='empleados_area'
     ),
     path(
          'lista-empleados-admin',
          views.ListaEmpleadosAdmin.as_view(),
          name='empleados_admin'
     ),
     path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
     path('listar-habilidades/', views.ListHabilidadesEmpleado.as_view()),
     path('listar-por-trabajo/', views.ListEmpleadoByTrabajo.as_view()),
     path(
          'ver-empleado/<pk>/', 
          views.DetalleEmpleado.as_view(),
          name='empleado_detail'
     ),
     path(
          'add-empleado/',
          views.EmpleadoCreateView.as_view(),
          name='empleado_agrega'
     ),
     path(
          'success/', 
          views.SuccessView.as_view(), 
          name='correcto'
     ),
     path(
          'update-empleado/<pk>/',
          views.EmpleadoUpdateView.as_view(),
          name='modificar_empleado'
     ),
     path(
          'delete-empleado/<pk>/',
          views.EmpleadoDeleteView.as_view(),
          name='eliminar_empleado'
     ),
]
