from django.contrib import admin
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_cursos, name="inicio"),    
    path('', inicio, name="inicio"),
    path('curso/', cursos, name="cursos"),
    path('cursoFormulario/', cursoFormulario, name="cursoFormulario"),
    path('profesores/', profesores, name="profesores"),
    path('profesoresFormulario/', profesoresFormulario, name="profesoresFormulario"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('estudiantesFormulario/', estudiantesFormulario, name="estudiantesFormulario"),
    path('entregables/', entregables, name="entregables"), 
    path('registroExitoso/', registroExitoso, name="registrado"),
    path('registroMal/', registroMal, name="registroMal"),
    path('BusquedaCamada/', BusquedaCamada, name="BusquedaCamada"),
    path('Buscar/', Buscar, name="Buscar"),
]
