from django import forms # para auxiliar na criação do usuário que interage com a model
from .models import Contato, Pessoa

class PessoaForm(forms.ModelForm):
    # exibe o campo 'Data Nascimento' no formato de 'Date'
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type":"date"}
        )
    )

    class Meta:
        model = Pessoa # para saber com qual model ele precisa fazer referencia
        fields = ['nome_completo', 'data_nascimento', 'ativa']

# class para o formulario de Contatos
class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato # referencia a model de contatos
        fields = ['nome', 'email', 'telefone'] # informa os campos do formulario