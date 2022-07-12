from django.shortcuts import render

# 'ListView' Própria para o desenvolvimento de telas de listagem de informação
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pessoa # model que será realizado a listagem
from .forms import PessoaForm # importa o formulário criado

class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo') # Consulta SQL -> retorna todos os registros ordenados pelo nome completo

    # mecanismo de busca
    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome: # verifica se contem o registro passado no filtro
            queryset = queryset.filter(nome_completo__contains=filtro_nome)
        
        return queryset


class PessoaCreateView(CreateView):
    model = Pessoa # Indica qual é o model de referencia
    form_class = PessoaForm
    success_url = '/pessoas/' # redireciona para outra página (pessoas) quando o cadastro tiver sido realizado

class PessoaUpdateView(UpdateView): # só muda a classe de herança, o princípio é o mesmo
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'

# Para deletar não precisa recuperar os dados do formulario
class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoas/'