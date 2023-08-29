from django.urls import path
from .views import *


urlpatterns = [
path("profesores/", profesores, name ="profesores"),
path("estudiantes/", estudiantes, name = "estudiantes"),
path("cursos/", cursos, name = "cursos"),
path("entregables/", entregables, name ="entregables"),
#path("cursoFormulario/", cursoFormulario, name ="cursoFormulario"),
#path("crear_curso/", crear_curso),
#path("listar_cursos/", listar_cursos),
path("busquedaComision/", busquedaComision, name="busquedaComision"),
path("buscar/", buscar, name="buscar"),

]