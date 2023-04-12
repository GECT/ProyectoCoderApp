from django.shortcuts import render
from .models import Curso, Profesor
from django.http import HttpResponse
from .forms import CursoFormulario, ProfesorFormulario 
# Create your views here.

def curso(self, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    return HttpResponse(f"""           
        <p>Curso: {curso.nombre} - {curso.camada} creado!<p/>
    """)
    
def lista_cursos(self):
    lista = Curso.objects.all()
    return render(self, "lista_cursos.html", {"lista_cursos": lista})

def cursos(self):
    lista = Curso.objects.all()    
    return render(self, "cursos.html",{"lista_cursos": lista})

def lista_profesores(self):
    lista = Profesor.objects.all()
    return render(self, "profesores.html", {"lista_profesores": lista})

def profesores(self):
    lista = Profesor.objects.all()  
    return render(self, "profesores.html", {"lista_profesores": lista})

def inicio(self):
    return render(self, "inicio.html")

def registroExitoso(self):
    return render(self, "registrado.html")

def registroMal(self):
    return render(self, "registroMal.html")

def estudiantes(self):
    return render(self, "estudiantes.html")

def entregables(self):
    return render(self, "entregables.html")

#formulario hecho con HTML

# def cursoFormulario(request):
#     print("method: ", request.method)
#     print("POST: ", request.POST)
#     if request.method == "POST":
#         curso = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
#         curso.save()
#         return render(request, "registrado.html")
#     return render(request, "cursoFormulario.html")

#formulario hecho con django, con el metodo form y todo lo demas, que verifique si la data es valida y la salve

def cursoFormulario(request):
    print("method: ", request.method)
    print("POST: ", request.POST)
    if request.method == "POST":
        miformulario = CursoFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid():
            data = miformulario.cleaned_data
            curso = Curso(nombre=data["curso"], camada=data["camada"])
            curso.save()
            return render(request, "registrado.html")
        else:
            return render(request, "registroMal.html")
    else:
        miformulario = CursoFormulario()        
        return render(request, "cursoFormulario.html",{"miFormulario": miformulario})

def profesoresFormulario(request):
    print("method: ", request.method)
    print("POST: ", request.POST)
    if request.method == "POST":
        miformulario2 = ProfesorFormulario(request.POST)
        print(miformulario2)
        if miformulario2.is_valid():
            data = miformulario2.cleaned_data
            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            profesor.save()
            return render(request, "registrado.html")
        else:
            return render(request, "registroMal.html")
    else:
        miformulario2 = ProfesorFormulario()        
        return render(request, "profesoresFormulario.html",{"miFormulario2": miformulario2})