from django.shortcuts import render
from .models import Curso
from  django.http import HttpResponse

def crear_curso(request):
    nombre_curso="Programación básica"
    comision_curso= 190300
    curso = Curso(nombre=nombre_curso, comision= comision_curso)
    curso.save()
    respuesta = f"Curso creado: {curso.nombre}  -  {curso.comision}"
    return HttpResponse(respuesta)
# Create your views here.


def listar_cursos(request):
    cursos = Curso.objects.all()
    respuesta=""
    for curso in cursos:
        respuesta += f"{curso.nombre} - {curso.comision}<br>"
    return HttpResponse(respuesta)