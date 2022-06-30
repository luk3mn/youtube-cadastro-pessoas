from django.shortcuts import render

# 'TemplateView' -> É uma classe para renderizar uma página para listar algum conteúdo sem função expecífica
from django.views.generic import TemplateView

# cria a classe informando o template que precisa renderizar
class HomeView(TemplateView):
    template_name = 'main/index.html' # não precisa passar a pasta 'template'