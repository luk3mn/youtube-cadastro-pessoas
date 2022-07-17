from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

# 'ListView' Própria para o desenvolvimento de telas de listagem de informação
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Contato, Pessoa # model que será realizado a listagem
from .forms import ContatoForm, PessoaForm # importa o formulário criado

class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo') # Consulta SQL -> retorna todos os registros ordenados pelo nome completo

    # mecanismo de busca
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(usuario=self.request.user) # retorna somente os registros associados ao usuario
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome: # verifica se contem o registro passado no filtro
            queryset = queryset.filter(nome_completo__contains=filtro_nome)
        
        return queryset


class PessoaCreateView(CreateView):
    model = Pessoa # Indica qual é o model de referencia
    form_class = PessoaForm
    success_url = '/pessoas/' # redireciona para outra página (pessoas) quando o cadastro tiver sido realizado

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PessoaUpdateView(UpdateView): # só muda a classe de herança, o princípio é o mesmo
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'

# Para deletar não precisa recuperar os dados do formulario
class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoas/'

# ====================
# = CRUD de contatos =
# ====================
# não está sendo feito o uso das class base views, 
# como: 
# ListView, CreateView, UpdateView, DeleteView
# e sim chamando diretamente os métodos
def contatos(request, pk_pessoa):
    contatos = Contato.objects.filter(pessoa=pk_pessoa)
    # renderiza o html e manda para dentro de 'contato_list.html' o contato e pk_pessoa
    return render(request, 'contato/contato_list.html', {'contatos':contatos, 'pk_pessoa':pk_pessoa})

def contato_novo(request, pk_pessoa):
    form = ContatoForm() # cria uma instância de 'ContatoForm' chamada 'form'
    if request.method == "POST": # testa se o método de requisição é um "POST"
        form = ContatoForm(request.POST) # passa para 'form' todos os campos do formulario 'ContatoForm'
        if form.is_valid(): # valida os campos
            contato = form.save(commit=False) # cria um objeto de contato, salvando ele mas sem persistir no DB
            contato.pessoa_id = pk_pessoa # atribui a qual pessoa aquele contato vai pertencer
            contato.save() # ao final salva no banco
            return redirect(reverse('pessoa.contatos', args=[pk_pessoa])) # retorna pegando o nome da url e passa os parâmetros que a url pede
    
    # se a primeira condição não for satisfeita e redireciona para contato_form.html um formulario vazio        
    return render(request, 'contato/contato_form.html', {'form': form})

def contato_editar(request, pk_pessoa, pk):
    contato = get_object_or_404(Contato, pk=pk) # tenta buscar o 'contato' pelo pk, mas se não encontrar ele retorna imediatamente um 404
    form = ContatoForm(instance=contato) # instancia o formulario caso encontre o contato
    if request.method == "POST": # valida o método de requisição
        form = ContatoForm(request.POST, instance=contato) # busca os campos de formulario e atribui para ainstacia carregado no começo do método
        if form.is_valid(): # valida
            form.save() # salva no banco
            return redirect(reverse('pessoa.contatos', args=[pk_pessoa])) # retorna para a listagem de contatos da pessoa específica

    # retorn um 'form' vazio caso o método for inválido
    return render(request, 'contato/contato_form.html', {'form': form})

def contato_remover(request, pk_pessoa, pk):
    contato = get_object_or_404(Contato, pk=pk) # faz a busca pelo contato filtrando a pk
    contato.delete() # se encontrou, deleta instantanhamente
    return redirect(reverse('pessoa.contatos', args=[pk_pessoa])) # retorna para contatos