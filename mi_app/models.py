from django.db import models

# Create your models here.
# Load and inspect the provided files to understand the current structure of the project.

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


