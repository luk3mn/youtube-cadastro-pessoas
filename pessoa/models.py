from django.db import models

# Criação dos models de Pessoa
class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=250)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)