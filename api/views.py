from django.shortcuts import render
from django.http import JsonResponse
from .models import Usuario

def hello_world(request):
    return HttpResponse("Hello World!")
# Create your views here.

def usuarios(request):
    usuarios = Usuario.objects.all()

    dados = []

    for usuario in usuarios:
        dados.append({
            "id": usuario.id,
            "nome": usuario.nome
        })

    return JsonResponse(dados, safe=False)
