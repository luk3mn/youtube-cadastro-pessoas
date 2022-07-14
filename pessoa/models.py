from django.db import models

# Criação dos models de Pessoa
class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=250)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)

    # retorna o que queremos exibir quando o sistema fizaer a chamada do objeto
    def __str__(self) -> str:
        return self.nome_completo

# SERÁ CRIADA UMA MODEL DE CONTATO DENTRO DO 
# APP 'Pessoa', MAS O IDEAL SERIA CRIAR UM 
# NOVO APP PARA CONTATO E ESTRUTURAR A MODEL 
# DENTRO DELE.
class Contato(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    telefone = models.CharField(max_length=20)
    # - indica que é chave estrangeira de Pessoa;
    # - informa que caso a pessoa seja deleta do DB, os contatos vinculados a ela tambem serão removidas
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome