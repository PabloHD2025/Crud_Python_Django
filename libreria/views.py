from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html') #Renderiza el archivo inicio.html

def libros(request):
    return render(request, 'libros/index.html') #Renderiza el archivo index.html

def nosotros(request):
    return render(request, 'paginas/nosotros.html') #Renderiza el archivo nosotros.html



