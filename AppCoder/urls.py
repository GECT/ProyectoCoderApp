from django.contrib import admin
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_cursos, name="inicio"),    
    path('', inicio, name="inicio"),
    path('curso/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"), 
    path('cursoFormulario/', cursoFormulario, name="cursoFormulario"),
    path('profesoresFormulario/', profesoresFormulario, name="profesoresFormulario"),
    path('registroExitoso/', registroExitoso, name="registrado"),
    path('registroMal/', registroMal, name="registroMal"),
]
