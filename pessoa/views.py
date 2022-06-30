from django.shortcuts import render

# 'ListView' Própria para o desenvolvimento de telas de listagem de informação
from django.views.generic import ListView
from .models import Pessoa # model que será realizado a listagem

class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo') # Consulta SQL -> retorna todos os registros ordenados pelo nome completo