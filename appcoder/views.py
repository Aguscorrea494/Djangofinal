from django.shortcuts import render
from django.http import HttpResponse
from appcoder.models import Curso


def crear_curso(request):
    curso = Curso(nombre="Python", camada=47785)
    contexto = {"Curso": curso}
    curso.save()

    return render(request, template_name= "index.html", context= contexto)

def show_html(request):
    curso = Curso.objects.first()
    contexto = {"Curso": curso}
    return render(request, template_name= "index.html", context= contexto)
