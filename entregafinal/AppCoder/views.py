from django.shortcuts import render
from .models import Curso, Profesor, Estudiante, Entregable
from  django.http import HttpResponse
from .forms import Cursoform, ProfesorForm, EstudiantesForm, EntregablesForm

#def crear_curso(request):
    #nombre_curso="Programación básica"
    #comision_curso= 190300
    #curso = Curso(nombre=nombre_curso, comision= comision_curso)
    #curso.save()
   # respuesta = f"Curso creado: {curso.nombre}  -  {curso.comision}"
    #return HttpResponse(respuesta)
# Create your views here.


#def listar_cursos(request):
   # cursos = Curso.objects.all()
    #respuesta=""
    #for curso in cursos:
       # respuesta += f"{curso.nombre} - {curso.comision}<br>"
   # return HttpResponse(respuesta)


def inicio(request):
    
    return render(request,"AppCoder/inicio.html")   

def profesores(request):
    if request.method== "POST":
        form=ProfesorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            email = info["email"]
            profesion = info["profesion"]
            profesor= Profesor(nombre=nombre,apellido=apellido,email=email,profesion=profesion)
            profesor.save()
            formulario_profesor = ProfesorForm()
            return render(request,"AppCoder/profesores.html",{"mensaje":"Profesor creado con éxito", "formulario":formulario_profesor})
        
        else:
            return render(request,"AppCoder/profesores.html",{"mensaje":"Datos invalidos"})
    else:
        formulario_profesor = ProfesorForm()

    return render(request, "AppCoder/profesores.html",{"formulario":formulario_profesor})


def estudiantes(request):
    if request.method== "POST":
        form=EstudiantesForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            email = info["email"]
            estudiantes= Estudiante(nombre=nombre,apellido=apellido,email=email)
            estudiantes.save()
            formulario_estudiantes = EstudiantesForm()
            return render(request,"AppCoder/estudiantes.html",{"mensaje":"Estudiante creado con éxito", "formulario":formulario_estudiantes})
        
        else:
            return render(request,"AppCoder/estudiantes.html",{"mensaje":"Datos invalidos"})
    else:
        formulario_estudiantes = EstudiantesForm()

    return render(request, "AppCoder/estudiantes.html",{"formulario":formulario_estudiantes})
    

def cursos(request):

    if request.method=="POST":
        #nombre = request.POST["nombre"]
        #comision = request.POST["comision"]
        form =Cursoform(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre= info["nombre"]
            comision= info["comision"]
            curso =Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request,"AppCoder/cursos.html", {"mensaje":"Curso creado con éxito"})
        return render(request,"AppCoder/cursos.html",{"mensaje":"Datos incorrectos"})
    else:
        formulario_curso=Cursoform()
        return render(request,"AppCoder/cursos.html", {"formulario":formulario_curso})

    
#def cursos(request):
   # cursos = Curso.objects.all()
   # return render(request,"AppCoder/cursos.html",{"cursos":cursos})

def entregables(request):
    if request.method== "POST":
        form=EntregablesForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            fecha_entrega = info["fecha_entrega"]
            entregado = info["entregado"]
            entregables= Entregable(nombre=nombre,fecha_entrega=fecha_entrega,entregado=entregado)
            entregables.save()
            formulario_entregables = EntregablesForm()
            return render(request,"AppCoder/entregables.html",{"mensaje":"Entrega creada con éxito", "formulario":formulario_entregables})
        
        else:
            return render(request,"AppCoder/entregables.html",{"mensaje":"Datos invalidos"})
    else:
        formulario_entregables = EntregablesForm()

    return render(request, "AppCoder/entregables.html",{"formulario":formulario_entregables})


def busquedaComision(request):
     return render(request,"AppCoder/busquedaComision.html")

def buscar(request):
    comision=request.GET["comision"]
    if comision!="":
        cursos = Curso.objects.filter(comision=comision)
        return render(request,"AppCoder/resultadosBusqueda.html",{"cursos":cursos})
    else:
        return render(request,"AppCoder/busquedaComision.html",{"mensaje":"Por favor ingrese una comisión"})
    pass