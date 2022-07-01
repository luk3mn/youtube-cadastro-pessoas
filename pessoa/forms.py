from django import forms # para auxiliar na criação do usuário que interage com a model
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa # para saber com qual model ele precisa fazer referencia
        fields = ['nome_completo', 'data_nascimento', 'ativa']