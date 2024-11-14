from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

#def hola_mundo(request):
 #   return HttpResponse("Nos echamos intro")

from django.shortcuts import render

def mi_app(request):
    return render(request, 'mi_app/index.html')

# Define the models for 'Recurso' and 'Evento' functionalities as per the requirements.
models_content = """
from django.db import models

class Recurso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    enlace = models.URLField(max_length=200, blank=True, null=True)
    tipo = models.CharField(max_length=50, choices=[
        ('articulo', 'Artículo'),
        ('video', 'Vídeo'),
        ('guia', 'Guía')
    ])

    def __str__(self):
        return self.titulo


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.DateField()
    descripcion = models.TextField()
    recordatorio = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
"""


