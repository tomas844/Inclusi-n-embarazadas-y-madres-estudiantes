from django.urls import path
from . import views

urlpatterns = [
    path('', views.mi_app, name='mi_app'),
]
# Adding views for 'biblioteca_recursos' and 'agenda' functionalities in views.py
views_content = """
from django.shortcuts import render
from .models import Recurso, Evento

def biblioteca_recursos(request):
    recursos = Recurso.objects.all()
    return render(request, 'biblioteca/biblioteca_recursos.html', {'recursos': recursos})

def agenda(request):
    eventos = Evento.objects.all().order_by('fecha')
    return render(request, 'biblioteca/agenda.html', {'eventos': eventos})
"""

