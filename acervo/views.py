from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

def lista_livros(request):
    livros = [
        {"id": 1, "titulo": "Código Limpo", "autor": "Robert C. Martin"},
        {"id": 2, "titulo": "Arquitetura Limpa", "autor": "Robert C. Martin"},
        {"id": 3, "titulo": "Entendendo Algoritmos", "autor": "Aditya Y. Bhargava"}
    ]
    return JsonResponse(livros, safe=False)