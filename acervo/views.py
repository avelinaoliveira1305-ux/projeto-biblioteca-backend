from rest_framework.response import Response  
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny 
from rest_framework.views import APIView 
from rest_framework import status 
from .serializers import UserRegistrationSerializer 

livros_db = [
    {"id_livro": 1, "titulo": "CÓDIGO LIMPO", "ano_publicacao": 2008, "id_autor": 1},
    {"id_livro": 2, "titulo": "ARQUITETURA LIMPA", "ano_publicacao": 2017, "id_autor": 1},
    {"id_livro": 3, "titulo": "ENTENDENDO ALGORITMOS", "ano_publicacao": 2017, "id_autor": 2}
]

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def lista_livros(request):
    
    return Response(livros_db)

@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def busca_livro_por_id(request, id):
    livro = next((item for item in livros_db if item["id_livro"] == id), None)
    
    if livro:
       
        return Response(livro)
    else:
        
        return Response({"erro": "Livro não encontrado"}, status=404)
    from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer

class UserRegistrationView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Usuário cadastrado com sucesso!"}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)