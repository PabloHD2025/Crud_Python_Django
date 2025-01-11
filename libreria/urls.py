from django.urls import path
from . import views

#Configuramos las rutas de las paginas que conforman la app.
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('libros', views.libros, name='libros'),
    path('paginas', views.nosotros, name='nosotros'),
    

]
