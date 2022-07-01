from django.shortcuts import render

# 'ListView' Própria para o desenvolvimento de telas de listagem de informação
from django.views.generic import ListView, CreateView
from .models import Pessoa # model que será realizado a listagem
from .forms import PessoaForm # importa o formulário criado

class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo') # Consulta SQL -> retorna todos os registros ordenados pelo nome completo


class PessoaCreateView(CreateView):
    model = Pessoa # Indica qual é o model de referencia
    form_class = PessoaForm
    success_url = '/pessoas/' # redireciona para outra página (pessoas) quando o cadastro tiver sido realizado
