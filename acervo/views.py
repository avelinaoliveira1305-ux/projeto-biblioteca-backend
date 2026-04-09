from django.http import JsonResponse


livros_db = [
    {"id_livro": 1, "titulo": "CÓDIGO LIMPO", "ano_publicacao": 2008, "id_autor": 1},
    {"id_livro": 2, "titulo": "ARQUITETURA LIMPA", "ano_publicacao": 2017, "id_autor": 1},
    {"id_livro": 3, "titulo": "ENTENDENDO ALGORITMOS", "ano_publicacao": 2017, "id_autor": 2},
]


def lista_livros(request):
    return JsonResponse(livros_db, safe=False)


def busca_livro_por_id(request, id):
    # Procura o livro específico na lista
    livro = next((item for item in livros_db if item["id_livro"] == id), None)
    
    if livro:
        return JsonResponse(livro)
    else:
        return JsonResponse({"erro": "Livro não encontrado"}, status=404)