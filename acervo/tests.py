import pytest
from django.urls import reverse
from django.test import Client

# Testes de Unidade (Backend - Regra de Negócio)

def calcular_multa_atraso(dias_atraso: int, taxa_diaria: float = 2.5) -> float:
    """Calcula multa sobre devolução de livros em atraso."""
    if dias_atraso <= 0:
        return 0.0
    return dias_atraso * taxa_diaria

def test_calculo_multa_sem_atraso():
    """Garante que devoluções no prazo não cobram multa."""
    assert calcular_multa_atraso(0) == 0.0

def test_calculo_multa_com_atraso():
    """Garante o cálculo correto por dia de atraso."""
    assert calcular_multa_atraso(3, 2.0) == 6.0


# Testes Simples (Frontend / Interface)

@pytest.mark.django_db
def test_pagina_admin_carrega_com_sucesso():
    """Valida se a rota da interface responde com HTTP 200."""
    client = Client()
    resposta = client.get(reverse('admin:login'))
    assert resposta.status_code == 200

@pytest.mark.django_db
def test_interface_contem_titulo_django():
    """Valida se o elemento HTML esperado é renderizado."""
    client = Client()
    resposta = client.get(reverse('admin:login'))
    conteudo_html = resposta.content.decode('utf-8')
    assert "Django administration" in conteudo_html