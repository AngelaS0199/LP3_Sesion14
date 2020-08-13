from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Articulo
from django.db.models import Q
# Create your views here.

layout = """
"""

def index(request):
    estudiantes = ['Angela Centeno',
                    'Alejandro Hermitaño',
                    'Isabella Caballero',
                    'Alexandra Huallcca']
    return render(request,'index.html',{
        'titulo':'Inicio',
        'mensaje':'Proyecto web con Django(Desde Views)',
        'estudiantes':estudiantes
    })

def saludo(request):
    return render(request,'saludo.html',{
        'titulo':'Saludo',
        'autor_saludo':'Angela Stephany Centeno Macalupu'
    })

def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request,'rango.html',{
        'titulo': 'Rango',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })

def rango2(request,a=0,b=100):
    if a>b:
        return redirect('rango2',a=b, b=a)

    resultado = f"""
        <h2> Numeros de [{a},{b}] </h2>
        Resultado: <br>
        <ul> 
    """
    
    while a<=b:
        resultado +=  f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(layout + resultado)

def crear_articulo(request, titulo, contenido, publicado):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")

def buscar_articulo(request):
    try:
        articulo = Articulo.objects.get(id=6)
        resultado = f"Articulo: <br>ID:{articulo.id} <br>Título: {articulo.titulo} <br>Contenido: {articulo.contenido}" 
    except:
        resultado: "<h1> Articulo No encontrado </h1>"
    return HttpResponse(resultado)

def editar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)

    articulo.titulo = "Enseñanza OnLine en la Untels"
    articulo.contenido = "Aula Virtual. Google Meet. Portal Académico. Correo Institucional"
    articulo.publicado = False

    articulo.save()
    return HttpResponse(f"Articulo Editado:  <br>ID:{articulo.id} <br>Nuevo Título: {articulo.titulo} <br>Nuevo Contenido: {articulo.contenido}")

def listar_articulos(request):
    #articulos = Articulo.objects.all()
    #articulos = Articulo.objects.filter(titulo__contains = "PHP")
    #articulos = Articulo.objects.filter(titulo__contains = "PHP").exclude(publicado=False)
    #articulos = Articulo.objects.filter(titulo__contains="Java")
    #articulos = Articulo.objects.filter(titulo__exact="Java")
    #articulos = Articulo.objects.filter(id__gt=6)
    #articulos = Articulo.objects.filter(id__gte=6)
    #articulos = Articulo.objects.filter(id__lt=6)
    #articulos = Articulo.objects.filter(id__lte=6)
    #articulos = Articulo.objects.order_by('titulo')
    #articulos = Articulo.objects.order_by('-titulo')
    #articulos = Articulo.objects.order_by('titulo')[:3]
    #articulos = Articulo.objects.order_by('titulo')[3:6]
    articulos = Articulo.objects.filter(
        Q(titulo__contains = "Java")|Q(titulo__contains = "PHP")
    )
    return render(request,'listar_articulos.html',{
        'articulos': articulos,
        'titulo': 'Listado de Articulos'
    })

def eliminar_articulos(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect('listar_articulos')

def save_articulo(request):
    articulo = Articulo(
        titulo = titulo,
        contenido = contenido,
        publicado = publicado
    )
    articulo.save()
    return HttpResponse(f"Articulo Creado: {articulo.titulo} - {articulo.contenido}")

def create_articulo(request):
    return render(request, 'create_articulo.html')