from django.urls import path
from . import views

urlpatterns = [
    path('acervo/', views.lista_livros),
]