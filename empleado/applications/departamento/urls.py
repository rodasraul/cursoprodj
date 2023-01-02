from django.contrib import admin
from django.urls import path

from . import views

app_name = 'app_dpto'

urlpatterns = [
    path(
        'new-departamento/',
        views.NewDepartamentoView.as_view(),
        name='nuevo_departamento'
    ),
    path(
        'departamento_lista',
        views.DepartamentoListView.as_view(),
        name='departamento_list'
    ),
]